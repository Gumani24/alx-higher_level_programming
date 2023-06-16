#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numb = 0
    den = 0

    for tup in my_list:
        numb += tup[0] * tup[1]
        den += tup[1]

    return (numb / den)
