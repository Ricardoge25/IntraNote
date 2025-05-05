from django import forms 
from .models import Incident

class IncidentForm(forms.ModelForm):

    class Meta:
        model = Incident
        fields = ['id_servicio', 'nombre_anillo', 'nombre_cliente', 'nit', 'nombre_contacto',
        'numero_contacto', 'correo_contacto', 'direccion_servicio', 'ip', 'observaciones']
        widgets = {
        'id_servicio': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'nombre_anillo': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'nombre_cliente': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'nit': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'nombre_contacto': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'numero_contacto': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'correo_contacto': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
        'direccion_servicio': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'ip': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        'observaciones': forms.Textarea(attrs={'class': 'form-control mb-3'}), 
        }

class AperturaEntreClientesForm(forms.Form):
    nro_incidente = forms.CharField(
        max_length=30,
        label='Número de incidente',
        required=False)
    ciudad = forms.CharField(
        max_length=30,
        label='Ciudad')
    giga_caida_A = forms.CharField(
        max_length=10, 
        label='Giga caida Extremo A')
    cliente_extremo_B = forms.CharField(
        max_length=100, 
        label='Cliente extremo B',)
    identificador_extremo_B = forms.CharField(
        max_length=100, 
        label='Identificador extremo B')
    giga_caida_B = forms.CharField(
        max_length=10, 
        label='Giga caida Extremo B')
    direccion_b = forms.CharField(
        max_length=100, 
        label='Dirección Extremo B')
    contacto_b = forms.CharField(
        max_length=100, 
        label='Contacto Extremo B')
    telefono_b = forms.CharField(
        max_length=15, 
        label='Teléfono Extremo B')
    correo_b = forms.EmailField(
        max_length=100,
        label='Correo Extremo B')
    ip_switch_b = forms.CharField(
        max_length=15, 
        label='IP Switch Extremo B')

    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base

class EquipoCaidoForm(forms.Form):
    nro_incidente = forms.CharField(
        max_length=30,
        label='Número de incidente',
        required=False)    
    ciudad = forms.CharField(
        max_length=30,
        label='Ciudad',
        required=False)
    ip_sw_vecinoA = forms.CharField(
        max_length=15, 
        label='IP Switch Vecino A',
        required=False)
    ip_sw_vecinoB = forms.CharField(
        max_length=15, 
        label='IP Switch Vecino B',
        required=False)
    
    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base

class NotaLlamadaForm(forms.Form):
    id_llamada1 = forms.CharField(
        max_length=20, 
        label='ID Llamada 1', 
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    id_llamada2 = forms.CharField(
        max_length=20,
        label='ID Llamada 2', 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    id_llamada3 = forms.CharField(
        max_length=20, 
        label='ID Llamada 3', 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        label='Observaciones de la llamada')
    
    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs) 

class AperturaContraCentralForm(forms.Form):

    nro_incidente = forms.CharField(
        max_length=30,
        label='Número de incidente',
        required=False)
    ciudad = forms.CharField(
        max_length=30,
        label='Ciudad')
    giga_caida_A = forms.CharField(
    max_length=10, 
    label='Giga caida Extremo A')    
    nombre_central = forms.CharField(
        max_length=30,
        label='Nombre de la Central')
    giga_central = forms.CharField(
        max_length=15,
        label='Giga de la Central')
    ip_sw_central = forms.CharField(
        max_length=15,
        label='IP de la Central')
    
    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base

class AlarmaPotencias(forms.Form):
    ciudad = forms.CharField(
        max_length=30,
        label='Ciudad')
    giga_extremo_A = forms.CharField(
        max_length=10,
        label = 'Giga Alarmada Extremo A')
    parametros = forms.CharField(
        max_length=10,
        label='Parámetros alarmados')
    cliente_extremo_B = forms.CharField(
        max_length=40,
        label= 'Cliente Extremo B')
    giga_extremo_B = forms.CharField(
        max_length=10,
        label='Giga Extremo B')

    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base

class TicketApDobleUnoForm(forms.Form):
    ciudad = forms.CharField(
        max_length=30,
        label='Ciudad')
    disponibilidad = forms.CharField(
        max_length=20, 
        label='Disponibilidad')
    descartes = forms.CharField(
        widget=forms.Textarea(attrs=
            {'class': 'form-control',
            'rows': 5
        }), 
        label="Descartes Realizados")

    def __init__(self, *args, **kwargs):
        self.incident = kwargs.pop('incident', None)  # Extraer el argumento 'incident'
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base