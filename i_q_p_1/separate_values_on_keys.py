# Input: {
#     "key1": {
#         "a": [0, 1, 2],
#         "b": [1, 2, 3],
#         "c": [2, 3, 4]
#     },
#     "key2": {
#         "a": [5, 6, 7],
#         "b": [6, 7, 8],
#     }
# }
# Output:
# list_a = [[0,1,2], [5,6,7]]
# list_b = [[1,2,3], [6,7,8]]
# list_c = [[2,3,4]]

d_keys = {
    "key1": {
        "a": [0, 1, 2],
        "b": [1, 2, 3],
        "c": [2, 3, 4]
    },
    "key2": {
        "a": [5, 6, 7],
        "b": [6, 7, 8],
    }
}

list_a = []
list_b = []
list_c = []
for k, v in d_keys.items():
    if v.get('a', None):
        list_a.append(v.get('a'))
    if v.get('b', None):
        list_b.append(v.get('b'))
    if v.get('c', None):
        list_c.append(v.get('c'))

print('List a', list_a, '\nList b', list_b, '\nList c', list_c)
