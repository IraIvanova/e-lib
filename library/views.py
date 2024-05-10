from rest_framework import generics, status
from rest_framework.response import Response
from .models import Text
from dictionary.models import Language
from .serializers import TextSerializer
from .utils import analyze_text


class TextCreateView(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def list(self, request, *args, **kwargs):
        search_string = request.GET.get('search')
        language = Language.objects.filter(name=request.GET.get('language')).first()
        book_id = request.GET.get('id')

        if search_string:
            self.queryset = self.queryset.filter(name__icontains=search_string, language=language)
        elif book_id:
            self.queryset = self.queryset.filter(pk=book_id)
        else:
            self.queryset = self.queryset.filter(language=language)

        return super().list(request, *args, **kwargs)

    def create(self, request):
        request_data = request.data
        text_content = request_data.get('content', [])
        Text.objects.create(**request_data)

        return Response(analyze_text(text_content))


class TextDetailView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
