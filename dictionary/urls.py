from django.urls import path
from .views import TranslationListCreateAPIView, WordsDetailView, WordsListCreateView

urlpatterns = [
    path('words/<int:pk>', WordsDetailView.as_view()),
    path('words', WordsListCreateView.as_view()),
    path('translations/', TranslationListCreateAPIView.as_view()),
]
