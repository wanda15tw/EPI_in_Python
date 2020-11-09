def int_to_string(x):
    if x < 0:
        x = -x
        is_negative = True
    else:
        is_negative = False

    s = [] # an array to store digits in string
    while True:
        s.append(str(x%10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(x):
    import string

    if x[0] == '-':
        is_negative = True
        x = x[1:]

    result = 0
    for d in x:
        result = result * 10 + string.digits.index(d)

    if is_negative:
        result = 0 - result

    return result

print(int_to_string(-1230))
print(string_to_int('-1230'))