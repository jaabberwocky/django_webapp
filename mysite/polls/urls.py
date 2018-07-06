from . import views # from where this file is, import views.py
from django.urls import path

# name-space URLs
app_name = "polls"

# define url patterns
urlpatterns = [
	path('', views.index, name='index'),
	path('specifics/<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote')
]

