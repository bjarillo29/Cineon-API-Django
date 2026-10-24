
from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        db_table = "usuarios"


class Pelicula(models.Model):
    id_peliculas = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    genero = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=20)
    duracion = models.PositiveIntegerField()
    fecha_estreno = models.DateField()
    portada = models.ImageField(
        upload_to="portadas/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "peliculas"


class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "salas"


class Asiento(models.Model):
    id_asiento = models.AutoField(primary_key=True)
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        db_column="id_sala",
        related_name="asientos"
    )
    fila = models.CharField(max_length=5)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sala.nombre} - {self.fila}{self.numero}"

    class Meta:
        db_table = "asientos"


class Funcion(models.Model):
    id_funcion = models.AutoField(primary_key=True)
    sala = models.ForeignKey(
        Sala,
        on_delete=models.PROTECT,
        db_column="id_sala",
        related_name="funciones"
    )
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.PROTECT,
        db_column="id_pelicula",
        related_name="funciones"
    )
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.fecha}"

    class Meta:
        db_table = "funciones"


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        db_column="id_usuario",
        related_name="reservas"
    )
    funcion = models.ForeignKey(
        Funcion,
        on_delete=models.PROTECT,
        db_column="id_funcion",
        related_name="reservas"
    )
    cantidad_boletos = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva {self.id_reserva}"

    class Meta:
        db_table = "reservas"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.PROTECT,
        db_column="id_reserva",
        related_name="pagos"
    )
    metodo_pago = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField()
    estado = models.CharField(max_length=30)

    def __str__(self):
        return f"Pago {self.id_pago} - {self.estado}"

    class Meta:
        db_table = "pagos"


class DetalleReserva(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.CASCADE,
        db_column="id_reserva",
        related_name="detalles"
    )
    asiento = models.ForeignKey(
        Asiento,
        on_delete=models.PROTECT,
        db_column="id_asiento",
        related_name="reservas"
    )

    def __str__(self):
        return f"Detalle {self.id_detalle}"

    class Meta:
        db_table = "detalle_reserva"
