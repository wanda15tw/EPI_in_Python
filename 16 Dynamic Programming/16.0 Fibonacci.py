def fibonacci_td(n, cache={}):
    """
    Top-Down: Start with the final condition and recursively get the result of its sub-problems.
    may cache to save time complexity at the expense of O(n) storage
    :param n:
    :return: the nth fibonacci number
    """
    # if n <= 1:
    #     return n
    # return fibonacci_td(n - 1) + fibonacci_td(n - 2)

    # with cache
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_td(n-1) + fibonacci_td(n-2)
    return cache[n]

def fibonacci_bu(n):
    """
    Bottom-Up: Start with the base condition and pass the value calculated until now recursively.
    Generally, these are tail recursions.
    :param n:
    :return:
    """
    if n <= 1:
        return n

    f_minus1, f_minus2 = 0, 1
    for _ in range(n):
        f_n = f_minus1 + f_minus2
        # print(f_n, f_minus1, f_minus2)
        f_minus1, f_minus2 = f_n, f_minus1

    return f_n

# print(fibonacci_td(10))
print(fibonacci_bu(10))


def find_maximum_subarray(A):

    pass


A = [-323, -994, 561, 689, -582, -246, -125, -577, 850, -321]

# brute-force
def find_maximum_subarray(A):

    max_sum, n = float('-inf'), len(A)

    # # O(n**3)
    # for i in range(n):
    #     for j in range(i, n):
    #         # print(i, j)
    #         max_sum = max(max_sum, sum(A[i:j+1]))

    # O(n**2)
    # S[k] = sum of A[0] to A[k]
    S = [0] + [sum(A[:k+1]) for k in range(n)]

    for j in range(n):
        for i in range(j+1):
            # print(i, j)
            # print(i, 'to', j, '=', S[j+1] - S[i])
            max_sum = max(max_sum, S[j+1] - S[i])

    return max_sum

# divide-and-conquer
def find_maximum_subarray(A):
    """
    1) Divide the given array in two halves
    2) Return the maximum of following three
    ….a) Maximum subarray sum in left half (Make a recursive call)
    ….b) Maximum subarray sum in right half (Make a recursive call)
    ….c) Maximum subarray sum such that the subarray crosses the midpoint
    :param A:
    :return:
    """
    m = len(A) // 2
    L = find_maximum_subarray(A[:m])
    R = find_maximum_subarray(A[m:])
    return

    return find_maximum_subarray(L), find_maximum_subarray(R),

print(find_maximum_subarray(A))


def maxCrossingSum(arr, l, m, h):

    # Include elements on left of mid
    sm = 0
    left_sum = float('-inf')

    for i in range(m, l-1, -1):
        sm += arr[i]

        if sm > left_sum:
            left_sum = sm

    # include elements on right of mid
    sm = 0
    right_sum = float('-inf')

    for i in range(m+1, h+1):
        sm += arr[i]
        if sm > right_sum:
            right_sum = sm

    return max(left_sum + right_sum, left_sum, right_sum)


def maxSubArraySum(arr, l, h):
    """
    return sum of maximum sum subaray in arr[l:h+1]
    :param arr:
    :param l:
    :param h:
    :return:
    """

    # base case: only one element
    if l == h:
        return arr[l]

    # find middle point
    m = (l+h) // 2

    return max(maxSubArraySum(arr, l, m), \
               maxSubArraySum(arr, m+1, h), \
               maxCrossingSum(arr, l, m, h))


# Driver Code
A = [-323, -994, 561, 689, -582, -246, -125, -577, 850, -321]
n = len(A)

max_sum = maxSubArraySum(A, 0, n-1)
print(max_sum)



# DP solution
import itertools

for running_sum in itertools.accumulate(A):
    print(running_sum)
    min_sum = min(min_sum, running_sum) # min S_k have been so far
    max_sum = max(max_sum, running_sum - min_sum) # max sub_sum by running_sum - min_sum seen so far
