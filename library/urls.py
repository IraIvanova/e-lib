from django.urls import path
from .views import TextCreateView, TextDetailView

urlpatterns = [
    path('', TextCreateView.as_view()),
    path('text/add', TextCreateView.as_view()),
    path('text/<int:pk>', TextDetailView.as_view()),
]
