def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid + 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Variant 1
def search_first_of_greater_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] >= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


# Variant 2
def find_min(A):

    # if A[0] <= A[1]:
    #     return 0
    # if A[-1] <= A[-2]:
    #     return len(A) - 1

    left, right = 0, len(A) - 1

    while left <= right:

        mid = (left + right) // 2
        # print(left, right, mid)

        if mid == 0:
            if A[0] < A[1]:
                return 0
            else:
                left = mid + 1
                mid += 1
        if mid == len(A) - 1:
            if A[-1] < A[-2]:
                return len(A) - 1
            else:
                right = mid - 1
                mid -= 1

        if A[mid] > A[mid - 1]:
            right = mid - 1
        elif A[mid] > A[mid + 1]:
            left = mid + 1
        else: # A[mid] <= A[mid - 1] and A[mid] >= A[mid + 1]
            return mid

    return left, right, mid # for debugging


if __name__ == "__main__":
    # A = [-14, -10, 2, 108, 108, 243, 285, 285]
    # print(search_first_of_greater_k(A, 285))
    # print(search_first_of_greater_k(A, -13))

    # A = [1, -1, -3, -10, -7, 10, 3, 0, 0, 1]
    # print(find_min(A))
    #
    # print(find_min([9, 6, 3, 14, 5, 7, 4]))

    print(find_min([23, 8, 15, 2, 3]))

    print(find_min([1, 2, 3]))

    print(find_min([3, 2, 1]))
