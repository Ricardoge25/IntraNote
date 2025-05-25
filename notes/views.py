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
  
class nota_llamada(BaseIncidentView):
  template_name = 'notes/nota_llamada.html'
  form_class = forms.llamada_form

  def generar_texto(self, form):
    nombre_contacto = form.cleaned_data['nombre_contacto']
    numero_contacto = form.cleaned_data['numero_contacto']
    id_llamada_1 = form.cleaned_data['id_llamada_1']
    id_llamada_2 = form.cleaned_data['id_llamada_2']
    id_llamada_3 = form.cleaned_data['id_llamada_3']
    avances = form.cleaned_data['avances']

    texto = f"""
De acuerdo con la comunicación establecida Nombre: {nombre_contacto} Teléfono: {numero_contacto} hemos registrado su llamada con el siguiente avance: 

{avances}

Seguiremos gestionando su caso en pro de una solución oportuna.

ID llamada: {id_llamada_1} """
    
    if id_llamada_2:
        texto = texto + f"""/ {id_llamada_2} """
    if id_llamada_3:
        texto = texto + f"""/ {id_llamada_3}"""

    texto = texto + f"""

    
S3GU1M13NT0_3V3NT0S:llamadaalcliente
"""
    
    return texto
  
class nota_correo_saliente(BaseIncidentView):
  template_name = 'notes/nota_correo_saliente.html'

  def get(self, request):
    texto = """
Se envía respuesta a los interesados en el correo adjunto.


S3GU1M13NT0_3V3NT0S:correoalcliente
"""
    return render(request, self.template_name, {
      'texto': texto
    })
  
class nota_correo_entrante(BaseIncidentView):
  template_name = 'notes/nota_correo_entrante.html'

  def get(self, request):
    texto = """
Se brinda respuesta a la solicitud del cliente en el correo adjunto. 


S3GU1M13NT0_3V3NT0S:correodelcliente
"""
    return render(request, self.template_name, {
      'texto': texto
    })

class nota_escalamiento(BaseIncidentView):
  template_name = 'notes/nota_escalamiento.html'
  form_class = forms.escalamiento_form

  def generar_texto(self, form):
    horario = form.cleaned_data['horario']
    nombre_contacto = form.cleaned_data['nombre_contacto']
    numero_contacto = form.cleaned_data['numero_contacto']
    acceso = form.cleaned_data['acceso']
    direccion = form.cleaned_data['direccion']
    permisos = form.cleaned_data['permisos']
    parafiscales = form.cleaned_data['parafiscales']
    cursos = form.cleaned_data['cursos']
    equipo = form.cleaned_data['equipo']
    referencia_equipo = form.cleaned_data['referencia_equipo']
    observaciones = form.cleaned_data['observaciones']

    permisos_texto = "No requiere permisos" if not permisos else "Requiere permisos"
    parafiscales_texto = "No requiere parafiscales" if not parafiscales else "Requiere parafiscales"
    cursos_texto = "No requiere cursos" if not cursos else "Requiere cursos"
    equipo_texto = "No requiere equipo" if not equipo else "Requiere equipo"
    acceso_texto = "No tiene acceso" if not acceso else "Tiene acceso"

    texto = f"""
Horario: {horario}
Nombre Contacto en Sitio: {nombre_contacto}
Teléfonos Contacto en Sitio: {numero_contacto}
Contacto en sitio, tiene acceso a los CPE: {acceso_texto}
Dirección: {direccion}
Permisos de ingreso: {permisos_texto}
Parafiscales: {parafiscales_texto}
Requiere Curso: {cursos_texto}
Requiere llevar equipo: {equipo_texto}
Tipo de equipo (Referencia) y cantidad: {referencia_equipo}
Observaciones detalladas: {observaciones}
"""

    return texto

class nota_reprueba(BaseIncidentView):
  template_name = 'notes/nota_reprueba.html'
  form_class = forms.reprueba_form

  def generar_texto(self, form):
    prueba_realizada = form.cleaned_data['prueba_realizada']
    herramienta = form.cleaned_data['herramienta']
    resultado = form.cleaned_data['resultado']

    texto = f"""
Prueba realizada: {prueba_realizada}
Herramienta utilizada: {herramienta}
Resultado obtenido: {resultado}


S3GU1M13NT0_3V3NT0S:p3s3rv1c10
"""
    return texto
  
class nota_resolucion(BaseIncidentView):
  template_name = 'notes/nota_resolucion.html'
  form_class = forms.resolucion_form

  def generar_texto(self, form):
    causa = form.cleaned_data['causa']
    solucion = form.cleaned_data['solucion']

    texto = f"""
La causa fue: {causa}
La solución fue: {solucion}
"""
    return texto
  
class nota_especialista(BaseIncidentView):
  template_name = 'notes/nota_especialista.html'
  form_class = forms.especialista_form

  def generar_texto(self, form):
    especialista = form.cleaned_data['especialista']
    canal = form.cleaned_data['canal']
    rol = form.cleaned_data['rol']
    avance = form.cleaned_data['avance']
    apoyo = form.cleaned_data['apoyo']

    texto = f"""
Especialista a quien escribe: {especialista}
Canal de comunicación: {canal}
Rol del especialista: {rol}
Avance solicitado del especialista: {avance}
Apoyo dado: {apoyo}


S3GU1M13NT0_3V3NT0S:c0mun1c4c10nalespecialista
"""
    return texto
  
class tiquete_ap_doble_uno(BaseIncidentView):
  template_name = 'notes/tiquete_ap_doble_uno.html'
  form_class = forms.tiquete_ap_doble_uno_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    ip_cliente = form.cleaned_data['ip_cliente']
    contacto_cliente = form.cleaned_data['contacto_cliente']
    numero_cliente = form.cleaned_data['numero_cliente']
    correo_cliente = form.cleaned_data['correo_cliente']
    direccion_cliente = form.cleaned_data['direccion_cliente']
    disponibilidad = form.cleaned_data['disponibilidad']
    descartes = form.cleaned_data['descartes']

    resumen = f"""
Se presenta apertura doble en el anillo {nombre_anillo}({ciudad}) afectando comunicaciones del cliente {nombre_cliente}"""
    
    descripcion = f"""{resumen} 
ANILLO: {nombre_anillo}
IP SWITCH: {ip_cliente}
CIUDAD: {ciudad}
NOMBRE DEL CLIENTE: {nombre_cliente}
CONTACTO CLIENTE: {contacto_cliente}
DIRECCIÓN CLIENTE: {direccion_cliente}
TELÉFONO CLIENTE: {numero_cliente}
CORREO CLIENTE: {correo_cliente}
DISPONIBILIAD: {disponibilidad}
DESCARTES REALIZADOS: {descartes}

NOTA: Se debe garantizar que al cerrar el anillo los niveles de potencia queden entre los rangos establecidos
"""
    return resumen, descripcion
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)

    resumen = None
    descripcion = None

    if form.is_valid():
        resumen_text, descripcion_text = self.generar_texto(form)
        action = request.POST.get('action')  
        if action == 'resumen':
            resumen = resumen_text
        elif action == 'descripcion':
            descripcion = descripcion_text

    return render(request, self.template_name, {
        'form': form,
        'resumen': resumen or request.POST.get('resumen'),
        'descripcion': descripcion or request.POST.get('descripcion'),
    })

class tiquete_ap_doble_dos(BaseIncidentView):
  template_name = 'notes/tiquete_ap_doble_dos.html'
  form_class = forms.tiquete_ap_doble_dos_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente_A = form.cleaned_data['nombre_cliente_A']
    ip_cliente_A = form.cleaned_data['ip_cliente_A']
    contacto_cliente_A = form.cleaned_data['contacto_cliente_A']
    numero_cliente_A = form.cleaned_data['numero_cliente_A']
    correo_cliente_A = form.cleaned_data['correo_cliente_A']
    direccion_cliente_A = form.cleaned_data['direccion_cliente_A']
    disponibilidad_A = form.cleaned_data['disponibilidad_A']
    descartes_A = form.cleaned_data['descartes_A']
    nombre_cliente_B = form.cleaned_data['nombre_cliente_B']
    ip_cliente_B = form.cleaned_data['ip_cliente_B']
    contacto_cliente_B = form.cleaned_data['contacto_cliente_B']
    numero_cliente_B = form.cleaned_data['numero_cliente_B']
    correo_cliente_B = form.cleaned_data['correo_cliente_B']
    direccion_cliente_B = form.cleaned_data['direccion_cliente_B']
    disponibilidad_B = form.cleaned_data['disponibilidad_B']
    descartes_B = form.cleaned_data['descartes_B']

    resumen = f"""
Se presenta apertura doble en el anillo {nombre_anillo}({ciudad}) entre los clientes {nombre_cliente_A} y {nombre_cliente_B}
"""
    descripcion = f"""{resumen}
ANILLO: {nombre_anillo}
CIUDAD: {ciudad}
NOMBRE CLIENTE CAÍDO EXTREMO A: {nombre_cliente_A}
IP SWITCH CLIENTE EXTREMO A: {ip_cliente_A}
CONTACTO CLIENTE CAÍDO EXTREMO A: {contacto_cliente_A}
CORREO CLIENTE CAÍDO EXTREMO A: {correo_cliente_A}
DIRECCIÓN CLIENTE CAÍDO EXTREMO A: {direccion_cliente_A}
TELÉFONO CLIENTE CAÍDO EXTREMO A: {numero_cliente_A}
DISPONIBILIAD HORARIA CLIENTE EXTREMO A: {disponibilidad_A}
DESCARTES REALIZADOS: {descartes_A}

NOMBRE CLIENTE EXTREMO B: {nombre_cliente_B}
IP SWITCH CLIENTE EXTREMO B: {ip_cliente_B}
CONTACTO CLIENTE CAÍDO EXTREMO B: {contacto_cliente_B}
CORREO CLIENTE CAÍDO EXTREMO B: {correo_cliente_B}
DIRECCIÓN CLIENTE CAÍDO EXTREMO B: {direccion_cliente_B}
TELÉFONO CLIENTE CAÍDO EXTREMO B: {numero_cliente_B}
DISPONIBILIAD HORARIA CLIENTE EXTREMO B: {disponibilidad_B}
DESCARTES REALIZADOS: {descartes_B}
"""
    return resumen, descripcion
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)

    resumen = None
    descripcion = None

    if form.is_valid():
        resumen_text, descripcion_text = self.generar_texto(form)
        action = request.POST.get('action')  
        if action == 'resumen':
            resumen = resumen_text
        elif action == 'descripcion':
            descripcion = descripcion_text

    return render(request, self.template_name, {
        'form': form,
        'resumen': resumen or request.POST.get('resumen'),
        'descripcion': descripcion or request.POST.get('descripcion'),
    })

class tiquete_retiro_empalme(BaseIncidentView):
  template_name = 'notes/tiquete_retiro_empalme.html'
  form_class = forms.tiquete_retiro_empalme_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    ip = form.cleaned_data['ip']
    identificador = form.cleaned_data['identificador']
    contacto_cliente = form.cleaned_data['contacto_cliente']
    numero_cliente = form.cleaned_data['numero_cliente']
    correo_cliente = form.cleaned_data['correo_cliente']
    direccion_cliente = form.cleaned_data['direccion_cliente']

    resumen = f"""
Se requiere realizar retiro desde el empalme del cliente "{nombre_cliente}" ubicado en el anillo "{nombre_anillo}", el cual se encuentra apagado por más de 48 horas *MONITOREO PROACTIVO*
"""
    descripcion = f"""{resumen}
ANILLO: {nombre_anillo}
IP SWITCH: {ip}
CIUDAD: {ciudad}
IDENTIFICADOR: {identificador}
NOMBRE CLIENTE: {nombre_cliente}
CONTACTO CLIENTE: {contacto_cliente}
TELÉFONO CLIENTE: {numero_cliente}
CORREO CLIENTE: {correo_cliente}
DIRECCIÓN CLIENTE: {direccion_cliente}
DISPONIBILIDAD CLIENTE: 24/7
"""    
    return resumen, descripcion
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    resumen = None
    descripcion = None
    if form.is_valid():
        resumen_text, descripcion_text = self.generar_texto(form)
        action = request.POST.get('action')  
        if action == 'resumen':
            resumen = resumen_text
        elif action == 'descripcion':
            descripcion = descripcion_text
    return render(request, self.template_name, {
      'form': form,
      'resumen': resumen or request.POST.get('resumen'),
      'descripcion': descripcion or request.POST.get('descripcion'),
    })

class tiquete_reingreso_empalme(BaseIncidentView):
  template_name = 'notes/tiquete_reingreso_empalme.html'
  form_class = forms.tiquete_reingreso_empalme_form

  def generar_texto(self, form):
    nombre_anillo = form.cleaned_data['nombre_anillo']
    ciudad = form.cleaned_data['ciudad']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    ip = form.cleaned_data['ip']
    identificador = form.cleaned_data['identificador']
    contacto_cliente = form.cleaned_data['contacto_cliente']
    numero_cliente = form.cleaned_data['numero_cliente']
    correo_cliente = form.cleaned_data['correo_cliente']
    direccion_cliente = form.cleaned_data['direccion_cliente']
    disponibilidad = form.cleaned_data['disponibilidad']
    descartes = form.cleaned_data['descartes']

    resumen = f"""
Se requiere realizar el reingreso al anillo {nombre_anillo}({ciudad}) desde el empalme de derivación al cliente
"""
    descripcion = f"""{resumen}
ANILLO: {nombre_anillo}
IP SWITCH: {ip}
CIUDAD: {ciudad}
IDENTIFICADOR: {identificador}
NOMBRE DEL CLIENTE: {nombre_cliente}
CONTACTO CLIENTE: {contacto_cliente}
TELÉFONO CLIENTE: {numero_cliente}
DIRECCIÓN: {direccion_cliente}
DISPONIBILIAD HORARIA: {disponibilidad}
DESCARTES REALIZADOS: {descartes}

NOTA: Se debe garantizar que al cerrar el anillo los niveles de potencia queden entre los rangos establecidos
"""
    return resumen, descripcion
  
  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    resumen = None
    descripcion = None
    if form.is_valid():
        resumen_text, descripcion_text = self.generar_texto(form)
        action = request.POST.get('action')  
        if action == 'resumen':
            resumen = resumen_text
        elif action == 'descripcion':
            descripcion = descripcion_text
    return render(request, self.template_name, {
      'form': form,
      'resumen': resumen or request.POST.get('resumen'),
      'descripcion': descripcion or request.POST.get('descripcion'),
    })
  
  