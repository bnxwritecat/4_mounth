from django.urls import path
from posts import views

urlpatterns = [
    path("contacts/", views.get_method, name='view-get_method'),
    path("about/", views.get_about, name='view-get_about'),
    path("hello/", views.hello, name='view-hello')
]