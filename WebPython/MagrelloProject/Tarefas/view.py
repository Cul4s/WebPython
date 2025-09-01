#from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
#from .models import Tarefa
#from .forms import TarefaForm

@login_required
def dashboard(request):
    status_filtro = request.GET.get("status")

    minhas_tarefas = Tarefa.objects.filter(criador=request.user)
    atribuidas = Tarefa.objects.filter(responsavel=request.user)

    if status_filtro and status_filtro != "todas":
        minhas_tarefas = minhas_tarefas.filter(status=status_filtro)
        atribuidas = atribuidas.filter(status=status_filtro)

    return render(request, "tarefas/dashboard.html", {
        "minhas_tarefas": minhas_tarefas,
        "atribuidas": atribuidas,
        "status_filtro": status_filtro,
    })


@login_required
def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            return redirect("dashboard")
    else:
        form = TarefaForm()
    return render(request, "tarefas/tarefa_form.html", {"form": form})

@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, criador=request.user)
    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, "tarefas/tarefa_form.html", {"form": form})

@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, criador=request.user)
    tarefa.delete()
    return redirect("dashboard")
