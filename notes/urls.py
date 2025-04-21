from django.urls import path
from . import views

notes_patterns = ([
    path('', views.ListNoteView.as_view(), name='notes'),
    path('nota_diagnostico/',  views.nota_diagnostico.as_view(), name='nota_diagnostico'),
])

