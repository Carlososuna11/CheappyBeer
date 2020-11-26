from core.Licores.forms import LicorForm
from django.http import *
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from core.Licores.models import * 
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator

class Catalogo(ListView):
    model = Licor
    template_name = 'Licores/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nombres=[]
        precios={}
        #{'anis':[[12,1,saco],[],[]]}
        provedores_n =[]
        provedor={}
        for i in Licor.objects.all():
            if i.nombre.lower() not in nombres:
                nombres.append(i.nombre)
                precios[i.nombre]=[]
            if i.nombre_provedor.lower() not in provedores_n:
                provedores_n.append(i.nombre_provedor)
                provedor[i.nombre_provedor] = []
            provedor[i.nombre_provedor].append(i)
            precios[i.nombre].append([i.precio,i.id,i.nombre_provedor])
        for key,value in precios.items():
            precios[key].sort(key=lambda x:x[0])
        print(nombres)
        context['nombres']=nombres
        context['precios']=precios
        context['provedores_n'] = provedores_n
        context['provedores']= provedor
        context['title'] = 'Catálogo de Productos'
        return context


class DescripcionLicor(ListView):
    model= Licor
    template_name = 'Licores/descripcion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Licor'] = get_object_or_404(Licor, id=self.kwargs['pk'])
        context['Licores'] = Licor.objects.filter(nombre=self.kwargs['nombre']).exclude(id=self.kwargs['pk'])
        print(context['Licor'])
        for licor in context['Licores']:
            print(licor)
        context['title'] = 'Descripción del Producto'
        return context


class CrearLicor(CreateView):
    model = Licor
    form_class = LicorForm
    template_name = 'Licores/formulario_licor.html'
    success_url = '/listalicores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un Licor'
        context['imagen'] = 'img/None.png'
        return context


class ModificarLicor(UpdateView):
    model= Licor
    form_class = LicorForm
    template_name = 'Licores/formulario_licor.html'
    success_url = '/listalicores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Licor'
        context['imagen'] = str(self.get_object().imagen).replace("core/Licores/static","")
        return context

class ListaLicores(ListView):
    model = Licor
    template_name = 'Licores/lista_licores.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        id_field = int(request.POST['id'])
        try:
            Licor.objects.get(pk=id_field).delete()
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Licores'
        return context