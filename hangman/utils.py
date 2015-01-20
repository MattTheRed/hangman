from hangman.models import Word

def bootstrap_words():
    words = open("/usr/share/dict/words", "r")
    for word in words:
        cleaned_word = word.strip().lower()
        Word.objects.create(word=cleaned_word)
