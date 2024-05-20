from django.urls import path

from 여자친구 import views

app_name = '여자친구'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]