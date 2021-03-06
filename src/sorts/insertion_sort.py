def insertion_sort(lst: list) -> list:
    """This is an insertion sort algorithm implementation
    
    Parameters
    ----------
    lst: list
        The unsorted list

    Returns
    -------
    list
        A sorted list in ascending order
    
    References
    ----------
    https://en.wikipedia.org/wiki/Insertion_sort
    """

    for i in range(1, len(lst)):
        for m in range(i, 0, -1):
            if lst[m - 1] > lst[m]:
                 lst[m - 1], lst[m] = lst[m], lst[m - 1]
            else:
                break
    return lst
