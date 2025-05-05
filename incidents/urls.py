from django.urls import path
from . import views

incidents_patterns = ([
    path('', views.ListIncidentView.as_view(), name='incidents'),
    path('<int:pk>/<slug:incident_slug>/', views.IncidentDetailView.as_view(), name='incident'),
    path('<int:incident_id>/<slug:incident_slug>/apertura_entre_clientes/', views.AperturaEntreClientes.as_view(), name ='apertura_entre_clientes'),
    path('<int:incident_id>/<slug:incident_slug>/apertura_contra_central/', views.AperturaContraCentral.as_view(), name ='apertura_contra_central'),
    path('<int:incident_id>/<slug:incident_slug>/equipo_caido/', views.EquipoCaido.as_view(), name ='equipo_caido'),
    path('<int:incident_id>/<slug:incident_slug>/alarma_potencias', views.DiagnosticoPotencias.as_view(), name='alarma_potencias'),
    path('<int:incident_id>/<slug:incident_slug>/llamada_saliente/', views.NotaLlamada.as_view(), name ='llamada_saliente'),
    path('<int:incident_id>/<slug:incident_slug>/ticket_ap_doble_uno/', views.TicketApDobleUno.as_view(), name ='ticket_ap_doble_uno'),
    #path('<int:incident_id>/<slug:incident_slug>/ticket_ap_doble_dos/', views.TicketApDobleDos.as_view(), name ='ticket_ap_doble_dos'),
    path('create/', views.IncidentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.IncidentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.IncidentDeleteView.as_view(), name='delete'),
], 'incidents')

