from django import forms

class ContactoForm(forms.Form):
    # label es la etiqueta del campo del form
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
        
    contenido = forms.CharField(label='Contenido ', widget=forms.Textarea)