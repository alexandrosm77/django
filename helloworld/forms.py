from django.forms import ModelForm, Textarea
from helloworld.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']

