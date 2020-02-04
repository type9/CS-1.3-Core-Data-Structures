#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    if len(text) <= 1:
        return True

    cleaned_text = ""
    for char in text.lower(): # keeps only letters in lower case
        if char in string.ascii_lowercase:
            cleaned_text += char

    left = 0
    right = len(cleaned_text) - 1
    while cleaned_text[left] == cleaned_text[right]:
        if left + 2 == right:
            return True
        if left + 1 == right:
            return True
        
        right -= 1
        left += 1
    return False
       

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if len(text) <= 1:
        return True

    cleaned_text = ""
    if left == None:
        for char in text.lower(): # keeps only letters in lower case
            if char in string.ascii_lowercase:
                cleaned_text += char
        text = cleaned_text
        left = 0
        right = len(text) - 1

    print(f'TEXT: {text}, LEFT: {text[left]}, RIGHT:{text[right]}')
    if not text[left] == text[right]:
        return False
    if left + 1 == right or left + 2 == right:
        return True

    return is_palindrome_recursive(text, left + 1, right - 1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
