from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.registerHandler, name="cadastro"),
    path('login/', views.loginHandler, name="login"),
    path('logout/', views.logoutHandler, name="logout"),
    path('alterar-senha/', views.newPassword, name="alterar-senha"),
    path('area-do-usuario/', views.userArea, name="area-do-usuario"),
]
