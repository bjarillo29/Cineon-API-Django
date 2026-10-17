
from django.contrib import admin
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

admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Asiento)
admin.site.register(Funcion)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(DetalleReserva)
