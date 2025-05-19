"""
Bubble Sort Algorithm:
    The simplest sorting algorithm that works by repeatedly 
    swapping the adjacent elements if they are in the wrong order.

Parameters:
    listInput (list): The list to be sorted.
    ascending (bool): Sort in ascending as default, otherwise sort in descending.
    isNumbers (bool): Check if the list is of numbers or letters.

Returns: 
    The sorted list (listInput).

References:
    https://www.geeksforgeeks.org/bubble-sort-algorithm/

"""
#fn_bubble_sort is a function that takes a list as a parameter
def fnBubbleSort(listInput, ascending=True, isNumbers=True): 

    #intRange is the length of the list
    intSize = len(listInput) 

    #check if the list is of numbers or letters
    if not isNumbers:
        for i in range(intSize):
            #convert the elements to string
            listInput[i] = str(listInput[i])

    #Outer loop to iterate through the list
    for i in range(intSize): 

        # Inner loop to compare adjacent elements
        for j in range(0, intSize - i - 1):

            # Compare if adjacent elements are in the correct order
            if listInput[j] > listInput[j+1]:

                # Swap if they are not in the correct order 
                listInput[j], listInput[j+1] = listInput[j+1], listInput[j]
                
                # Repeat until the list is sorted
    
    #reverse the list if not in ascending order
    if not ascending:
        for i in range(intSize // 2):
            # swap elements from the starting index and the ending index
            listInput[i], listInput[intSize - 1 - i] = listInput[intSize - 1 - i], listInput[i]

    # Return the sorted list
    return listInput 

