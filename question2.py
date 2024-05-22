# find if the given number is a palindrome or not?
def is_simple_palindrome(s):
    return s == s[::-1]
test_string =input()
print(is_simple_palindrome(test_string)) 
