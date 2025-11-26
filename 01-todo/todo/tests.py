from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTests(TestCase):
    def test_create_todo_defaults_and_str(self):
        t = Todo.objects.create(title="Test task")
        self.assertEqual(str(t), "Test task")
        self.assertFalse(t.completed)
        self.assertEqual(t.priority, 0)

class TodoViewTests(TestCase):
    def test_list_view_empty(self):
        resp = self.client.get(reverse('todo:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "No todos yet.")