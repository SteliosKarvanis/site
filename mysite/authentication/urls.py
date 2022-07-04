from django.shortcuts import redirect
from django.urls import path
from .views import pass_gen, pass_generated

urlpatterns = [
    path('', lambda req: redirect('login/')),
    path('login/', pass_gen, name="login"),
    path('register/', pass_generated, name="index"),
]