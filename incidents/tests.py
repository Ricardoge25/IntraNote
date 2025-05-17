from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Incident

class IncidentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.incident = Incident.objects.create(
            id_servicio='12345',
            nombre_anillo='Anillo1',
            nombre_cliente='Cliente1',
            nit='123456789',
            nombre_contacto='Contacto1',
            numero_contacto='1234567890',
            correo_contacto='contacto1@example.com',
            direccion_servicio='Calle 123',
            ip='192.168.1.1',
            usuario=self.user
        )

    def test_incident_creation(self):
        self.assertEqual(self.incident.nombre_cliente, 'Cliente1')
        self.assertEqual(self.incident.usuario.username, 'testuser')

    def test_incident_str(self):
        self.assertEqual(str(self.incident), '12345')

    def test_incident_nit(self):
        self.assertEqual(self.incident.nit, '123456789')


class IncidentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.incident = Incident.objects.create(
            id_servicio='12345',
            nombre_anillo='Anillo1',
            nombre_cliente='Cliente1',
            nit='123456789',
            nombre_contacto='Contacto1',
            numero_contacto='1234567890',
            correo_contacto='contacto1@example.com',
            direccion_servicio='Calle 123',
            ip='192.168.1.1',
            usuario=self.user
        )

    def test_list_incidents_view(self):
        response = self.client.get('/incidents/')  # Ajusta la URL según tu configuración
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cliente1')

    def test_create_incident_view(self):
        data = {
            'id_servicio': '54321',
            'nombre_anillo': 'Anillo2',
            'nombre_cliente': 'Cliente2',
            'nit': '987654321',
            'nombre_contacto': 'Contacto2',
            'numero_contacto': '0987654321',
            'correo_contacto': 'contacto2@example.com',
            'direccion_servicio': 'Calle 456',
            'ip': '192.168.1.2',
            'usuario': self.user.id
        }
        response = self.client.post('/incidents/create/', data)
        self.assertEqual(response.status_code, 302)  # Redirige tras crear
        self.assertTrue(Incident.objects.filter(id_servicio='54321').exists())

    def test_access_without_login(self):
        self.client.logout()
        response = self.client.get('/incidents/')
        self.assertEqual(response.status_code, 302)  # Redirige al login

    def test_update_incident_view(self):
        data = {
            'id_servicio': '12345',
            'nombre_anillo': 'AnilloEditado',
            'nombre_cliente': 'ClienteEditado',
            'nit': '123456789',
            'nombre_contacto': 'ContactoEditado',
            'numero_contacto': '1234567890',
            'correo_contacto': 'contacto1@example.com',
            'direccion_servicio': 'Calle Editada',
            'ip': '192.168.1.1',
            'usuario': self.user.id
        }
        response = self.client.post(f'/incidents/update/{self.incident.id}/', data)
        self.assertEqual(response.status_code, 302)
        self.incident.refresh_from_db()
        self.assertEqual(self.incident.nombre_cliente, 'ClienteEditado')

    def test_delete_incident_view(self):
        response = self.client.post(f'/incidents/delete/{self.incident.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Incident.objects.filter(id=self.incident.id).exists())

    def test_cannot_access_other_user_incident(self):
        other_user = User.objects.create_user(username='otheruser', password='54321')
        other_incident = Incident.objects.create(
            id_servicio='99999',
            nombre_anillo='OtroAnillo',
            nombre_cliente='OtroCliente',
            nit='000000000',
            nombre_contacto='OtroContacto',
            numero_contacto='0000000000',
            correo_contacto='otro@example.com',
            direccion_servicio='Otra Calle',
            ip='10.0.0.1',
            usuario=other_user
        )
        response = self.client.get(f'/incidents/update/{other_incident.id}/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_form(self):
        data = {
            'id_servicio': '',  # Campo requerido vacío
            'nombre_anillo': '',
            'nombre_cliente': '',
            'nit': '',
            'nombre_contacto': '',
            'numero_contacto': '',
            'correo_contacto': 'noemail',  # Email inválido
            'direccion_servicio': '',
            'ip': '',
            'usuario': self.user.id
        }
        response = self.client.post('/incidents/create/', data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este campo es obligatorio.', html=True)


