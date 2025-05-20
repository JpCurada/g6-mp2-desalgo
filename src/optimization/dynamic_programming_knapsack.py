def dynamic_programming_knapsack(items, capacity):
    """
    This function solves the Knapsack Problem using a dynamic programming approach. It creates a 2d table where each cell represents the best value achievable using a subset of items within a given capacity. This then pick an item based on which option gives a higher value.

    Argument:
        weights (list): the weights of the items
        values (list): the values of the items
        capacity (integer): the maximum weight knapsack must only handle
        
    Return:
        tuple: (maximum value, list of selected item (values, weight))
    
    Example:

    """

    #Variables
    length = len(items)
    weights = [item["weight"] for item in items]
    values = [item["value"] for item in items]
    all_valid_subset = []


    #2d table
    table = [[0] * (capacity + 1) for _ in range(length + 1)]

    for i in range(1, length + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                table[i][w] = table[i - 1][w]

    #Trace back to find the selected item
    selected_items = []
    w = capacity
    for i in range(length, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    #format data: (subset item name, total weight, total value)
    selected_items.reverse()

    selected_item_name = [f"Item {i+1}" for i in selected_items]
    value = table[length][capacity]
    weight = capacity - w

    all_valid_subset.extend([selected_item_name, f"Weight: {weight}", f"Value: {value}"])
    
    return selected_item_name, value, all_valid_subset
