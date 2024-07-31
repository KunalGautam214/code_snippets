# Write a program to check Palindrome without using predefined functions

def check_palimdrome(s):
    length = len(s)
    flag = False
    for item in range(0, length//2):
        if s[item] != s[length - item - 1]:
            flag = True
            break
    if flag:
        return False
    else:
        return True


s = 'madam'
is_palimdrome = check_palimdrome(s)
print(is_palimdrome)
print(s[::] == s[::-1])
