from django.urls import path
from .views import Blogview

urlpatterns = [
    path('Blog/', Blogview.as_view()),
]
