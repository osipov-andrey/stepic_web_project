from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='new'),
   # url(r'', views.test, name='test'),
    path('popular/', views.popular, name='popular'),
    path('question/<int:pk>/', views.question, name='question'),
]
