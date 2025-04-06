from django.test import TestCase
from .models import Note
from .forms import NoteForm

class NoteModelTest(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(title="Test title", content="Test content")
        self.assertEqual(note.title, "Test title")
        self.assertEqual(note.content, "Test content")
        self.assertEqual(str(note), "Test title")  # Tikrina __str__()

class NoteFormTest(TestCase):
    def test_valid_form(self):
        form = NoteForm(data={"title": "Valid title", "content": "Valid content"})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = NoteForm(data={"title": "", "content": ""})
        self.assertFalse(form.is_valid())

class NoteViewTest(TestCase):
    def test_get_notes_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Tikrina, ar puslapis pasiekiamas

    def test_post_create_note(self):
        response = self.client.post('/create/', {"title": "Test title", "content": "Test content"})
        self.assertEqual(response.status_code, 302)  # Tikrina peradresavimą po POST
        self.assertTrue(Note.objects.filter(title="Test title").exists())  # Tikrina, ar užrašas sukurtas