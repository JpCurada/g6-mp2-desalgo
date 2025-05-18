import os

def selection_sort(arr):
    """
    Selection Sort using Brute Force approach.

    Selection Sort is a simple and intuitive sorting algorithm that works by repeatedly selecting the minimum element from
    the unsorted portion of the array and swapping it with the first element.

    Args:
        arr (list): A list of elements (either all numbers or all strings).

    Returns:
        list: A new list containing the sorted elements in ascending order.
    """
    for i in range(len(arr)):
        intMinIndex  = i
        for j in range(i + 1, len(arr)):
            a = arr[j].lower() if isinstance(arr[j], str) else arr[j]
            b = arr[intMinIndex].lower() if isinstance(arr[intMinIndex], str) else arr[intMinIndex]
            if a < b:
                intMinIndex = j
        if intMinIndex != i:
            arr[i], arr[intMinIndex] = arr[intMinIndex], arr[i]
    return arr

def is_number(str):
    if str == "":
        return False
    intDotCount = 0
    i = 0
    if str[0] == '-':
        if len(str) == 1:
            return False
        i = 1
    while i < len(str):
        c = str[i]
        if c == '.':
            intDotCount += 1
            if intDotCount > 1:
                return False
        elif c < '0' or c > '9':
            return False
        i += 1
    return True

def is_valid_word(str):
    if str == "":
        return False
    return all(c.isalpha() for c in str)

# ========== USER INPUT ==========
try:
    intNumElements = int(input("\nEnter the number of elements to sort: "))
    if intNumElements <= 0:
        print("\nError: The number of elements must be greater than zero.")
        exit(0)
except ValueError:
    print("\nError: Invalid input. Please enter a valid integer.")
    exit(0)

arrUserInput  = []
arrInvalidElements  = []

for i in range(intNumElements):
    strElement = input(f"Enter element #{i + 1}: ").strip()
    
    if is_number(strElement):
        if '.' in strElement:
            intSign = -1 if strElement[0] == '-' else 1
            arrParts = strElement.lstrip('-').split('.')
            intPart = 0
            dblDecPart = 0.0

            for ch in arrParts[0]:
                intPart  = intPart * 10 + (ord(ch) - ord('0'))

            if len(arrParts) > 1:
                divisor = 10.0
                for ch in arrParts[1]:
                    dblDecPart += (ord(ch) - ord('0')) / divisor
                    dblDivisor *= 10

            arrUserInput.append(intSign * (intPart + dblDecPart))
        else:
            intNum = 0
            intSign = 1
            intStart = 0
            if strElement[0] == '-':
                intSign = -1
                intStart = 1
            intIdx = intStart
            while intIdx < len(strElement):
                intDigit = ord(strElement[intIdx]) - ord('0')
                intNum = intNum * 10 + intDigit
                intIdx += 1
            arrUserInput.append(intSign * intNum)
    elif is_valid_word(strElement):
        arrUserInput.append(strElement)
    else:
        arrInvalidElements.append(strElement)

# ========== INVALID ENTRY HANDLING ==========
if arrInvalidElements:
    print("\nNote: The following entries were invalid and have been excluded:")
    print(", ".join(arrInvalidElements))

if not arrUserInput:
    print("\nNo valid inputs detected. Exiting program.")
    exit(0)

# ========== UNIFORM DATA TYPE CHECK ==========
if len(arrUserInput) > 1:
    typeFirst = type(arrUserInput[0])
    for element in arrUserInput[1:]:
        if type(element) != typeFirst and not (isinstance(element, (int, float)) and isinstance(typeFirst, (int, float))):
            print("\nError: Mixed data types detected. Please enter either only numbers or only words.")
            exit(1)

# ========== SCREEN CLEAR ==========
os.system('cls' if os.name == 'nt' else 'clear')

# ========== DISPLAY UNSORTED ==========
print("Unsorted List:")
print("[", end="")
for i in range(len(arrUserInput)):
    e = arrUserInput[i]
    print(f"'{e}'" if isinstance(e, str) else e, end="")
    if i != len(arrUserInput) - 1:
        print(", ", end="")
print("]")

# ========== SORTING ==========
arrSorted = selection_sort(arrUserInput.copy())

# ========== DISPLAY SORTED ==========
print("\nSorted List:")
print("[", end="")
for i in range(len(arrSorted)):
    e = arrSorted[i]
    print(f"'{e}'" if isinstance(e, str) else e, end="")
    if i != len(arrSorted) - 1:
        print(", ", end="")
print("]")