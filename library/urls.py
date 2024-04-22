from django.urls import path
from .views import TextCreateView

urlpatterns = [
    path('text/add', TextCreateView.as_view()),
]
