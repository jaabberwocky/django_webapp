from . import views # from where this file is, import views.py
from django.urls import path

# name-space URLs
app_name = "polls"

# define url patterns
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote')
]

