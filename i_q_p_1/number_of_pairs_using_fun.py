# Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array
# whose sum is equal to sum

from itertools import combinations


def combination(l, s):
    pair_list = []
    index_list = []
    for (i, num_1), (j, num_2) in combinations(enumerate(l), 2):
        if sum([num_1, num_2]) == s:
            pair_list.append((num_1, num_2))
            index_list.append((i, j))
    return pair_list, index_list


input_list = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
sum_1 = 11
pairs, indexes = combination(input_list, sum_1)
print(pairs)
print(indexes)
