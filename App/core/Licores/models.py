from django.db import models
from django.core.validators import *
from django.db.models.deletion import CASCADE, SET_NULL 
from django.utils.translation import gettext_lazy as _
# Create your models here.

# class Sabor(models.Model):
#     sabor = models.CharField('Sabor del Licor',max_length=20,unique= True,primary_key=True)
 
#     def __str__(self) -> str:
#         return self.sabor
# class Tipo(models.Model):
#     tipo = models.CharField('Tipo de Licor',max_length=20,unique= True,primary_key=True)

#     def __str__(self) -> str:
#         return f"{self.tipo}"
# class Grado_Alcoholico(models.Model):
#     grado = models.FloatField('Grado Alcohol',validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],unique= True,primary_key=True)

#     def __str__(self) -> str:
#         return f"{self.grado}°"
# # class Imagen(models.Model):
# #     imagen = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

# class Marca(models.Model):
#     marca = models.CharField('Marca del Licor', max_length=20,unique=True,primary_key=True)

#     def __str__(self) -> str:
#         return self.marca
# class Pais(models.Model):
#     pais = models.CharField('Pais de Origen',max_length=20,unique=True,primary_key=True)

#     def __str__(self) -> str:
#         return self.pais

# class Tamano(models.Model):
#     class Opciones_Unidad(models.TextChoices):
#         LITROS = 'L', _('Litros')
#         MILILITROS = 'mL', _('Mililitros')

#     tamano = models.FloatField('Tamaño del licor')
#     unidad = models.CharField('Unidad de Medida',max_length=2,choices=Opciones_Unidad.choices,default=Opciones_Unidad.LITROS,unique=True)

#     def __str__(self) -> str:
#         return f"{self.tamano} {self.unidad}"

# class Material(models.Model):
#     material = models.CharField('Material', max_length=20)
    
#     def __str__(self) -> str:
#         return self.material
 
class Licor(models.Model):
    # class Opciones_Unidad(models.TextChoices):
    #      LITROS = 'L', _('Litros')
    #      MILILITROS = 'mL', _('Mililitros')
    # nombre = models.CharField(verbose_name='Nombre del Licor',null=False, max_length=30,)
    # id_licor = models.CharField(max_length=20,unique=True,primary_key=True,null=False)
    # precio = models.FloatField(validators=[MinValueValidator(0.0)],null=False)
    # material = models.CharField('Material', max_length=20,null=False)
    # tamano = models.FloatField('Tamaño del licor',validators=[MinValueValidator(0.0)],default=0.0,null=False)
    # unidad = models.CharField('Unidad de Medida',max_length=2,choices=Opciones_Unidad.choices,default=Opciones_Unidad.LITROS)
    # pais = models.CharField('Pais de Origen',max_length=20,null=False)
    # marca = models.CharField('Marca del Licor', max_length=20,null=False)
    # grado = models.FloatField('Grado Alcohol',validators=[MinValueValidator(0.0),MaxValueValidator(100.0)],null=False)
    # tipo = models.CharField('Tipo de Licor',max_length=20,null=False)
    # sabor = models.CharField('Sabor del Licor',max_length=20,null=False)
    # imagen = models.ImageField("Imagen del Licor",upload_to='core/Licores/static/Licores/img', height_field=None, width_field=None, max_length=100,default = 'core/Licores/static/Licores/img/Default.jpg')
    class Opciones_Municipios(models.TextChoices):
        Santa_Rosalia = 'Santa Rosalía',_('Santa Rosalía')
        El_Valle= 'El Valle',_('El Valle')
        Coche = 'Coche',_('Coche')
        Caricuao = 'Caricuao',_('Caricuao')
        Macarao = 'Macarao',_('Macarao')
        Antimano = 'Antimano',_('Antímano')
        Vega = 'La Vega',_('La Vega')
        Paraiso = 'El Paraíso',_('El Paraíso')
        junquito = 'El Junquito',_('El Junquito')
        sucre = 'Sucre (Catia)',_('Sucre (Catia)')
        sanjuan='San Juan' ,_('San Juan')
        santateresa = 'Santa Teresa',_('Santa Teresa')
        enero = '23 de enero',_('23 de enero')
        lapastora = 'La Pastora' ,_('La Pastora')
        altagracia = 'Altagracia' ,_('Altagracia')
        sanjose = 'San José' ,_('San José')
        sanbenardino = 'San Bernardino' ,_('San Bernardino')
        catedral ='Catedral',_('Catedral')
        candelaria = 'Candelaria',_('Candelaria')
        sanagustin = 'San Agustín',_('San Agustín')
        recreo = 'El Recreo',_('El Recreo')
        sanpedro = 'San Pedro' ,_('San Pedro')




    nombre = models.CharField(verbose_name='Nombre del Licor',null=False, max_length=30)
    #id_licor = models.CharField(max_length=20,unique=True,primary_key=True,null=False)
    nombre_provedor = models.CharField(verbose_name='Nombre del Proovedor',null=False, max_length=30)
    precio = models.FloatField(validators=[MinValueValidator(0.0)],null=False)
    tipo = models.CharField('Tipo de Licor',max_length=20,null=False)
    valoracion = models.FloatField('Valoracion',validators=[MinValueValidator(0.0),MaxValueValidator(5.0)],null=False,default = 0.0)
    imagen = models.ImageField("Imagen del Licor",upload_to='core/Licores/static/Licores/img', height_field=None, width_field=None, max_length=100,default = 'img/None.png')
    ubicacion = models.TextField('Ubicación',choices=Opciones_Municipios.choices,default=Opciones_Municipios.recreo)
    stock = models.IntegerField('Stock',validators=[MinValueValidator(1)],null=False)
    descripcion = models.TextField("Descripcion del Producto",null = False)
    # #material = models.ManyToManyField(Material,through="hecho",through_fields=("Licor","Material"))
    # sabor = models.ManyToManyField(Sabor)
    # tipo = models.ForeignKey(Tipo,on_delete=CASCADE)
    # Tamano = models.ForeignKey(Tamano,on_delete=CASCADE)
    # pais = models.ForeignKey(Pais,on_delete=CASCADE)
    # marca = models.ForeignKey(Marca,on_delete=CASCADE)
    # grado = models.ForeignKey(Grado_Alcoholico,on_delete=CASCADE)
    # material = models.ForeignKey(Material,on_delete=CASCADE)
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.lower()
        self.nombre_provedor = self.nombre_provedor.lower()
        self.tipo = self.tipo.lower()
        return super(Licor, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.nombre} {self.nombre_provedor} {self.precio} {self.stock}'
    class Meta:
        verbose_name = 'Licor'
        verbose_name_plural = 'Licores'
        ordering = ['id']