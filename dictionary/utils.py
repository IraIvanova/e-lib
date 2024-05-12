from library.models import Text
import re


def get_example_sentences(word):
    examples = []
    books = Text.objects.all()

    for book in books:
        if len(examples) >= 5:
            return examples

        pattern = '[^.]* (?:' + word +') [^.]*\.'
        res = re.findall(pattern, book.content, re.IGNORECASE)

        if res:
            examples.append({'example': res[0], "book": book.id})

    return examples

