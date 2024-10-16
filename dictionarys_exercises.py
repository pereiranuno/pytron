# Exercise 1

sentences = [
    "I am a student",
    "I am a teacher",
    "I am a programmer"
]

# Cria um dicionário vazio para armazenar as contagens de palavras
word_count = {}

def count_words(sentences) -> {str,int}:
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


def count_wordsVania(sentences) -> {str,int}:
    word_count = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Chama a função e imprime o resultado
print(count_wordsVania(sentences))