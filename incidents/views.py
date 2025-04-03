from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Incident
from . import forms

"""class AuthenticatedRequiredMixin():
    
    Este mixin se utiliza para verificar si el usuario está autenticado
    
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedRequiredMixin, self).dispatch(request, *args, **kwargs)
"""
# Create your views here.
class ListIncidentView(LoginRequiredMixin, ListView):
    model = Incident

    def get_queryset(self):
        #Filtramos los incidentes para mostrar solo los del usuario actual
        return Incident.objects.filter(usuario=self.request.user)

class IncidentDetailView(DetailView):
    model = Incident

    def get_queryset(self):
        # Filtra para permitir acceso solo a los incidentes propios
        return Incident.objects.filter(usuario=self.request.user)

class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    form_class = forms.IncidentForm
    success_url = reverse_lazy('incidents:incidents')

    def form_valid(self, form):
        # Asigna el usuario actual antes de guardar
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class IncidentUpdateView(UpdateView):
    model = Incident
    form_class = forms.IncidentForm
    template_name_suffix = "_update_form"

    def get_queryset(self):
        # Filtra para permitir editar solo los incidentes propios
        return Incident.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy('incidents:update', args=[self.object.id]) + '?ok'
    
class IncidentDeleteView(DeleteView):
    model = Incident
    success_url = reverse_lazy("incidents:incidents")

    def get_queryset(self):
        # Filtra para permitir eliminar solo los incidentes propios
        return Incident.objects.filter(usuario=self.request.user)

class BaseIncidentView(View):
    template_name = None
    form_class = None

    def get(self, request, incident_id, *args, **kwargs):
        incident = get_object_or_404(Incident, pk=incident_id)
        form = self.form_class()
        return render(request, self.template_name, {
            'incident': incident,
            'form': form,
            'texto': None
        })  

    def post(self, request, incident_id, *args, **kwargs):
        incident = get_object_or_404(Incident, pk=incident_id)
        form = self.form_class(request.POST, incident=incident)
        texto = None
        if form.is_valid():
            texto = self.generar_texto(form, incident)
        return render(request, self.template_name, {
            'form': form,
            'incident': incident,
            'texto': texto
        })

    def generar_texto(self, form, incident):
        # Este método debe ser implementado en las subclases
        raise NotImplementedError("La subclase debe implemetar este método")

class AperturaEntreClientes(BaseIncidentView):
    template_name = 'incidents/apertura_entre_clientes.html'
    form_class = forms.AperturaEntreClientesForm

    def generar_texto(self, form, incident):
        nro_incidente = form.cleaned_data['nro_incidente']
        ciudad = form.cleaned_data['ciudad']
        giga_caida_A = form.cleaned_data['giga_caida_A']
        cliente_extremo_B = form.cleaned_data['cliente_extremo_B']
        identificador_extremo_B = form.cleaned_data['identificador_extremo_B']
        giga_caida_B = form.cleaned_data['giga_caida_B']
        direccion_b = form.cleaned_data['direccion_b']
        contacto_b = form.cleaned_data['contacto_b']
        telefono_b = form.cleaned_data['telefono_b']
        ip_switch_b = form.cleaned_data['ip_switch_b']

        return f"""
REMARK:
Extremo A: {nro_incidente} / Preventivo / {incident.nombre_anillo} / {ciudad} / {incident.ip}
Extremo B: {nro_incidente} / Preventivo / {incident.nombre_anillo} / {ciudad} / {ip_switch_b}

S. Avanzado: 
    Conclusión al ejecutar lista de chequeo: No aplica
	Numeral donde se evidencia falla en la lista de chequeo: No aplica
    Diagnóstico realizado: Se presenta apertura simple en el anillo {incident.nombre_anillo} entre los clientes {incident.nombre_cliente} por la GE {giga_caida_A} contra {cliente_extremo_B}. por la GE {giga_caida_B}

CIUDAD: {ciudad}
ANILLO: {incident.nombre_anillo}

CLIENTE EXTREMO A: {incident.nombre_cliente}
IDENTIFICADOR: {incident.id_servicio}
GE CAIDA: {giga_caida_A}
DIRECCIÓN: {incident.direccion_servicio}
CONTACTO: {incident.nombre_contacto}
TELÉFONO: {incident.numero_contacto}
IP SWITCH: {incident.ip}
DISPONIBILIDAD: L-V 8:00 - 16:00

CLIENTE EXTREMO B: {cliente_extremo_B}
IDENTIFICADOR: {identificador_extremo_B}
GE CAIDA: {giga_caida_B}
DIRECCIÓN: {direccion_b}
CONTACTO: {contacto_b}
TELÉFONO: {telefono_b}
IP SWITCH: {ip_switch_b}
DISPONIBILIDAD: L-V 8:00 - 16:00


S3GU1M13NT0_3V3NT0S:d1agnostico
"""

class EquipoCaido(BaseIncidentView):
    template_name = 'incidents/equipo_caido.html'
    form_class = forms.EquipoCaidoForm

    def generar_texto(self, form, incident):
        fecha_caida = form.cleaned_data['fecha_caida']
        nro_incidente = form.cleaned_data['nro_incidente']
        ciudad = form.cleaned_data['ciudad']
        ip_sw_vecinoA = form.cleaned_data['ip_sw_vecinoA']
        ip_sw_vecinoB = form.cleaned_data['ip_sw_vecinoB']
        return f"""
REMARK:
Equipo Caído: 
{nro_incidente} / Switch Apagado / {incident.nombre_anillo} / {ciudad} / {incident.ip}
Vecino A: 
{nro_incidente} / Apertura sin afectación / {incident.nombre_anillo} / {ciudad} / {ip_sw_vecinoA}
Vecino B: 
{nro_incidente} / Apertura sin afectación / {incident.nombre_anillo} / {ciudad} / {ip_sw_vecinoB}  
-------------------------------------------------------------------------------------------------------------------------------------------------------------
    ID prueba: 
    Conclusión al ejecutar lista de chequeo: No aplica
    Diagnóstico realizado: Servicio activo en Fénix, se evidencia alarma de equipo apagado para el cliente {incident.nombre_cliente} en el anillo {incident.nombre_anillo}. Se ingresa a NCE y se evidencia switch de fibra óptica offline por SecureCRT. Se validan los vecinos presentan apertura por una de las gigas. 
    Falla eléctrica S/N : Sin definir

NOTA: El equipo de fibra óptica se evidencia apagado desde {fecha_caida}.


S3GU1M13NT0_3V3NT0S:d1agnostico
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
       
class NotaLlamada(BaseIncidentView):
    template_name = 'incidents/llamada_saliente.html'
    form_class = forms.NotaLlamadaForm
    
    def generar_texto(self, form, incident):
        id_llamada1 = form.cleaned_data['id_llamada1']
        id_llamada2 = form.cleaned_data['id_llamada2']
        id_llamada3 = form.cleaned_data['id_llamada3']
        observaciones = form.cleaned_data['observaciones']
        texto = f"""De acuerdo con la comunicación establecida Nombre: {incident.nombre_contacto} Tel: {incident.numero_contacto} hemos registrado su llamada con el siguiente avance: 

{observaciones}

Seguiremos gestionando su caso en pro de una solución oportuna.

ID llamada: {id_llamada1} """
        if id_llamada2:
            texto = texto + f"""/ {id_llamada2} """
        if id_llamada3:
            texto = texto + f"""/ {id_llamada3}"""

        texto = texto + f"""


S3GU1M13NT0_3V3NT0S:llamadaalcliente"""
        return texto
    
class AperturaContraCentral(BaseIncidentView):
    template_name = 'incidents/apertura_contra_central.html'
    form_class = forms.AperturaContraCentralForm

    def generar_texto(self, form, incident):
        nro_incidente = form.cleaned_data['nro_incidente']
        ciudad = form.cleaned_data['ciudad']
        giga_caida_A = form.cleaned_data['giga_caida_A']
        nombre_central = form.cleaned_data['nombre_central']
        giga_central = form.cleaned_data['giga_central']
        ip_sw_central = form.cleaned_data['ip_sw_central']

        return f"""
REMARK:
{nro_incidente} / Preventivo / {incident.nombre_anillo} / {ciudad} / {incident.ip}

S. Avanzado: 
    Conclusión al ejecutar lista de chequeo: No aplica
	Numeral donde se evidencia falla en la lista de chequeo: No aplica
    Diagnóstico realizado: Se presenta apertura simple en el anillo {incident.nombre_anillo} entre los clientes {incident.nombre_cliente} por la GE {giga_caida_A} contra {nombre_central}. por la GE {giga_central}

CIUDAD: {ciudad}
ANILLO: {incident.nombre_anillo}

CLIENTE EXTREMO A: {incident.nombre_cliente}
IDENTIFICADOR: {incident.id_servicio}
GE CAIDA: {giga_caida_A}
DIRECCIÓN: {incident.direccion_servicio}
CONTACTO: {incident.nombre_contacto}
TELÉFONO: {incident.numero_contacto}
IP SWITCH: {incident.ip}
DISPONIBILIDAD: L-V 8:00 - 16:00

CLIENTE EXTREMO B: {nombre_central}
GE B: {giga_central}
IP SWITCH: {ip_sw_central}
DISPONIBILIDAD: L-V 8:00 - 16:00


S3GU1M13NT0_3V3NT0S:d1agnostico
"""
    
class DiagnosticoPotencias(BaseIncidentView):
    template_name = 'incidents/alarma_potencias.html'
    form_class =forms.AlarmaPotencias

    def generar_texto(self, form, incident):
        ciudad = form.cleaned_data['ciudad']
        giga_extremo_A = form.cleaned_data['giga_extremo_A']
        parametros = form.cleaned_data['parametros']
        cliente_extremo_B = form.cleaned_data['cliente_extremo_B']
        giga_extremo_B = form.cleaned_data['giga_extremo_B']

        return f"""
    S. Avanzado: 
        Conclusión al ejecutar lista de chequeo: NA
        Numeral donde se evidencia falla en la lista de chequeo: NA
        Diagnóstico realizado: Se presenta alarma de potencia en el anillo {incident.nombre_anillo} ({ciudad}) entre los clientes {incident.nombre_cliente} por el puerto Giga{giga_extremo_A} RxPower(dBm) {parametros} contra {cliente_extremo_B} por el puerto Giga{giga_extremo_B} 

        Falla eléctrica S/N: NA


    S3GU1M13NT0_3V3NT0S:d1agnostico
    """