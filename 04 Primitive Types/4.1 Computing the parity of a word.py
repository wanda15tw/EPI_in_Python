def parity(x):
    """
    compute the parity of a word
    :param x:
    :return: 1 if the number of 1s in the word is odd, otherwise 0
    """


    # determine max wordsize
    import sys
    if sys.maxsize > 2 ** 32:
        wordsize = 64
    else:
        wordsize = 32

    # split x in half and then XOR -> O(log n)
    while (wordsize > 1):
        wordsize //= 2
        print(bin(x), wordsize)
        x ^= (x >> wordsize)


    return x & 1

print(parity(int('11010111', 2)))
print(parity(int('11010110', 2)))
