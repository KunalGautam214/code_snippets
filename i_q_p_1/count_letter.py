# Count letter of the word.
# Input: ‘aaabbbccc’
# output: ‘3a3b3c’

a = 'aaabbbccc'
b = ''
for i in a:
    count = a.count(i)
    if i not in b:
        b += str(count) + i

print(b)

