# Sort list of tuples according to second value
# Input: [("a", 250), ("b", 210), ("c", 300)]
# Output: ["b", "a", "c"]

def sort_list_of_tuples_ascending(l):
    d = dict(l)
    d_sorted = dict(sorted(d.items(), key=lambda x: x[1]))
    return list(d_sorted.keys())


list_of_tuples = [("a", 250), ("b", 210), ("c", 300)]
l = sort_list_of_tuples_ascending(list_of_tuples)
print(l)

