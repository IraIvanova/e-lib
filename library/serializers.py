from rest_framework import serializers
from .models import Text
from dictionary.models import Word
from .utils import analyze_text



class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'content', 'name', 'author', 'language']
