# How to make a nested list to flat list?
# Input: ["Sam", [10987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]
# Output <list>: ["Hi", "Sam", "Hello12345", 39, 56, 2.0, 10.345678]

def flatten_list(l, new_list=[]):
    for item in l:
        if isinstance(item, list):
            flatten_list(item)
        else:
            new_list.append(item)
    return new_list


nested_list = ["Sam", [10987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]
flatted_list = flatten_list(nested_list)
print(flatted_list)
