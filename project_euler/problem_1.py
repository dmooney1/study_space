"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def get_sum_of_multiples(multiples, max_value):
    """
    Returns the sum of multiples up to max (exc.)

    :param list[int] multiples: the multiples to look for
    :param int max_value: look for multiples up to this value
    :rtype: int
    :return: sum of multiples below max
    """
    all_multiples = []
    for i in range(max_value):
        if not all(i % multiple for multiple in multiples):
            all_multiples.append(i)

    return sum(all_multiples)


if __name__ == '__main__':
    print("Problem 1 solution: {}".format(get_sum_of_multiples([3,5],1000)))
