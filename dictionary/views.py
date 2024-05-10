from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word, Translation, Language
from django.db.models import Q, Prefetch
from .serializers import WordSerializer, TranslationSerializer


class WordsListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()

    serializer_class = WordSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data

        if Word.objects.filter(word=request_data.get('word')).exists():
            return Response({'error': 'Same word already exists'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        search_string = request.GET.get('search')
        language = Language.objects.filter(name=request.GET.get('language')).first()
        word_id = request.GET.get('id')

        if search_string:
            self.queryset = self.queryset.filter(Q(translations__translation__icontains=search_string),
                                                 Q(translations__language=language)).distinct()
        elif word_id:
            self.queryset = self.queryset.filter(id=word_id)

        return super().list(request, *args, **kwargs)


class WordsDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class TranslationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def list(self, request, *args, **kwargs):
        search_string = request.GET.get('search')
        language = Language.objects.filter(name=request.GET.get('language')).first()
        word_id = request.GET.get('id')

        if search_string:
            self.queryset = self.queryset.filter(translation__icontains=search_string, language=language)
        elif word_id:
            self.queryset = self.queryset.filter(word_id=word_id, language=language)

        return super().list(request, *args, **kwargs)


class WordSynonymsActionsAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        word = Word.objects.get(pk=data.get("word_id"))
        synonym_word = Word.objects.get(pk=data.get("synonym_word_id"))
        word.synonyms.add(synonym_word)

        return "ok"
