from rest_framework import serializers
from .models import Word, Translation, Language
from .utils import get_example_sentences


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['word_id', 'language', 'translation', 'transcription']


class SynonymsSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['id', 'word', 'translations']


class ExtraFieldSerializer(serializers.Serializer):
    def to_representation(self, instance):
        get_data = self.context['request'].GET
        translation = Translation.objects.filter(language=get_data['language'], word_id=instance.id).first()
        return get_example_sentences(translation.translation, self.context['request'].GET['language'])


class WordSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True)
    synonyms = SynonymsSerializer(many=True, read_only=True)
    examples = ExtraFieldSerializer(source='*', required=False)

    class Meta:
        model = Word
        fields = ['id', 'word', 'translations', 'synonyms', 'examples']

    def create(self, validated_data):
        translations_data = validated_data.get('translations', [])
        word = Word.objects.create(word=validated_data.get('word'))

        translations_instances = []
        for translation_data in translations_data:
            language = Language.objects.filter(locale=translation_data['language']).first()
            if language:
                translation = Translation.objects.create(word=word, language=language,
                                                         translation=translation_data['translation'],
                                                         transcription=translation_data['transcription'])
                translations_instances.append(translation)

        word.translations.set(translations_instances)

        return word

    def update(self, word, validated_data):
        word.word = validated_data.get('word')
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
