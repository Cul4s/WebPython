from django import forms
from .models import Quadro, Lista, Cartao

class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ['nome']

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nome', 'quadro']

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['titulo', 'descricao', 'lista']
