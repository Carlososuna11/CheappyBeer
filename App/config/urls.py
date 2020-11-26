"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config.views import *
from django.views.generic import *
from core.Licores.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Indexview.as_view(),name='home'),
    path('catalogo',Catalogo.as_view(),name='catalogo'),
    path('crear',CrearLicor.as_view(),name='crear'),
    path('editar/<int:pk>',ModificarLicor.as_view(),name='editar'),
    path('catalogo/descripcion/<str:nombre>/<int:pk>',DescripcionLicor.as_view(),name='descripcion'),
    path('listalicores', ListaLicores.as_view(), name= 'listalicores'),
    path('catalogo/filtro/<str:tipo>/<str:precio>/<str:ubicacion>/<str:valoracion>',CatalogoFiltro.as_view(),name="filtrico")
]