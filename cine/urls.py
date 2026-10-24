
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register("usuarios", views.UsuarioViewSet)
router.register("peliculas", views.PeliculaViewSet)
router.register("salas", views.SalaViewSet)
router.register("asientos", views.AsientoViewSet)
router.register("funciones", views.FuncionViewSet)
router.register("reservas", views.ReservaViewSet)
router.register("pagos", views.PagoViewSet)
router.register("detalles-reserva", views.DetalleReservaViewSet)


urlpatterns = [
    path("", views.inicio, name="inicio"),

    path(
        "pelicula/<int:id>/",
        views.detalle_pelicula,
        name="detalle_pelicula"
    ),

    path(
        "funcion/<int:id_funcion>/asientos/",
        views.elegir_asientos,
        name="elegir_asientos"
    ),

    path(
        "reserva/<int:id_reserva>/confirmacion/",
        views.confirmacion_reserva,
        name="confirmacion_reserva"
    ),

    path("api/", include(router.urls)),
]
