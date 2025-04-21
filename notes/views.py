from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from .models import Note
from .forms import caido_form

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
  
class nota_diagnostico(BaseIncidentView):
  template_name = 'notes/nota_diagnostico.html'
  form_class = caido_form

  def generar_texto(self, form):
    # Aquí puedes implementar la lógica para generar el texto de diagnóstico
    # Por ejemplo, puedes obtener los datos del formulario y generar un texto
    # basado en ellos.
    # Esto es solo un ejemplo, debes adaptarlo a tus necesidades.
    nombre_anillo = form.cleaned_data['nombre_anillo']
    nombre_cliente = form.cleaned_data['nombre_cliente']
    estado = form.cleaned_data['estado']

    estado = "Activo" if estado else "Retirado"
    return f"""
    ID prueba: N/A
    Conclusión al ejecutar lista de chequeo: N/A
    Diagnóstico realizado: Servicio {estado} en Fénix, se evidencia alarma de equipo apagado para el cliente {nombre_cliente} en el anillo {nombre_anillo}. Se ingresa a NCE y se evidencia switch de fibra óptica offline por SecureCRT. Se validan los vecinos presentan apertura por una de las gigas. 
    Falla eléctrica S/N: N/A
    

    S3GU1M13NT0_3V3NT0S:d1agnostico
    """

