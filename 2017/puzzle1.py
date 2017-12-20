def get_sum(input):
    '''  (str) -> int

    Finds the sum of all digits that match the next digit in the list.
    The list is circular, so the digit after the last digit is the first
    digit in the list.

    >>> get_sum('1111')
    4
    >>> get_sum('1234')
    0
    >>> get_sum('1122')
    3
    >>> get_sum('91212129')
    9
    '''
    first_number = input[0]
    sum = 0
    number = 0

    while number != len(input)-1:
        if input[number] == input[number+1]:
            sum += int(input[number])
            number += 1
        else:
            number += 1

    if input[number] == first_number:
        sum += int(input[number])

    return print(sum)

def get_sum2(input_):
    ''' (str) -> int

    Finds the sum of all digits that match the digit halfway around the
    list (len(list)/2).

    >>> get_sum2('1212')
    6
    >>> get_sum2('1122')
    0
    >>> get_sum2('123123')
    12
    '''
    sum_ = 0
    len_ = len(input_)
    halflen = int(len_/2)

    for number in range(len_):
        if input_[number] == input_[(number + halflen) % len_]:
            sum_ += int(input_[number])

    return print(sum_)



    
