# Invariants boot camp
def has_two_sum(A, t):
    i, j = 0, len(A)-1

    A.sort()

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

    return False


def has_three_sum(A, t):

    A.sort()
    n = len(A)

    for i in range(n):
        j, k = i+1, n-1
        while j < k:
            if A[j] + A[k] == t - A[i]:
                return True
            elif A[j] + A[k] < t:
                j += 1
            else:
                k -= 1
    return False


def has_three_sum_f(A, t):
    A.sort()
    return any(has_two_sum(A, t-a) for a in A)


A = [11, 2, 5, 7, 3]
print(has_three_sum(A, 21))
print(has_three_sum(A, 22))
print(has_three_sum_f(A, 21))
print(has_three_sum_f(A, 22))


def has_k_sum(A, t, k):
    """

    :param A: assume sorted
    :param t:
    :param k: number of elements to sum
    :return:
    """
    # base case
    if k == 1:
        return any(a==t for a in A)

    if k == 2:
        return has_two_sum(A, t)

    if k == 3:
        return any(has_two_sum(A, t-a) for a in A)


    return any(has_k_sum(A, t-a, k-1) for a in A)

import random
A.sort()
t = random.randint(1, 100)
print(t)
print(has_k_sum(A, t, 5))