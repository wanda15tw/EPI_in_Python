def dutch_flag_partition_On(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        smaller = 0
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # Second pass = group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

def dutch_flag_partition_O1(pivot_index, A):
    pivot = A[pivot_index]

    smaller, equal, larger =  0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal +- 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]