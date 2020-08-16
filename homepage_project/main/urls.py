from django.urls import include, path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='index'),
    path('exrave',views.exrave, name='exrave'),
]
