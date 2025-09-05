from django.shortcuts import render, redirect
from .models import Quadro, Lista, Cartao
from .form import QuadroForm, ListaForm, CartaoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def home(request):
    quadros = Quadro.objects.all()
    minhas_tarefas = Cartao.objects.all()
    atribuidas = []

    return render(request, 'home.html', {
        'quadros': quadros,
        'minhas_tarefas': minhas_tarefas,
        'atribuidas': atribuidas,
    })

@login_required
def criar_quadro(request):
    if request.method == 'POST':
        form = QuadroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuadroForm()
    return render(request, 'form.html', {'form': form})

@login_required
def criar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CartaoForm()
    return render(request, 'form.html', {'form': form})

@login_required
def criar_lista(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListaForm()
    return render(request, 'form.html', {'form': form})
@login_required
def editar_cartao(request, cartao_id):
    cartao = get_object_or_404(Cartao, id=cartao_id)
    if request.method == 'POST':
        form = CartaoForm(request.POST, instance=cartao)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CartaoForm(instance=cartao)
    return render(request, 'form.html', {'form': form})

@login_required
def excluir_cartao(request, cartao_id):
    cartao = get_object_or_404(Cartao, id=cartao_id)
    if request.method == 'POST':
        cartao.delete()
        return redirect('home')
    return render(request, 'confirmar_exclusao.html', {'cartao': cartao})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso! Faça login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})