def comb_sort(intArr):
    """
        This algorithm use the known bubble sort algorithm, but instead of comparing the adjacent pairs it repeatedly sort pairs of element that are a certain gap apart. This gap starts as the length of the list and is continuously reduced by diving it to 1.3 at each cycle. 

    Reference:
        https://www.tutorchase.com/answers/a-level/computer-science/how-does-the-comb-sort-algorithm-work
        https://www.geeksforgeeks.org/comb-sort/

    Arguments:
        intArray (list): The list of integers to be sorted

    Return:
        list: The sorted list in ascending order

    Example:
        >>>bidirectional_enhanced_selection_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """

    #variables
    intLength = len(intArr)
    intGap = int(len(intArr) / 1.3)

    #loop through array
    while intGap > 0:
        for i in range(intLength - intGap):
            if(intArr[i] > intArr[i + intGap]):
                intTemporaryContainer = intArr[i]
                intArr[i] = intArr[i + intGap]
                intArr[i + intGap] = intTemporaryContainer

        intGap = int(intGap/1.3)
    
    return intArr

print(comb_sort([5, 2, 1, 6, 8, 4]))
print(comb_sort([34, 7, 23, 32, 5, 62, 14, 2, 87, 45]))
print(comb_sort([42, 16, 8, 23, 4, 15, 91, 67, 2, 33, 10, 58]))
print(comb_sort([84, 1, 77, 32, 10, 45, 99, 63, 18, 73, 5, 12, 40, 27, 69, 91, 34, 21, 56, 2, 88, 14, 39, 60, 31]))
print(comb_sort([3, 7, 2, 7, 9, 1, 3, 6, 5, 2, 8, 4, 9, 0, 6]))
print(comb_sort([7, 6, 2, -1, 2, -8, 10, -9]))
