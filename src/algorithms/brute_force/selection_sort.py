import os

def selection_sort(arr, ascending=True):
    """
    Selection Sort using Brute Force approach with step tracking.

    Args:
        arr (list): A list of elements (all numbers or all strings).
        ascending (bool): Sort order flag. True for ascending, False for descending.

    Returns:
        tuple: (sorted_list, steps) where steps is a list of list states after each iteration.
    """
    n = len(arr)
    arr_copy = arr.copy()
    steps = []

    for i in range(n):
        intMinIndex = i
        for j in range(i + 1, n):
            a = arr_copy[j].lower() if isinstance(arr_copy[j], str) else arr_copy[j]
            b = arr_copy[intMinIndex].lower() if isinstance(arr_copy[intMinIndex], str) else arr_copy[intMinIndex]

            if (a < b and ascending) or (a > b and not ascending):
                intMinIndex = j

        arr_copy[i], arr_copy[intMinIndex] = arr_copy[intMinIndex], arr_copy[i]

        steps.append(arr_copy.copy())

    return arr_copy, steps

def is_number(s):
    if s == "":
        return False
    intDotCount = 0
    i = 0
    if s[0] == '-':
        if len(s) == 1:
            return False
        i = 1
    while i < len(s):
        c = s[i]
        if c == '.':
            intDotCount += 1
            if intDotCount > 1:
                return False
        elif c < '0' or c > '9':
            return False
        i += 1
    return True

def is_valid_word(s):
    if s == "":
        return False
    return all(c.isalpha() for c in s)

# ========== USER INPUT ==========
try:
    intNumElements = int(input("\nEnter the number of elements to sort: "))
    if intNumElements <= 0:
        print("\nError: The number of elements must be greater than zero.")
        exit(0)
except ValueError:
    print("\nError: Invalid input. Please enter a valid integer.")
    exit(0)

arrUserInput = []
arrInvalidElements = []

for i in range(intNumElements):
    strElement = input(f"Enter element #{i + 1}: ").strip()

    if is_number(strElement):
        # Convert to float or int accordingly
        if '.' in strElement:
            try:
                arrUserInput.append(float(strElement))
            except ValueError:
                arrInvalidElements.append(strElement)
        else:
            try:
                arrUserInput.append(int(strElement))
            except ValueError:
                arrInvalidElements.append(strElement)
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
        # Allow mixing ints and floats but not mixing numbers with strings
        if type(element) != typeFirst and not (isinstance(element, (int, float)) and isinstance(arrUserInput[0], (int, float))):
            print("\nError: Mixed data types detected. Please enter either only numbers or only words.")
            exit(1)

# ========== SCREEN CLEAR ==========
os.system('cls' if os.name == 'nt' else 'clear')

# ========== DISPLAY UNSORTED ==========
print("Unsorted List:")
print("[", end="")
for i, e in enumerate(arrUserInput):
    print(f"'{e}'" if isinstance(e, str) else e, end="")
    if i != len(arrUserInput) - 1:
        print(", ", end="")
print("]")

# ========== SORTING ==========
arrSorted, steps = selection_sort(arrUserInput)

# ========== PRINT STEPS ==========
for i, step in enumerate(steps, start=1):
    print(f"\nStep {i}: [", end="")
    for k, e in enumerate(step):
        print(f"'{e}'" if isinstance(e, str) else e, end="")
        if k != len(step) - 1:
            print(", ", end="")
    print("]")

# ========== DISPLAY SORTED ==========
print("\nSorted List:")
print("[", end="")
for i, e in enumerate(arrSorted):
    print(f"'{e}'" if isinstance(e, str) else e, end="")
    if i != len(arrSorted) - 1:
        print(", ", end="")
print("]")