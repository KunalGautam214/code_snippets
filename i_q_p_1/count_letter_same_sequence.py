# Count letter of the word as a same sequence.
# input = 'aaabbbaac'
# output = 'a3b3a2c1'

def count_letter(word):
    output = []
    current_char = word[0]
    count = 0

    for item in word:
        if item == current_char:
            count += 1
        else:
            output.append(current_char + str(count))
            current_char = item
            count = 1

    output.append(current_char + str(count))
    return ''.join(output)


s = 'aaabbbaac'
count_letters = count_letter(s)
print(count_letters)
