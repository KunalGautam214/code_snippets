# Sort a mixed element list

def mix_element_sort(each_item):
    try:
        item = int(each_item)
        return (1, item)
    except Exception:
        return (0, each_item)


mix_list = ["Sam", 10987, 2.0, "Hi", 39, "Hello12345", 56, 10.345678, "He!!0", 1]
print('Original list', mix_list)
mix_list.sort(key=mix_element_sort)
print('Sorted list', mix_list)
