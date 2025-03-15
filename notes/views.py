from django.views.generic.list import ListView
from .models import Note

# Create your views here.
class ListNoteView(ListView):
    model = Note