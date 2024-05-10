from django.urls import path
from .views import TranslationListCreateAPIView, WordsDetailView, WordsListCreateView, WordSynonymsActionsAPIView

urlpatterns = [
    path('words/<int:pk>', WordsDetailView.as_view()),
    path('words', WordsListCreateView.as_view()),
    path('translations/', TranslationListCreateAPIView.as_view()),
    path('words/synonyms', WordSynonymsActionsAPIView.as_view()),
]
