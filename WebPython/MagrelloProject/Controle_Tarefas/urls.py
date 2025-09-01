#from django.contrib import admin
#from django.urls import path
#from tarefas import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # autenticação
    path('login/', auth_views.LoginView.as_view(template_name="tarefas/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # tarefas
    path('', views.dashboard, name="dashboard"),
    path('nova/', views.criar_tarefa, name="nova_tarefa"),
    path('editar/<int:pk>/', views.editar_tarefa, name="editar_tarefa"),
    path('excluir/<int:pk>/', views.excluir_tarefa, name="excluir_tarefa"),
]
