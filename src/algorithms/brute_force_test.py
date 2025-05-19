def bubble_sort(arr, ascending=True):
    n = len(arr)
    steps = []
    arr_copy = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if (arr_copy[j] > arr_copy[j+1] and ascending) or (arr_copy[j] < arr_copy[j+1] and not ascending):
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
                steps.append(arr_copy.copy())
        if not swapped:
            break
    
    return arr_copy, steps

def selection_sort(arr, ascending=True):
    n = len(arr)
    steps = []
    arr_copy = arr.copy()
    
    for i in range(n):
        # Find the minimum/maximum element in remaining unsorted array
        idx = i
        for j in range(i + 1, n):
            if (arr_copy[j] < arr_copy[idx] and ascending) or (arr_copy[j] > arr_copy[idx] and not ascending):
                idx = j
                
        # Swap the found minimum/maximum element with the first element
        if idx != i:
            arr_copy[i], arr_copy[idx] = arr_copy[idx], arr_copy[i]
            steps.append(arr_copy.copy())
    
    return arr_copy, steps

def knapsack_brute_force(items, capacity):
    """
    Solves the 0/1 Knapsack problem using brute force approach.
    
    Args:
        items: List of tuples (name, weight, value)
        capacity: Maximum weight capacity of knapsack
        
    Returns:
        best_subset: List of selected items
        best_value: Total value of the best subset
        all_valid_subsets: List of all valid subsets with their weights and values
    """
    n = len(items)
    best_value = 0
    best_subset = []
    all_valid_subsets = []
    
    # Add empty subset
    all_valid_subsets.append(([], 0, 0))
    
    # Generate all possible subsets (2^n possibilities)
    for i in range(1, 2**n):
        # Convert i to binary representation to determine which items to include
        subset = []
        total_weight = 0
        total_value = 0
        
        for j in range(n):
            if (i & (1 << j)) > 0:  # Check if jth bit is set
                subset.append(items[j][0])  # Add item name
                total_weight += items[j][1]  # Add weight
                total_value += items[j][2]   # Add value
        
        # Check if this subset is valid (within capacity)
        if total_weight <= capacity:
            all_valid_subsets.append((subset, total_weight, total_value))
            
            # Update best solution if this subset has higher value
            if total_value > best_value:
                best_value = total_value
                best_subset = subset
    
    # Sort valid subsets by length for better display
    all_valid_subsets.sort(key=lambda x: (len(x[0]), x[2]))
    
    return best_subset, best_value, all_valid_subsets