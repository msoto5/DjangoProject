from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La direccion") 
    # verbose_name="La direccion" is the name that will be displayed in the admin page
    email = models.EmailField(blank=True, null=True)
    # blank=True, null=True means that the field is optional
    tlfno = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return "El nombre del articulo es %s, la seccion es %s y el precio es" \
               " %s" %(self.nombre, self.seccion, self.precio)
    
class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
