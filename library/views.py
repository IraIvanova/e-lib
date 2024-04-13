from rest_framework import generics, status
from rest_framework.response import Response
from .models import Text
from .serializers import TextSerializer
from .utils import analyze_text


class TextCreateView(generics.CreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def create(self, request):
        request_data = request.data

        text_content = request_data.get('content', [])
        Text.objects.create(**request_data)

        return Response(analyze_text(text_content))
