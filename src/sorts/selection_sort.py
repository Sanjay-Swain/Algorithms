def selection_sort(lst: list) -> list:
    """This is a selection sort algorithm implementation
    
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
    https://en.wikipedia.org/wiki/Selection_sort
    """

    start = 0
    while start < len(lst):
        min_val = lst[start]
        for i in range(start, len(lst)):
            if lst[start] > lst[i]:
                lst[start], lst[i] = lst[i], lst[start]
        start += 1
    
    return lst
