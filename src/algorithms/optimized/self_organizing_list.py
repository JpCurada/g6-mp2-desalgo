def fnSelfOrganizingSearch(arrInput: list, varTarget: any) -> int:
    """
    Description:
        This function implements a self-organizing list search that positions the most 
        frequently searched items at the front of the array to improve sequential search 
        performance. It uses the count method where each element maintains a count of 
        how many times it has been accessed.

    Parameters:
        arrInput (list): The array to search in, can contain any comparable type
        varTarget (any): The target element to search for

    Returns:
        int: Index of the target element in the current state of the list, -1 if not found

    Reference:
        https://www.geeksforgeeks.org/self-organizing-list-count-method/
    """
    if not arrInput:
        return -1

    # Convert array elements to [value, count] pairs
    arrList = [[x, 0] for x in arrInput]
    intLength = len(arrInput)
    intIndex = -1

    # Search for the target and update its count
    for i in range(intLength):
        if arrList[i][0] == varTarget:
            intIndex = i
            arrList[i][1] += 1
            break

    if intIndex == -1:
        return -1

    # Reorganize list based on access frequency
    while (intIndex > 0 and arrList[intIndex][1] > arrList[intIndex - 1][1]):
        # Swap elements and their counts
        arrList[intIndex], arrList[intIndex - 1] = arrList[intIndex - 1], arrList[intIndex]
        intIndex -= 1

    # Update the original input array to reflect the new order
    for i in range(intLength):
        arrInput[i] = arrList[i][0]

    return intIndex

    