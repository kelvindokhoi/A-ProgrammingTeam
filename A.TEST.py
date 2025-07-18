from functools import lru_cache

@lru_cache
def is_palindrome(word):
    if len(word) in [0,1]:
        return True
    if word[0]==word[-1]:
        return is_palindrome(word[1:-1])
    return False
