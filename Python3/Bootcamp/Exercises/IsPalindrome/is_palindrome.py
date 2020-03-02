def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]
    
print(is_palindrome("a man a plan a canal Panama"))