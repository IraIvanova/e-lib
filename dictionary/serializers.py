from rest_framework import serializers
from .models import Word, Translation, Language


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'language', 'translation']


class WordSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True)

    class Meta:
        model = Word
        fields = ['id', 'word', 'translations']

    def create(self, validated_data):
        translations_data = validated_data.get('translations', [])
        word = Word.objects.create(word=validated_data.get('word'))

        translations_instances = []
        for translation_data in translations_data:
            language = Language.objects.filter(locale=translation_data['language']).first()
            if language:
                translation = Translation.objects.create(word=word, language=language, translation=translation_data['translation'])
                translations_instances.append(translation)

        word.translations.set(translations_instances)

        return word

    def update(self, word, validated_data):
        word.word = validated_data.get('word')
        # word.synonyms.set(validated_data.get('synonyms', word.synonyms.all()))
        word.save()

        translations_data = validated_data.get('translations', [])
        translations_instances = []

        for translation_data in translations_data:
            language = Language.objects.filter(locale=translation_data['language']).first()
            if language:
                translation, _ = Translation.objects.update_or_create(
                    word=word,
                    language=language,
                    defaults={'translation': translation_data['translation']}
                )
                translations_instances.append(translation)

        word.translations.set(translations_instances)

        return word
