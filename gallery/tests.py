from django.test import TestCase
from .models import Editor
# Create your tests here.
# Create your tests here.
class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.isaac= Editor(editor_name = 'Isaac', email = '7248zack@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.isaac,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.isaac.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)