from rest_framework import generics, status
from rest_framework.response import Response
from .models import Word, Translation
from django.db.models import Q
from .serializers import WordSerializer, TranslationSerializer


class WordsListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data

        if Word.objects.filter(word=request_data.get('word')).exists():
            return Response({'error': 'Same word already exists'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        search_string = request.GET.get('search')

        if search_string:
            self.queryset = self.queryset.filter(Q(translations__translation__icontains=search_string)).distinct()

        return super().list(request, *args, **kwargs)


class WordsDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class TranslationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
