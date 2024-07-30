# Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array
# whose sum is equal to sum

def pair_number(l, s):
    length = len(l)
    pairs_list = []
    index_list = []
    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if l[i] + l[j] == s:
                pairs_list.append((l[i], l[j]))
                index_list.append((i, j))
            j += 1
        i += 1
    return pairs_list, index_list


input_list = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
sum_1 = 11
pairs, indexes = pair_number(input_list, sum_1)
print(pairs, indexes)
for i in pairs:
    print(i)
for i in indexes:
    print(i)

print(len(pairs))
