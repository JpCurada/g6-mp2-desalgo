"""
Optimized Selection Sort Algorithm:
    A sorting algorithm that repeatedly finds the minimum (or maximum) element 
    from the unsorted part and swaps it with the first unsorted element. 
    This optimized version swaps only when a new minimum (or maximum) is found.

Parameters:
    listInput (list): The list to be sorted (numbers or strings).
    ascending (bool): Sort in ascending order by default; otherwise descending.

Returns: 
    The sorted list (listInput).

Notes:
    - String comparisons are case-insensitive.
    - Works on a copy of the input list to avoid modifying the original list.
"""

def optimizedSelectionSort(listInput, ascending=True):
    # Get the length of the list
    n = len(listInput)

    # Create a copy of the list to avoid modifying the original
    arr_copy = listInput.copy()

    # Iterate through each element in the list
    for i in range(n):
        # Assume the current element is the minimum (or maximum)
        min_index = i

        # Convert to lowercase if string for case-insensitive comparison
        current_val = arr_copy[min_index].lower() if isinstance(arr_copy[min_index], str) else arr_copy[min_index]

        # Find the minimum (or maximum) element in the remaining unsorted list
        for j in range(i + 1, n):
            comp_val = arr_copy[j].lower() if isinstance(arr_copy[j], str) else arr_copy[j]

            # Check if a smaller (or larger if descending) element is found
            if (ascending and comp_val < current_val) or (not ascending and comp_val > current_val):
                min_index = j
                current_val = comp_val

        # Swap only if a new minimum (or maximum) is found
        if min_index != i:
            arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]

    # Return the sorted list
    return arr_copy