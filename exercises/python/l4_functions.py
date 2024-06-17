#Write functions here

def test_odd(*args):
    result = []
    for number in args:
        if number % 2 == 1:
            result.append(number)
        else:
            pass
    return result


def test_even(*args):
    result = []
    for number in args:
        if number % 2 == 0:
            result.append(number)
        else:
            pass
    return result


def find_max(*args):
    max = args[0]

    for number in args:
        if number > max:
            max = number
        else:
            pass
    return max


def find_min(*args):
    min = args[0]

    for number in args:
        if number < min:
            min = number
        else:
            pass
    return min


def find_sum(*args):
    # does not work idk why :)
    result = 0

    for number in args:
        result =+ number


    return sum(args)



