import collections

def if_palindromic(s):
    len(s) = n
    if n % 2 == 1:
        return s[:n//2] == s[-1:n//2-1:-1]
    else:
        return s[:n//2] == s[-1:n//2:-1]

def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1