from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    class Estado(models.TextChoices):
        ARCHIVADO = "ARCHIVADO", "Archivado"
        PERDIDO = "PERDIDO", "Perdido"
        PRESTADO = "PRESTADO", "Prestado"
        DISPONIBLE = "DISPONIBLE", "Disponible"
    titulo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True)
    sinopsis = models.TextField(blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name="libros",
        null=True,
        blank=True,
    )
    autores = models.ManyToManyField(Autor, related_name="libros", blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo