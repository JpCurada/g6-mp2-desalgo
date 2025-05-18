def brute_force_knapsack(items, capacity, number_of_items):
    """
    Solves the 0/1 Knapsack problem using brute-force by checking all possible combinations.


    Args:
        items (list of dict): A list of dictionaries, each representing an item with:
            - "weight" (int): The weight of the item.
            - "value" (int): The value of the item.
        capacity (int): The maximum weight the knapsack can carry.
        number_of_items (int): The total number of items available.


    Returns:
        tuple:
            best_value (int): The highest value that can be obtained within the knapsack's capacity.
            best_weight (int): The total weight of the selected combination.
            best_selection (int): An integer bitmask representing which items are selected (1 means selected).
    """
   
    best_value = 0
    best_selection = 0
    best_weight = 0
    selection = 0


    while selection < 2 ** number_of_items:
        total_weight = 0
        total_value = 0
        index = 0


        # Check each item in the current selection combination
        while index < number_of_items:
            if selection & (1 << index):
                total_weight += items[index]["weight"]
                total_value += items[index]["value"]
            index += 1


        # Update best solution found if conditions are met
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_selection = selection
            best_weight = total_weight


        selection += 1


    return best_value, best_weight, best_selection




# Example usage
items = [
    {"weight": 3, "value": 4},
    {"weight": 4, "value": 5},
    {"weight": 2, "value": 6},
]


capacity = 7
number_of_items = 3


best_value, best_weight, best_selection = brute_force_knapsack(items, capacity, number_of_items)


print("\nThe Capacity of knapsack:", capacity)
print("Best total weight of selected items:", best_weight)
print("Best total value of selected items:", best_value)
print("Items Chosen:")


index = 0
while index < number_of_items:
    if best_selection & (1 << index):
        print("   - Item", index + 1,
              "Weight:", items[index]["weight"],
              "Value:", items[index]["value"])
    index += 1



