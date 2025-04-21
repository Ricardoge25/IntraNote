from django import forms 

class caido_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente',) 
  estado = forms.BooleanField(
    label='¿Activo?',
    required=False)