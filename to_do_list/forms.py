from django import forms
from .models import  Todos

class TodosForm(forms.ModelForm):
    class Meta:
        model= Todos
        fields = ['todo_name','todo_desc','todo_status']
        labels = {
            'todo_name':'Name of the todo',
            'todo_desc':'Description',
            'todo_status':'Status'
        }

        widgets = {
            'todo_name':forms.TextInput(attrs={'class':'form-control'}),
            'todo_desc':forms.TextInput(attrs={'class':'form-control'}),
        }