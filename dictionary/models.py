from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    locale = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class PartOfSpeech(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=100)
    synonyms = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='related_synonyms')
    parts_of_speech = models.ManyToManyField(PartOfSpeech)

    def __str__(self):
        return self.word


class Translation(models.Model):
    language = models.CharField(max_length=50)
    translation = models.CharField(max_length=100)
    word = models.ForeignKey(Word, related_name='translations', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.language}: {self.translation}"



