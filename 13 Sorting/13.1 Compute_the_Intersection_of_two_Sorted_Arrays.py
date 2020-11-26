import bisect

# brute-force
def intersect_two_sorted_arrays_WJ(A, B):
    return [e for e in set(A) if e in set(B)]

def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1] and a in B)]

# BS
def intersect_two_sorted_arrays_BST(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i-1]) and is_present(a)
    ]

def intersect_two_sorted_arrays_linear(A, B):
    i, j, intersection = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else: # A[i] > B[j]
            j += 1
    return intersection