from django.urls import path
from database import views

urlpatterns = [
	path ('welcome', views.index, name = 'index'),
	path ('ask', views.answer, name = 'answer'),
	path ('nope', views.doesnotexist, name = 'dne')
	
]
