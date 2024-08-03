# Read the file and count word of the file.

def read_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def count_word_of_a_file(file_data):
    file_data = file_data.split()
    d = {}
    for word in file_data:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    return d

file_path = '../files/count_word_of_a_file.txt'
data = read_file(file_path)

# 1'st way to solve
count_word_dict = count_word_of_a_file(data)
print(count_word_dict)
sorted_word_count = dict(sorted(count_word_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_word_count)


# 2'st way to solve
from collections import Counter
file_data = data.split()
count_word = Counter(file_data)
print(count_word)


