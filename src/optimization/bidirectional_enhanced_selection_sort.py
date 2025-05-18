def bidirectional_enhanced_selection_sort(intArray):
    """
        This function use the advantage of applying the selection sort algorithm bidirectionally (from left to right & right to left in one iteration), swapping the previous maximum/minimum to the location before the new maximum/minimum, storing the new location of previous maximum/minimum to the stack, and once there's no new maximum/minimum, then the current maximum/minimum will be place to its correct position. To continue, the previous maximum/minimum in the stack will be use as the starting point for the next iteration and will repeat the process until the array is sorted. And Finally, the sorting will stop when there is no swapped performed and empty stack or the stack pop of both are equal, or the front search is greater than the end search and the end search is less than the front search.
    
    Reference:
        https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3828471
        
    Arguments:
        intArray (list): The list of integers to be sorted

    Return:
        list: The sorted list in ascending order

    Example:
        >>>bidirectional_enhanced_selection_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """

    #variables
    stackMaxLocation = []
    stackMinLocation = []
    intEnd = len(intArray)
    intFront = 0
    intMaxBegin = 0
    intCurrentMax = 0
    intCurrentMin = intEnd - 2

    #loop through the array
    while intFront<intEnd and intEnd>intFront:
        booleanSwapped = False

        #loop from left to right (sort the large value)
        for i in range(intCurrentMax, intEnd):

            if(intArray[intCurrentMax] < intArray[i]):
                booleanSwapped = True
                intTemporaryContainer = intArray[intCurrentMax]
                intArray[intCurrentMax] = intArray[i - 1]
                intArray[i - 1] = intTemporaryContainer

                stackMaxLocation.append(i - 1)

                intCurrentMax = i
        
        intTemporaryContainer = intArray[intCurrentMax]
        intArray[intCurrentMax] = intArray[intEnd - 1]
        intArray[intEnd - 1] = intTemporaryContainer

        intEnd -= 1

        #loop from right to left (sort the small value)
        for j in range(intCurrentMin, intFront - 1, -1):

            if(intArray[intCurrentMin] > intArray[j]):
                booleanSwapped = True
                intTemporaryContainer = intArray[intCurrentMin]
                intArray[intCurrentMin] = intArray[j + 1]
                intArray[j + 1] = intTemporaryContainer

                stackMinLocation.append(j + 1)

                intCurrentMin = j

        intTemporaryContainer = intArray[intCurrentMin]
        intArray[intCurrentMin] = intArray[intFront]
        intArray[intFront] = intTemporaryContainer

        intFront += 1

        try:
            intCurrentMax = stackMaxLocation.pop()
            intCurrentMin = stackMinLocation.pop()

            if(intCurrentMax == intCurrentMin):
                break

        except IndexError:
            
            if(not booleanSwapped):
                break

            intCurrentMax = intFront
            intCurrentMin = intEnd
            continue

    return intArray

print(bidirectional_enhanced_selection_sort([5, 2, 1, 6, 8, 4]))
print(bidirectional_enhanced_selection_sort([34, 7, 23, 32, 5, 62, 14, 2, 87, 45]))
print(bidirectional_enhanced_selection_sort([42, 16, 8, 23, 4, 15, 91, 67, 2, 33, 10, 58]))
print(bidirectional_enhanced_selection_sort([84, 1, 77, 32, 10, 45, 99, 63, 18, 73, 5, 12, 40, 27, 69, 91, 34, 21, 56, 2, 88, 14, 39, 60, 31]))
print(bidirectional_enhanced_selection_sort([3, 7, 2, 7, 9, 1, 3, 6, 5, 2, 8, 4, 9, 0, 6]))
print(bidirectional_enhanced_selection_sort([7, 6, 2, -1, 2, -8, 10, -9]))





