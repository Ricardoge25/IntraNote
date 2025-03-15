from django.urls import path
from .views import ListNoteView

notes_patterns = ([
    path('', ListNoteView.as_view(), name='notes'),
])

