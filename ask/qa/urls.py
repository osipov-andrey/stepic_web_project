from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='new'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:pk>/', views.question, name='question'),
    path('ask/', views.AskAdd, name='ask'),
    path('signup/', views.user_signup, name='signup'),
]
