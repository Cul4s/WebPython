from django.contrib import admin
from django.urls import path
from Magrello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('criar-quadro/', views.criar_quadro, name='criar_quadro'),
    path('criar-cartao/', views.criar_cartao, name='criar_cartao'),
    path('criar-lista/', views.criar_lista, name='criar_lista'),
    path('editar-cartao/<int:cartao_id>/', views.editar_cartao, name='editar_tarefa'),
    path('excluir-cartao/<int:cartao_id>/', views.excluir_cartao, name='excluir_tarefa'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar, name='registrar'),
]
