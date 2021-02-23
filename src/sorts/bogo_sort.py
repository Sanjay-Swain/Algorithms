import random


def bogo_sort(lst: list, iterations=False) -> list:
    """This is an implementation of pure bogo sort algorithm.

    Parameters
    ----------
    iterations: bool [Optional]
        To know hoow much iterations it took to sort.
    lst: list
        The unsorted list

    Returns
    -------
    list
        A sorted list in ascending order

    References
    ----------
    https://en.wikipedia.org/wiki/Bogosort
    """

    # Check list is sorted or not
    def is_sorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    shuffles = 0
    while not is_sorted(lst):
        shuffles += 1
        random.shuffle(lst)
    if iterations:
        print(shuffles)
    return lst
