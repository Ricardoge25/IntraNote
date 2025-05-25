from django import forms 

class ap_doble_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente',) 
  estado = forms.BooleanField(
    label='¿Retirado?',
    required=False)
  
class ap_simple_clientes_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente_A = forms.CharField(
    max_length=100, 
    label='Nombre Cliente A')
  nombre_cliente_B = forms.CharField(
    max_length=100, 
    label='Nombre Cliente B')
  id_servicio_A = forms.CharField(
    max_length=30,
    label='ID Servicio A')
  id_servicio_B = forms.CharField(
    max_length=30,
    label='ID Servicio B')
  ip_cliente_A = forms.CharField(
    max_length=30, 
    label='IP Cliente A')
  ip_cliente_B = forms.CharField(
    max_length=30, 
    label='IP Cliente B')
  giga_extremo_A = forms.CharField(
    max_length=30, 
    label='Giga Extremo A')
  giga_extremo_B = forms.CharField(
    max_length=30, 
    label='Giga Extremo B')
  contacto_cliente_A = forms.CharField(
    max_length=100, 
    label='Contacto Cliente A')
  contacto_cliente_B = forms.CharField(
    max_length=100, 
    label='Contacto Cliente B')
  numero_cliente_A = forms.CharField(
    max_length=30, 
    label='Número Cliente A')
  numero_cliente_B = forms.CharField(
    max_length=30, 
    label='Número Cliente B')
  correo_cliente_A = forms.EmailField(
    max_length=100, 
    label='Correo Cliente A')
  correo_cliente_B = forms.EmailField(
    max_length=100, 
    label='Correo Cliente B')
  direccion_cliente_A = forms.CharField(
    max_length=100, 
    label='Dirección Cliente A')
  direccion_cliente_B = forms.CharField(
    max_length=100, 
    label='Dirección Cliente B')
  
class ap_simple_central_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente')
  id_servicio = forms.CharField(
    max_length=30,
    label='ID Servicio')
  ip_cliente = forms.CharField(
    max_length=30, 
    label='IP Cliente')
  giga_extremo = forms.CharField(
    max_length=30, 
    label='Giga Extremo')
  contacto_cliente = forms.CharField(
    max_length=100, 
    label='Contacto Cliente')
  numero_cliente = forms.CharField(
    max_length=30, 
    label='Número Cliente')
  correo_cliente = forms.EmailField(
    max_length=100, 
    label='Correo Cliente')
  direccion_cliente = forms.CharField(
    max_length=100, 
    label='Dirección Cliente')
  nombre_central = forms.CharField(
    max_length=100, 
    label='Nombre Central')
  ip_central = forms.CharField(
    max_length=30, 
    label='IP Central')
  giga_central = forms.CharField(
    max_length=30, 
    label='Giga Central')
  
class potencias_alarmadas_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente_A = forms.CharField(
    max_length=100, 
    label='Nombre Cliente A')
  giga_extremo_A = forms.CharField(
    max_length=30, 
    label='Giga Extremo A')
  nombre_cliente_B = forms.CharField(
    max_length=100, 
    label='Nombre Cliente B')
  giga_extremo_B = forms.CharField(
    max_length=30, 
    label='Giga Extremo B')
  valor_potencia = forms.CharField(
    max_length=30, 
    label='Potencia (Rx)')
  
class llamada_form(forms.Form):
  nombre_contacto = forms.CharField(
    max_length=30, 
    label='Nombre Contacto')
  numero_contacto = forms.CharField(
    max_length=30, 
    label='Número Contacto')
  id_llamada_1 = forms.CharField(
    max_length=30, 
    label='ID Llamada')
  id_llamada_2 = forms.CharField(
    max_length=30, 
    label='ID Llamada',
    required=False)
  id_llamada_3 = forms.CharField(
    max_length=30, 
    label='ID Llamada',
    required=False)
  avances = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 5
    }), 
    label="Avances Realizados",)

class escalamiento_form(forms.Form):
  horario = forms.CharField(
    max_length=30, 
    label='Horario')
  nombre_contacto = forms.CharField(
    max_length=30, 
    label='Nombre Contacto')
  numero_contacto = forms.CharField(
    max_length=30, 
    label='Número Contacto')
  direccion = forms.CharField(
    max_length=100, 
    label='Dirección')
  acceso = forms.BooleanField(
    label='¿Tiene acceso?',
    required=False)
  permisos = forms.BooleanField(
    label='¿Requiere permisos?',
    required=False)
  parafiscales = forms.BooleanField(
    label='¿Requiere parafiscales?',
    required=False)
  cursos = forms.BooleanField(
    label='¿Requiere cursos?',
    required=False)
  equipo = forms.BooleanField(
    label='¿Requiere equipo?',
    required=False)
  referencia_equipo = forms.CharField(
    max_length=100, 
    label='Referencia Equipo')
  observaciones = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 5
    }), 
    label="Observaciones",
    required=False)
  
class reprueba_form(forms.Form):
  prueba_realizada = forms.CharField(
    max_length=50, 
    label='Prueba Realizada')
  herramienta = forms.CharField(
    max_length=50, 
    label='Herramienta Utilizada')
  resultado = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 5
    }), 
    label="Resultado Obtenido",
    required=False)

class resolucion_form(forms.Form):
  causa = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 3
    }), 
    label="La causa fue:")
  solucion = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 4
    }), 
    label="La solución fue:")

class especialista_form(forms.Form):
  especialista = forms.CharField(
    max_length=30, 
    label='Especialista a que escribe:')
  canal = forms.CharField(
    max_length=30, 
    label='Canal de comunicación:')
  rol = forms.CharField(
    max_length=30, 
    label='Rol del especialista:')
  avance = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 2
    }), 
    label="Avance del especialista:")
  apoyo = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 2
    }),
    label="Apoyo dado:")
  
class tiquete_ap_doble_uno_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente A')
  ip_cliente = forms.CharField(
    max_length=30, 
    label='IP Cliente A')
  contacto_cliente = forms.CharField(
    max_length=100, 
    label='Contacto Cliente A')
  numero_cliente = forms.CharField(
    max_length=30, 
    label='Número Cliente A')
  correo_cliente = forms.EmailField(
    max_length=100, 
    label='Correo Cliente A')
  direccion_cliente = forms.CharField(
    max_length=100, 
    label='Dirección Cliente A')
  disponibilidad = forms.CharField(
    max_length=30, 
    label='Disponibilidad A')
  descartes = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 3
    }), 
    label="Descartes Realizados")

class tiquete_ap_doble_dos_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente_A = forms.CharField(
    max_length=100, 
    label='Nombre Cliente A')
  ip_cliente_A = forms.CharField(
    max_length=30, 
    label='IP Cliente A')
  contacto_cliente_A = forms.CharField(
    max_length=100, 
    label='Contacto Cliente A')
  numero_cliente_A = forms.CharField(
    max_length=30, 
    label='Número Cliente A')
  correo_cliente_A = forms.EmailField(
    max_length=100, 
    label='Correo Cliente A')
  direccion_cliente_A = forms.CharField(
    max_length=100, 
    label='Dirección Cliente A')
  disponibilidad_A = forms.CharField(
    max_length=30, 
    label='Disponibilidad A')
  descartes_A = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 3
    }), 
    label="Descartes realizados A")
  nombre_cliente_B = forms.CharField(
    max_length=100, 
    label='Nombre Cliente B')
  ip_cliente_B = forms.CharField(
    max_length=30, 
    label='IP Cliente B')
  contacto_cliente_B = forms.CharField(
    max_length=100, 
    label='Contacto Cliente B')
  numero_cliente_B = forms.CharField(
    max_length=30, 
    label='Número Cliente B')
  correo_cliente_B = forms.EmailField(
    max_length=100, 
    label='Correo Cliente B')
  direccion_cliente_B = forms.CharField(
    max_length=100, 
    label='Dirección Cliente B')
  disponibilidad_B = forms.CharField(
    max_length=30, 
    label='Disponibilidad B')
  descartes_B = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 3
    }), 
    label="Descartes realizados B")
  
class tiquete_retiro_empalme_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente')
  ip = forms.CharField(
    max_length=30, 
    label='IP Cliente')
  identificador = forms.CharField(
    max_length=30, 
    label='Identificador')
  contacto_cliente = forms.CharField(
    max_length=100, 
    label='Contacto Cliente')
  numero_cliente = forms.CharField(
    max_length=30, 
    label='Número Cliente')
  correo_cliente = forms.EmailField(
    max_length=100, 
    label='Correo Cliente')
  direccion_cliente = forms.CharField(
    max_length=100, 
    label='Dirección Cliente')

class tiquete_reingreso_empalme_form(forms.Form):
  nombre_anillo = forms.CharField(
    max_length=30,
    label='Nombre Anillo')
  ciudad = forms.CharField(
    max_length=30,
    label='Ciudad')
  nombre_cliente = forms.CharField(
    max_length=100, 
    label='Nombre Cliente')
  ip = forms.CharField(
    max_length=30, 
    label='IP Cliente')
  identificador = forms.CharField(
    max_length=30, 
    label='Identificador')
  contacto_cliente = forms.CharField(
    max_length=100, 
    label='Contacto Cliente')
  numero_cliente = forms.CharField(
    max_length=30, 
    label='Número Cliente')
  correo_cliente = forms.EmailField(
    max_length=100, 
    label='Correo Cliente')
  direccion_cliente = forms.CharField(
    max_length=100, 
    label='Dirección Cliente')
  disponibilidad = forms.CharField(
    max_length=30, 
    label='Disponibilidad')
  descartes = forms.CharField(
    widget=forms.Textarea(attrs=
      {'class': 'form-control',
      'rows': 3
    }), 
    label="Descartes Realizados")