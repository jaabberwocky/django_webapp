from . import views # from where this file is, import views.py
from django.urls import path

# define url patterns
urlpatterns = [
	path('', views.index, name='index')
]

