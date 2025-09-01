#from django import forms
#from .models import Tarefa

class Tarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome','descrição','status_atv','dono_atv']