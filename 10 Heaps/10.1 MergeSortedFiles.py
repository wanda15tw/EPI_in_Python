def top_k(k, stream):
    """
    given a stream of strings, output the k longest strings in the sequence
    :param k:
    :param stream:
    :return:
    """
    # Entries are compared by their lengths
    import itertools
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    # print(min_heap)
    for next_string in stream:
        # print(next_string)
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]

def merge_sorted_arrays(sorted_arrays):
    " sort increasingly -> min_heap"
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        print(first_element)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        print('smallest:', smallest_entry, smallest_array_i)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        print('result:', result)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
        print(min_heap)
    return result

def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))

if __name__ == "__main__":
    import heapq

    sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
    merge_sorted_arrays(sorted_arrays)


    # H = [21, 1, 45, 78, 3, 5]
    # heapq.heapify(H)  # This function converts a regular list to a heap.
    # # In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
    # print(H)
    #
    # boy_names = [
    # 'Liam',
    # 'Noah',
    # 'Oliver',
    # 'William',
    # 'Elijah',
    # 'James',
    # 'Benjamin',
    # 'Lucas',
    # 'Mason',
    # 'Ethan',
    # 'Alexander',
    # 'Henry',
    # 'Jacob',
    # 'Michael',
    # 'Daniel',
    # 'Logan',
    # 'Jackson',
    # 'Sebastian',
    # 'Jack',
    # 'Aiden',
    # 'Owen',
    # 'Samuel',
    # 'Matthew',
    # 'Joseph',
    # 'Levi']
    # print(top_k(5, boy_names))

