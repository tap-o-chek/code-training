import string

def is_palindrome(word):
    word = ''.join(char for char in word if char.isalnum()).lower()
    return word == word[::-1]

def filter_palindromes(text):
    words = text.split()
    palindromes = [word for word in words if is_palindrome(word)]
    return ' '.join(palindromes)

input_text = input()
result = filter_palindromes(input_text)
print(result)
