'''
templatetags module
'''

from django import template
from core.Licores.models import *
register = template.Library()

@register.simple_tag
def go_to_url(url):
    return "window.location='" + url +"'; return false;"


@register.filter
def to_and(value):
    return str(value).replace("core/Licores/static","")

@register.filter
def val(value,pos):
    return value[pos]

@register.filter
def desc(value,a):
    return Licor.objects.get(id=a[value][0][1]).descripcion

@register.filter
def to_and_img(value,imagenx):
    return str(Licor.objects.get(id=imagenx[value][0][1]).imagen).replace("core/Licores/static","")

@register.filter
def mas_barato(value,diccionario):
    return diccionario[value][0][0]

@register.filter
def cinco(value,nombre):
    return value[nombre][:5]

@register.filter
def uno(value,nombre):
    return value[nombre][0]

@register.filter
def productos_pro(provedor,index):
    return provedor[index]

@register.filter
def to_and_licores(nombre):
    return str(list(Licor.objects.filter(nombre=nombre))[0].imagen).replace("core/Licores/static","")

@register.filter
def fist_id_name(nombre):
    return list(Licor.objects.filter(nombre=nombre))[0].id