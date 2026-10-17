
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
    path("api/", include(router.urls)),
]
