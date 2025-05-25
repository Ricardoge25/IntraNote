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
    path('nota_reprueba/', views.nota_reprueba.as_view(), name='nota_reprueba'),
    path('nota_resolucion/', views.nota_resolucion.as_view(), name='nota_resolucion'),
    path('nota_especialista/', views.nota_especialista.as_view(), name='nota_especialista'),
    path('tiquete_ap_doble_uno/', views.tiquete_ap_doble_uno.as_view(), name='tiquete_ap_doble_uno'),
    path('tiquete_ap_doble_dos/', views.tiquete_ap_doble_dos.as_view(), name='tiquete_ap_doble_dos'),
    path('tiquete_retiro_empalme/', views.tiquete_retiro_empalme.as_view(), name='tiquete_retiro_empalme'),
    path('tiquete_reingreso_empalme/', views.tiquete_reingreso_empalme.as_view(), name='tiquete_reingreso_empalme'),
])

