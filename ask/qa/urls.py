from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='new'),
<<<<<<< HEAD
    url(r'test/', views.test, name='test'),
=======
   # url(r'', views.test, name='test'),
>>>>>>> 4e2f287caf2ed1da998ee5cc366d2e632faf7fb6
    path('popular/', views.popular, name='popular'),
    path('question/<int:pk>/', views.question, name='question'),
]
