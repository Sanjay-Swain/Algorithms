def bubble_sort(lst: list) -> list:
    """This is a bubble sort algorithm implementation
    
    Parameters
    ----------
    lst: list
        The unsorted list

    Returns
    -------
    list
        A sorted list in ascending order
    """

    for i in range(0, len(lst)):
        for m in range(len(lst) - i - 1):
            if lst[m] > lst[m+1]:
                lst[m], lst[m + 1] = lst[m + 1], lst[m]
    return lst
