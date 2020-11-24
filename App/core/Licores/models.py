from django.db import models
from django.core.validators import *
from django.db.models.deletion import CASCADE, SET_NULL 
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Sabor(models.Model):
    sabor = models.CharField('Sabor del Licor',max_length=20,unique= True,primary_key=True)
 
    def __str__(self) -> str:
        return self.sabor
class Tipo(models.Model):
    tipo = models.CharField('Tipo de Licor',max_length=20,unique= True,primary_key=True)

    def __str__(self) -> str:
        return f"{self.tipo}"
class Grado_Alcoholico(models.Model):
    grado = models.FloatField('Grado Alcohol',validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],unique= True,primary_key=True)

    def __str__(self) -> str:
        return f"{self.grado}°"
# class Imagen(models.Model):
#     imagen = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

class Marca(models.Model):
    marca = models.CharField('Marca del Licor', max_length=20,unique=True,primary_key=True)

    def __str__(self) -> str:
        return self.marca
class Pais(models.Model):
    pais = models.CharField('Pais de Origen',max_length=20,unique=True,primary_key=True)

    def __str__(self) -> str:
        return self.pais

class Tamano(models.Model):
    class Opciones_Unidad(models.TextChoices):
        LITROS = 'L', _('Litros')
        MILILITROS = 'mL', _('Mililitros')

    tamano = models.FloatField('Tamaño del licor')
    unidad = models.CharField('Unidad de Medida',max_length=2,choices=Opciones_Unidad.choices,default=Opciones_Unidad.LITROS,unique=True)

    def __str__(self) -> str:
        return f"{self.tamano} {self.unidad}"

class Material(models.Model):
    material = models.CharField('Material', max_length=20)
    
    def __str__(self) -> str:
        return self.material
class Licor(models.Model):
    nombre = models.CharField(verbose_name='Nombre del Licor',null=False, max_length=30)
    id_licor = models.CharField(max_length=20,unique=True)
    precio = models.FloatField(validators=[MinValueValidator(0.0)])    
    #material = models.ManyToManyField(Material,through="hecho",through_fields=("Licor","Material"))
    sabor = models.ManyToManyField(Sabor)
    tipo = models.ForeignKey(Tipo,on_delete=CASCADE)
    Tamano = models.ForeignKey(Tamano,on_delete=CASCADE)
    pais = models.ForeignKey(Pais,on_delete=CASCADE)
    marca = models.ForeignKey(Marca,on_delete=CASCADE)
    grado = models.ForeignKey(Grado_Alcoholico,on_delete=CASCADE)
    material = models.ForeignKey(Material,on_delete=CASCADE)
        
    class Meta:
        verbose_name = 'Licor'
        verbose_name_plural = 'Licores'