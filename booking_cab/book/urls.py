from django.urls import path
from book import views
urlpatterns = [
    path('',views.index),
    path('create',views.create),
]
