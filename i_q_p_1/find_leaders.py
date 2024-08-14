# Write a program to print all the LEADERS in the array. An element is leader if it is greater than
# all the elements to its right side. And the rightmost element is always a leader
# Input: [16, 17, 3, 4, 5, 2]
# Output: [17, 5, 2]

# Time complexity O(n*n)
def leaders(n):
    length = len(n)
    i = 0
    leader_list = []
    while i < length:
        j = i + 1
        leader_flag = False
        while j < length:
            if n[i] < n[j]:
                leader_flag = True
                break
            j += 1
        if not leader_flag:
            leader_list.append(n[i])
        i += 1
    return leader_list


# Time complexity O(n)
def find_leader(n):
    current_value = n[-1]
    leader_list = [current_value]
    for i in n[::-1]:
        if i > current_value:
            leader_list.append(i)
            current_value = i
    return leader_list


l1 = [16, 17, 3, 4, 5, 2]
leaders_list = leaders(l1)
print(leaders_list)

leaders_list_2 = find_leader(l1)
print(leaders_list_2)


