from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        """Create about me content"""
        self.about_contents = About(
            title="About Me",
            content="This is the about me content."
        )
        self.about_contents.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"This is the about me content.", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_form_submission(self):
        """Test for submitting the collaboration form"""
        post_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertIn(
            b'Collaboration request received! '
            b'I endeavour to respond within 2 working days.',
            response.content
        )
