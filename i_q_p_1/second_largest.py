# Find a second largest element from a list

def second_largest(items):
    largest = second_largest = items[0]
    for item in items:
        if largest < item:
            second_largest = largest
            largest = item
        elif item > second_largest and largest != item:
            second_largest = item
        elif largest == second_largest and second_largest != item:
            second_largest = item
    return largest, second_largest


list_items = [11, 2, 1, 0, 10, 11, 6, 5, 10, 11]
largest, second_largest = second_largest(list_items)
print('Largest', largest)
print('Second Largest', second_largest)
