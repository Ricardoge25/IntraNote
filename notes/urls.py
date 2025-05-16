from django.urls import path
from . import views

notes_patterns = ([
    path('', views.ListNoteView.as_view(), name='notes'),
    path('nota_ap_doble/',  views.nota_ap_doble.as_view(), name='nota_ap_doble'),
    path('nota_ap_simple_clientes/',  views.nota_ap_simple_clientes.as_view(), name='nota_ap_simple_clientes'),
    path('nota_ap_simple_central/', views.nota_ap_simple_central.as_view(), name='nota_ap_simple_central'),
    path('nota_potencias_alarmadas/', views.nota_potencias_alarmadas.as_view(), name='nota_potencias_alarmadas'),
    path('nota_llamada/', views.nota_llamada.as_view(), name='nota_llamada'),
    path('nota_correo_saliente/', views.nota_correo_saliente.as_view(), name='nota_correo_saliente'),
    path('nota_correo_entrante/', views.nota_correo_entrante.as_view(), name='nota_correo_entrante'),
    path('nota_escalamiento/', views.nota_escalamiento.as_view(), name='nota_escalamiento'),
])

