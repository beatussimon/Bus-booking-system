from django.urls import path
from . import views
urlpatterns= [
    path("", views.index, name="index"),
    path("<int:pk>/", views.info, name="info"),
    path("<int:pk>/book/", views.book, name="book")
]