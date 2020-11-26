from django.forms import * 
from core.Licores.models import *



class LicorForm(ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        count = 0
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
            form.field.widget.attrs['id'] = str(count)
            form.field.widget.attrs['class']='row'
            if form.name == 'imagen':
                form.field.widget.attrs['onchange'] = 'readURL(this);'
            count+=1
            if count == 3:
                count=0
    
    class Meta:
        model = Licor
        fields = '__all__'
        exclude = ['valoracion']
        widgets = {
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese una Descripcion...',
                    'rows': 4,
                    'cols': 90,
                }
            ),
        }
        
