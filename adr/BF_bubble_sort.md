# Algorithm Activity Documentation Report

---

## I. Assigned Algorithm

**A. Bubble Sort:**  


**B. Pseudocode:**  
```plaintext
Start
    - Accept array(arrInput) and boolean(boolAscending) to check if it will be sorted ascending or descending.
    - initialize the size of the array(intSize)
    - initialize the variable to store the steps (arrSteps)
    - initialize the variable for the result of the sorting by first copying the array that is passed first (arrResult)
    -If boolAscending is true
        - for i is less than size of the array
            set boolSwapped to false
                - for j is less than the size of array minus i
                    - if the value of element at index[j] is greater than the element at inde[j+1]
                        swap the elements of index[j] and index[j+1]
                        set boolSwapped to true
                - if boolSwapped is true
                    append a copy of arrayResult to arrSteps
                - if boolSwapped is false
                    exit the loop
    - else if boolAscending is false
        proceed to do the same process but it will swap if the value of element at index[j] is less than that of element at index[j+1]
    -return variables arrResult, arrSteps
End
```

**C. Brief Description:**  
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity are quite high. 

---

## II. Python Implementation

**Function Code:**  
```python
def fnBubbleSort(arrInput: list, boolAscending: bool = True) -> tuple[list, list]:
    """
    Description:
        The simplest sorting algorithm that works by repeatedly 
        swapping the adjacent elements if they are in the wrong order.
    Parameters:
        arrInput (list): The array to be sorted, can contain numbers or strings
        boolAscending (bool): Sort in ascending order if True, descending if False
    Returns: 
        tuple: A tuple containing:
            - list: The sorted array
            - list: List of steps showing the array state after each iteration
    References:
        https://www.geeksforgeeks.org/bubble-sort-algorithm/
    """

    intSize: int = len(arrInput)
    arrSteps: list = []
    arrResult: list = arrInput.copy()

    if boolAscending:
        for i in range(intSize):
            boolSwapped: bool = False
            for j in range(0, intSize - i - 1):
                if arrResult[j] > arrResult[j + 1]:
                    arrResult[j], arrResult[j + 1] = arrResult[j + 1], arrResult[j]
                    boolSwapped = True

            if boolSwapped:
                arrSteps.append(arrResult.copy())

            if not boolSwapped:
                break
    else:
        for i in range(intSize):
            boolSwapped: bool = False
            for j in range(0, intSize - i - 1):
                if arrResult[j] < arrResult[j + 1]:
                    arrResult[j], arrResult[j + 1] = arrResult[j + 1], arrResult[j]
                    boolSwapped = True

            if boolSwapped:
                arrSteps.append(arrResult.copy())

            if not boolSwapped:
                break

    return arrResult, arrSteps
```
---

## III. Simulation / Step-by-Step Example

**A. Sample Input:**  

arrInput[37, 98, 5, 12, 9,], boolAscending = true

**B. Step-by-Step Process:**  

1. Start first iteration

2. Start to compare the first element (37) with the second element (98)
    - 37 < 98, therefore no swap is needed

3. Compare the next element which is 98 and 5
    - 98 > 5, swap their position
    - New array: [37, 5, 98, 12, 9]

4. Compare the next element which is 98 and 12
    - 98 > 12, swap their position
    - New array: [37, 5, 12, 98, 9]

5. Compare the next element which is 98 and 9
    - 98 > 9, swap their position
    - New array: [37, 5, 12, 9, 98]

6. First iteration complete

7. Start second iteration

8. Compare the first element (37) with the second element (5)
    - 37 > 5, swap their position
    - New array: [5, 37, 12, 9, 98]

9. Compare the next element which is 37 and 12
    - 37 > 12, swap their position
    - New array: [5, 12, 37, 9, 98]

10. Compare the next element which is 37 and 9
    - 37 > 9, swap their position
    - New array: [5, 12, 9, 37, 98]

11. Second iteration complete

12. Start third iteration

13. Compare the first element (5) with the second element (12)
    - 5 < 12, no swap needed

14. Compare the next element which is 12 and 9
    - 12 > 9, swap their position
    - New array: [5, 9, 12, 37, 98]

15. Third iteration

16. Start fourth iteration

17. Compare the first element (5) with the second element (9)
    - 5 < 9, no swap needed

18. Fourth iteration complete

Final sorted array: [5, 9, 12, 37, 98]

**C. Final Output:**  

- Step 1: [37, 5, 98, 12, 9]
- Step 2: [37, 5, 12, 98, 9]
- Step 3: [37, 5, 12, 9, 98]
- Step 4: [5, 37, 12, 9, 98]
- Step 5: [5, 12, 37, 9, 98]
- Step 6: [5, 12, 9, 37, 98]
- Step 7: [5, 9, 12, 37, 98]

- Sorted List: [5, 9, 12, 37, 98]

---

## IV. Discussion

**A. Implementation Logic:**  
The function takes input from the user then it also takes a boolean to check if it should be ascending or descending. The function used and conditional statement to check if it should be ascending or descending. In sorting the list, the function uses a nested for loop. The outer loop keeps track of how many passes while the inner loop is the one that compares and swap the adjacent elements. The rightmost value is always the first to be sorted that is why each iteration of the outerloop subtracts in the range of the inner loop. The process repeats until the list is sorted.

**B. References:**  
- https://www.geeksforgeeks.org/bubble-sort-algorithm/

**C. Possible Improvements / Future Work:**  
One possible improvement is to accept not just integer or float values but also allow to sort letters in descending and ascending order.

Other minor improvement would be displaying the process of ascending and descending side by side automatically for comparisons and to avoid asking for the user if it should be sorted in ascending or descending. 

---