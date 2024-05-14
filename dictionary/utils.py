from library.models import Text
import re


def get_example_sentences(word, language):
    examples = []
    books = Text.objects.filter(language=language)

    for book in books:
        print(book.content)
        if len(examples) >= 5:
            return examples

        pattern = '[^.]* (?:' + word +') [^.]*\.'
        res = re.findall(pattern, book.content, re.IGNORECASE)

        if res:
            examples.append({'example': res[0], "book": book.id})

    return examples

