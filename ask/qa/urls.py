
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='new'),
    url(r'test/', views.test, name='test'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:pk>/', views.question, name='question'),
    path('ask/', views.AskAdd, name='ask')
]
