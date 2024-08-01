# Write a program to check Palindrome without using predefined functions

def check_palindrome(s):
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
is_palindrome = check_palindrome(s)
print(is_palindrome)
print(s[::] == s[::-1])
