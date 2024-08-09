# Reverse each work of the sentence

def reverse_word_sentence(sentence):
    reverse_sentence = []
    splited_word = sentence.split(' ')
    for item in splited_word:
        reverse_sentence.append(item[::-1])
    return ' '.join(reverse_sentence)


s = 'Python is a versatile language'
reversed_word_sentence = reverse_word_sentence(s)
print(reversed_word_sentence)
