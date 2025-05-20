## I. Assigned Algorithm

**A. Name of Algorithm:**  
Selection Sort (Customizable Order)

**B. Pseudocode:**  
```plaintext
FUNCTION fnSelectionSort(arrInput, boolAscending = True):
    SET intSize = length of arrInput
    SET arrResult = copy of arrInput
    SET arrSteps = empty list

    FOR i FROM 0 TO intSize - 1:
        SET intMinIndex = i

        FOR j FROM i+1 TO intSize - 1:
            SET varCurrent = lower(arrResult[j]) IF element is string ELSE arrResult[j]
            SET varMin = lower(arrResult[intMinIndex]) IF element is string ELSE arrResult[intMinIndex]

            IF boolAscending AND varCurrent < varMin:
                SET intMinIndex = j
            ELSE IF NOT boolAscending AND varCurrent > varMin:
                SET intMinIndex = j

        IF intMinIndex != i:
            SWAP arrResult[i] WITH arrResult[intMinIndex]
            APPEND current state of arrResult to arrSteps

    RETURN (arrResult, arrSteps)
```

**C. Brief Description:**  
Selection Sort is a comparison-based sorting algorithm that divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly selects the minimum (or maximum) element from the unsorted portion and places it in its correct position. This implementation supports both ascending and descending order and works with numbers or strings. It also records each significant step of the sorting process for visualization or analysis.
---

## II. Python Implementation

**A. Function Code:**  
```python
def fnSelectionSort(arrInput: list, boolAscending: bool = True) -> tuple[list, list]:
    """
    Description:
        Selection Sort algorithm that finds the minimum/maximum element 
        in the unsorted portion and places it at the beginning.

    Parameters:
        arrInput (list): The array to be sorted, can contain numbers or strings
        boolAscending (bool): Sort in ascending order if True, descending if False

    Returns:
        tuple: A tuple containing:
            - list: The sorted array
            - list: List of steps showing the array state after each iteration

    References:
        https://www.geeksforgeeks.org/selection-sort/
    """
    intSize: int = len(arrInput)
    arrResult: list = arrInput.copy()
    arrSteps: list = []

    for i in range(intSize):
        intMinIndex: int = i
        for j in range(i + 1, intSize):
            varCurrent = arrResult[j].lower() if isinstance(arrResult[j], str) else arrResult[j]
            varMin = arrResult[intMinIndex].lower() if isinstance(arrResult[intMinIndex], str) else arrResult[intMinIndex]

            if (varCurrent < varMin and boolAscending) or (varCurrent > varMin and not boolAscending):
                intMinIndex = j

        if intMinIndex != i:
            arrResult[i], arrResult[intMinIndex] = arrResult[intMinIndex], arrResult[i]
            arrSteps.append(arrResult.copy())

    return arrResult, arrSteps
```
---

## III. Simulation / Step-by-Step Example

**A. Sample Input:**  
*["banana", "apple", "cherry", "date"]*
*boolAscending = True*

**B. Step-by-Step Process:**  
*Initial array: ["banana", "apple", "cherry", "date"]*

1. Pass 1 (i = 0):
        Find minimum from index 0 to 3:
        Compare "banana" with "apple" → "apple" < "banana" → min = "apple" at index 1
        Compare "apple" with "cherry" → "apple" < "cherry" → min stays at index 1
        Compare "apple" with "date" → "apple" < "date" → min stays at index 1
        Swap "banana" and "apple":
        `["apple", "banana", "cherry", "date"]`

2. Pass 2 (i = 1):
        Find minimum from index 1 to 3:
        Compare "banana" with "cherry" → "banana" < "cherry" → min = "banana" at index 1
        Compare "banana" with "date" → "banana" < "date" → min stays at index 1
        No swap needed.

3. Pass 4 (i = 3):
        Only one element left ("date") → no operation.

4. Pass 4 (i = 3):
        Minimum from index 3 to 4: min = 6 at index 3
        No swap needed → `[2, 3, 5, 6, 8]`

5. Pass 5 (i = 4):
        Only one element left → no operation.

**C. Final Output:**  
Sorted array: ["apple", "banana", "cherry", "date"]
---

## IV. Discussion

**A. Implementation Logic:**  
- This function applies the classic Selection Sort approach.
- It supports both strings and numbers by normalizing string comparisons to lowercase.
- It allows sorting in ascending or descending order through a Boolean flag.
- Steps are tracked and stored only when a swap occurs, making it suitable for educational or visualization purposes.

**B. References:**  
*https://www.geeksforgeeks.org/selection-sort/*

**C. Possible Improvements / Future Work:**  
- Extend to support custom comparison functions (e.g., sort by length for strings).
- Optimize for stability (current implementation is unstable).
- Add time complexity tracking or step count summary.