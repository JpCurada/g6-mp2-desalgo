def selection_sort(arr):
    """
    Selection sort is a simple and intuitive sorting algorithm 
    that works by repeatedly selecting the minimum element from the 
    unsorted portion of the array and swapping it with the first element.

    Args:
        arr (list): list of elements to sort
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                