# Replace n with m in the given list


def replace_number(number_list, n, m):
    for idx, item in enumerate(number_list):
        if isinstance(item, int):
            if item == n:
                number_list[idx] = m
        elif isinstance(item, list):
            replace_number(item, n, m)
    return number_list


numbers = [5, 10, [60, [20, 25, [30, [60, 40], 45], 50, 55], 60], 65, 70]
n = 60
m = 80
print('Original list', numbers)
replaced_list = replace_number(numbers, n, m)
print('Replaced list', replaced_list)
