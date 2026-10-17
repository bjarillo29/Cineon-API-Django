
from rest_framework import serializers
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


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = "__all__"


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = "__all__"


class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"


class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = "__all__"
