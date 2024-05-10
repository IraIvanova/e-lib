import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from dictionary.models import Word, PartOfSpeech, Translation
from collections import defaultdict


class AnalysisResultDTO:
    def __init__(self, total_words, new_words_added):
        self.total_words = total_words
        self.new_words_added = new_words_added


def analyze_text(text):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    lemmatizer = WordNetLemmatizer()
    partsOfSpeech = PartOfSpeech.objects.all()
    lemmas = []

    total_words = len(tokens)
    new_words_added = 0

    # grouped_data = defaultdict(list)
    # for value, key in pos_tags:
    #     grouped_data[key].append(value)
    # print(grouped_data)

    for word, pos_tag in pos_tags:
        partOfSpeech = partsOfSpeech.filter(code=pos_tag)
        lemma = lemmatizer.lemmatize(word)
        lemmas.append((word, pos_tag, lemma))

        if not Word.objects.filter(word=lemma).exists():
            new_words_added += 1
            word_instance = Word.objects.create(word=lemma)
            word_instance.parts_of_speech.set(partOfSpeech)
            translation_instance = Translation.objects.create(language='English', translation=lemma, word=word_instance)
            word_instance.translations.set([].append(translation_instance))

    # return AnalysisResultDTOSerializer(AnalysisResultDTO(total_words, new_words_added)).data
    return {
        "total_words": total_words,
        "new_words_added": new_words_added
    }


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
