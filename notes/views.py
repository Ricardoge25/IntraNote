from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from .models import Note
from . import forms

# Create your views here.
class ListNoteView(ListView):
  model = Note

class BaseIncidentView(View):
  template_name = None
  form_class = None

  def get(self, request):
    form = self.form_class()
    return render(request, self.template_name, {
      'form': form,
      'texto': None
    })  

  def post(self, request):
    form = self.form_class(request.POST)
    texto = None
    if form.is_valid():
      texto = self.generar_texto(form)
    return render(request, self.template_name, {
      'form': form,
      'texto': texto
    })

  def generar_texto(self, form):
    # Este método debe ser implementado en las subclases
    raise NotImplementedError("La subclase debe implemetar este método")
  
class nota_ap_doble(BaseIncidentView):
  template_name = 'notes/nota_ap_doble.html'
  form_class = forms.ap_doble_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    estado = form.cleaned_data['estado']

    estado = "Retirado" if estado else "Activo"
    return f"""
    ID prueba: N/A
    Conclusión al ejecutar lista de chequeo: N/A
    Diagnóstico realizado: Servicio {estado} en Fénix, se evidencia alarma de equipo apagado para el cliente {nombre_cliente} en el anillo {nombre_anillo}. Se ingresa a NCE y se evidencia switch de fibra óptica offline por SecureCRT. Se validan los vecinos presentan apertura por una de las gigas. 
    Falla eléctrica S/N: N/A
    

    S3GU1M13NT0_3V3NT0S:d1agnostico
    """

class nota_ap_simple_clientes(BaseIncidentView):
  template_name = 'notes/nota_ap_simple_clientes.html'
  form_class = forms.ap_simple_clientes_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente_A = form.cleaned_data['nombre_cliente_A']
    nombre_cliente_B = form.cleaned_data['nombre_cliente_B']
    id_servicio_A = form.cleaned_data['id_servicio_A']
    id_servicio_B = form.cleaned_data['id_servicio_B']
    ip_cliente_A = form.cleaned_data['ip_cliente_A']
    ip_cliente_B = form.cleaned_data['ip_cliente_B']
    giga_extremo_A = form.cleaned_data['giga_extremo_A']
    giga_extremo_B = form.cleaned_data['giga_extremo_B']
    contacto_cliente_A = form.cleaned_data['contacto_cliente_A']
    contacto_cliente_B = form.cleaned_data['contacto_cliente_B']
    numero_cliente_A = form.cleaned_data['numero_cliente_A']
    numero_cliente_B = form.cleaned_data['numero_cliente_B']
    correo_cliente_A = form.cleaned_data['correo_cliente_A']
    correo_cliente_B = form.cleaned_data['correo_cliente_B']
    direccion_cliente_A = form.cleaned_data['direccion_cliente_A']
    direccion_cliente_B = form.cleaned_data['direccion_cliente_B']

    return f"""
    ID prueba: N/A
    Conclusión al ejecutar lista de chequeo: N/A
    Diagnóstico realizado: Se presenta apertura simple en el anillo {nombre_anillo} entre los clientes {nombre_cliente_A} por la GE {giga_extremo_A} contra {nombre_cliente_B}. por la GE {giga_extremo_B}

CIUDAD: {ciudad}
ANILLO: {nombre_anillo}

CLIENTE EXTREMO A: {nombre_cliente_A}
IDENTIFICADOR: {id_servicio_A}
GE CAIDA: {giga_extremo_A}
DIRECCIÓN: {direccion_cliente_A}
CONTACTO: {contacto_cliente_A}
TELÉFONO: {numero_cliente_A}
CORREO: {correo_cliente_A}
IP SWITCH: {ip_cliente_A}
DISPONIBILIDAD: L-V 8:00 - 16:00

CLIENTE EXTREMO B: {nombre_cliente_B}
IDENTIFICADOR: {id_servicio_B}
GE CAIDA: {giga_extremo_B}
DIRECCIÓN: {direccion_cliente_B}
CONTACTO: {contacto_cliente_B}
TELÉFONO: {numero_cliente_B}
CORREO: {correo_cliente_B}
IP SWITCH: {ip_cliente_B}
DISPONIBILIDAD: L-V 8:00 - 16:00

S3GU1M13NT0_3V3NT0S:d1agnostico"""
  
class nota_ap_simple_central(BaseIncidentView):
  template_name = 'notes/nota_ap_simple_central.html'
  form_class = forms.ap_simple_central_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    id_servicio = form.cleaned_data['id_servicio']
    ip_cliente = form.cleaned_data['ip_cliente']
    giga_extremo = form.cleaned_data['giga_extremo']
    contacto_cliente = form.cleaned_data['contacto_cliente']
    numero_cliente = form.cleaned_data['numero_cliente']
    correo_cliente = form.cleaned_data['correo_cliente']
    direccion_cliente = form.cleaned_data['direccion_cliente']
    nombre_central = form.cleaned_data['nombre_central']
    ip_central = form.cleaned_data['ip_central']
    giga_central = form.cleaned_data['giga_central']

    return f"""
    ID prueba: N/A
    Conclusión al ejecutar lista de chequeo: N/A
	Diagnóstico realizado:Se presenta apertura simple en el anillo {nombre_anillo} entre los clientes {nombre_cliente} por la GE{giga_extremo} contra {nombre_central} por la GE{giga_central}.

CIUDAD: {ciudad}
ANILLO: {nombre_anillo} 

CLIENTE EXTREMO A: {nombre_cliente}
IDENTIFICADOR: {id_servicio}
GE A: {giga_extremo}
DIRECCIÓN: {direccion_cliente}
CONTACTO: {contacto_cliente}
TELÉFONO: {numero_cliente}
CORREO: {correo_cliente}
IP SWITCH: {ip_cliente}
DISPONIBILIDAD: L-V 8:00 - 16:00

CLIENTE EXTREMO B: {nombre_central}
GE B: {giga_central}
IP SWITCH: {ip_central}
DISPONIBILIDAD: L-V 8:00 - 16:00

S3GU1M13NT0_3V3NT0S:d1agnostico"""
  
class nota_potencias_alarmadas(BaseIncidentView):
  template_name = 'notes/nota_potencias_alarmadas.html'
  form_class = forms.potencias_alarmadas_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente_A = form.cleaned_data['nombre_cliente_A']
    nombre_cliente_B = form.cleaned_data['nombre_cliente_B']
    giga_extremo_A = form.cleaned_data['giga_extremo_A']
    giga_extremo_B = form.cleaned_data['giga_extremo_B']
    valor_potencia = form.cleaned_data['valor_potencia']

    return f"""
    ID prueba: N/A
    Conclusión al ejecutar lista de chequeo: N/A
	Diagnóstico realizado: Se presenta alarma de potencia en el anillo {nombre_anillo} ({ciudad}) entre los clientes {nombre_cliente_A} por el puerto Giga{giga_extremo_A} RxPower(dBm) {valor_potencia} contra {nombre_cliente_B} por el puerto Giga{giga_extremo_B}

	Falla eléctrica S/N: NA


S3GU1M13NT0_3V3NT0S:d1agnostico"""