
from django.shortcuts import render
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


# Página principal de Cineon
def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(
        request,
        "Cine/Inicio.html",
        {"peliculas": peliculas},
    )


# API de usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# API de películas
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


# API de salas
class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


# API de asientos
class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer


# API de funciones
class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer


# API de reservas
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


# API de pagos
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# API de detalles de reserva
class DetalleReservaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReserva.objects.all()
    serializer_class = DetalleReservaSerializer
