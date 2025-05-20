## I. Assigned Algorithm

**A. Name of Algorithm:**  
Optimized Selection Sort

**B. Pseudocode:**  
```plaintext
FUNCTION optimizedSelectionSort(listInput, ascending = True):
    SET n = length of listInput
    SET arr_copy = copy of listInput

    FOR i FROM 0 TO n - 1:
        SET min_index = i
        SET current_val = lower(arr_copy[i]) IF string ELSE arr_copy[i]

        FOR j FROM i+1 TO n - 1:
            SET comp_val = lower(arr_copy[j]) IF string ELSE arr_copy[j]

            IF ascending AND comp_val < current_val:
                SET min_index = j
                SET current_val = comp_val
            ELSE IF NOT ascending AND comp_val > current_val:
                SET min_index = j
                SET current_val = comp_val

        IF min_index != i:
            SWAP arr_copy[i] WITH arr_copy[min_index]

    RETURN arr_copy
```

**C. Brief Description:**  
*This optimized version of Selection Sort iteratively finds the minimum (or maximum) element in the unsorted portion of the list and swaps it with the first unsorted element — but only if a smaller (or larger) value is found. It avoids unnecessary swaps, making it more efficient in practice. It supports both numeric and case-insensitive string comparisons and maintains the original list by working on a copy.*
---

## II. Python Implementation

**A. Function Code:** 
```python

def optimizedSelectionSort(listInput, ascending=True):
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
    n = len(listInput)
    arr_copy = listInput.copy()

    for i in range(n):
        min_index = i
        current_val = arr_copy[min_index].lower() if isinstance(arr_copy[min_index], str) else arr_copy[min_index]

        for j in range(i + 1, n):
            comp_val = arr_copy[j].lower() if isinstance(arr_copy[j], str) else arr_copy[j]

            if (ascending and comp_val < current_val) or (not ascending and comp_val > current_val):
                min_index = j
                current_val = comp_val

        if min_index != i:
            arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]

    return arr_copy
```
---

## III. Simulation / Step-by-Step Example

**A. Sample Input:**  
*[5, 3, 8, 6, 2]*

**B. Step-by-Step Process:**  
*We perform searches that increase the frequency of accessed elements and reorder the list accordingly.*

1. Pass 1 (i = 0):
        *Find the minimum from index 0 to 4: min = 2 at index 4*
        *Swap 5 and 2 → `[2, 3, 8, 6, 5]`*

2. Pass 2 (i = 1):
        *Minimum from index 1 to 4: min = 3 at index 1*
        *No swap needed → `[2, 3, 8, 6, 5]`*

3. Pass 3 (i = 2):
        *Minimum from index 2 to 4: min = 5 at index 4*
        *Swap 8 and 5 → `[2, 3, 5, 6, 8]`*

4. Pass 4 (i = 3):
        *Minimum from index 3 to 4: min = 6 at index 3*
        *No swap needed → `[2, 3, 5, 6, 8]`*

5. Pass 5 (i = 4):
        *Only one element left → no operation.*

**C. Final Output:**  
*Sorted List (Ascending): [2, 3, 5, 6, 8]*
---

## IV. Discussion

**A. Implementation Logic:**  

- The algorithm improves over the standard selection sort by avoiding unnecessary swaps.
- It works for both strings and numbers. If comparing strings, it converts them to lowercase to ensure case-insensitive sorting.
- It does not modify the original list; a copy is created for in-place sorting.

**B. References:**  
GeeksForGeeks – Selection Sort

**C. Possible Improvements / Future Work:**  
- Add step tracking like in educational visualizations.
- Accept a custom comparison key (e.g., by length or external ranking).
- Convert to a stable version by shifting instead of swapping.