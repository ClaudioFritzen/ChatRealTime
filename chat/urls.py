from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('room/<str:room>/', views.room, name='room'),  # Página da sala
    path('checkviews/', views.checkviews, name='checkviews'),  # Verificação de visualizações
    #path('checkview', views.checkview, name='checkview')
]