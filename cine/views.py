
from decimal import Decimal

from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from rest_framework import viewsets

from .models import (
    Usuario,
    Pelicula,
    Sala,
    Asiento,
    Funcion,
    Reserva,
    Pago,
    DetalleReserva,
)

from .serializers import (
    UsuarioSerializer,
    PeliculaSerializer,
    SalaSerializer,
    AsientoSerializer,
    FuncionSerializer,
    ReservaSerializer,
    PagoSerializer,
    DetalleReservaSerializer,
)


# =========================
# PAGINA DE INICIO
# =========================

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(
        request,
        "Cine/Inicio.html",
        {"peliculas": peliculas}
    )


# =========================
# DETALLE DE PELICULA
# =========================

def detalle_pelicula(request, id):
    pelicula = get_object_or_404(
        Pelicula,
        id_peliculas=id
    )

    funciones = (
        Funcion.objects
        .filter(pelicula=pelicula)
        .select_related("sala")
        .order_by("fecha", "hora")
    )

    return render(
        request,
        "Cine/DetallePelicula.html",
        {
            "pelicula": pelicula,
            "funciones": funciones,
        }
    )


# =========================
# SELECCION Y CONFIRMACION DE ASIENTOS
# =========================

def elegir_asientos(request, id_funcion):
    funcion = get_object_or_404(
        Funcion.objects.select_related("pelicula", "sala"),
        id_funcion=id_funcion
    )

    asientos = (
        funcion.sala.asientos
        .all()
        .order_by("fila", "numero")
    )

    asientos_reservados = list(
        DetalleReserva.objects
        .filter(reserva__funcion=funcion)
        .values_list("asiento_id", flat=True)
        .distinct()
    )

    if request.method == "POST":
        ids_asientos = request.POST.getlist("asientos")

        # Evita solicitudes vacias o asientos repetidos.
        ids_asientos = list(dict.fromkeys(ids_asientos))

        if not ids_asientos:
            messages.error(
                request,
                "Selecciona al menos un asiento."
            )
            return redirect(
                "elegir_asientos",
                id_funcion=funcion.id_funcion
            )

        # Verifica que todos los asientos pertenezcan a la sala.
        asientos_seleccionados = list(
            Asiento.objects
            .filter(
                id_asiento__in=ids_asientos,
                sala=funcion.sala
            )
            .order_by("id_asiento")
        )

        if len(asientos_seleccionados) != len(ids_asientos):
            messages.error(
                request,
                "Uno o mas asientos no son validos para esta sala."
            )
            return redirect(
                "elegir_asientos",
                id_funcion=funcion.id_funcion
            )

        try:
            with transaction.atomic():
                # Bloquea las filas de asiento durante la operacion.
                list(
                    Asiento.objects
                    .select_for_update()
                    .filter(
                        id_asiento__in=ids_asientos,
                        sala=funcion.sala
                    )
                    .order_by("id_asiento")
                )

                # Vuelve a consultar los asientos ya reservados.
                ocupados = list(
                    DetalleReserva.objects
                    .filter(
                        reserva__funcion=funcion,
                        asiento_id__in=ids_asientos
                    )
                    .values_list("asiento_id", flat=True)
                    .distinct()
                )

                if ocupados:
                    nombres_ocupados = [
                        str(asiento)
                        for asiento in asientos_seleccionados
                        if asiento.id_asiento in ocupados
                    ]
                    raise ValueError(
                        "Estos asientos ya fueron reservados: "
                        + ", ".join(nombres_ocupados)
                    )

                # Usa el primer usuario registrado como usuario de prueba.
                usuario = Usuario.objects.order_by("id_usuario").first()

                if usuario is None:
                    raise ValueError(
                        "No existe ningun usuario en la base de datos. "
                        "Crea uno desde el administrador de Django."
                    )

                cantidad = len(asientos_seleccionados)
                total = funcion.precio * Decimal(cantidad)

                reserva = Reserva.objects.create(
                    usuario=usuario,
                    funcion=funcion,
                    cantidad_boletos=cantidad,
                    total=total
                )

                DetalleReserva.objects.bulk_create([
                    DetalleReserva(
                        reserva=reserva,
                        asiento=asiento
                    )
                    for asiento in asientos_seleccionados
                ])

                # Pago de demostracion: no se realiza ningun cobro real.
                Pago.objects.create(
                    reserva=reserva,
                    metodo_pago="Simulado",
                    monto=total,
                    fecha_pago=timezone.now(),
                    estado="Simulado"
                )

            return redirect(
                "confirmacion_reserva",
                id_reserva=reserva.id_reserva
            )

        except ValueError as error:
            messages.error(request, str(error))
            return redirect(
                "elegir_asientos",
                id_funcion=funcion.id_funcion
            )

    return render(
        request,
        "Cine/ElegirAsientos.html",
        {
            "funcion": funcion,
            "asientos": asientos,
            "asientos_reservados": asientos_reservados,
        }
    )


# =========================
# CONFIRMACION DE RESERVA
# =========================

def confirmacion_reserva(request, id_reserva):
    reserva = get_object_or_404(
        Reserva.objects.select_related(
            "usuario",
            "funcion__pelicula",
            "funcion__sala"
        ).prefetch_related(
            "detalles__asiento",
            "pagos"
        ),
        id_reserva=id_reserva
    )

    return render(
        request,
        "Cine/ConfirmacionReserva.html",
        {"reserva": reserva}
    )


# =========================
# API DE USUARIOS
# =========================

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# =========================
# API DE PELICULAS
# =========================

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


# =========================
# API DE SALAS
# =========================

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


# =========================
# API DE ASIENTOS
# =========================

class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer


# =========================
# API DE FUNCIONES
# =========================

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer


# =========================
# API DE RESERVAS
# =========================

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


# =========================
# API DE PAGOS
# =========================

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# =========================
# API DE DETALLES DE RESERVA
# =========================

class DetalleReservaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReserva.objects.all()
    serializer_class = DetalleReservaSerializer
