from django import template
from incidents.models import Incident

register = template.Library()

@register.simple_tag
def get_incident_list():
    incidents = Incident.objects.all()
    return incidents

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})