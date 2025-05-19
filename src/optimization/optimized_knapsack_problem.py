def knapsack_optimize(items, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming without
    using built-in functions like len, append, or any imports.
    Parameters:
        items (list of dict): Each dictionary contains two keys:
            - "weight" (int): The weight of the item.
            - "value" (int): The value of the item.
        capacity (int): The maximum weight the knapsack can carry.
    Returns:
        tuple:
            best_subset (list of int): List of indices (0-based) of the selected items.
            best_value (int): The maximum total value that can be carried in the knapsack.
            all_valid_subsets (list): All optimal subsets found (for reference).
    """

    # count number_of_items without len()
    number_of_items = 0
    while True:
        try:
            _ = items[number_of_items]
            number_of_items += 1
        except IndexError:
            break

    # Create DP table or 2d Array
    knapsack_table = []
    item_index = 0
    while item_index <= number_of_items:
        row_for_current_item = []
        current_capacity = 0
        while current_capacity <= capacity:
            row_for_current_item += [0]
            current_capacity += 1
        knapsack_table += [row_for_current_item]
        item_index += 1

    # Fill the table
    current_item = 1
    while current_item <= number_of_items:
        current_capacity = 0
        while current_capacity <= capacity:
            item_weight = items[current_item - 1]["weight"]
            item_value = items[current_item - 1]["value"]

            if item_weight <= current_capacity:
                value_with_item = knapsack_table[current_item - 1][current_capacity - item_weight] + item_value
                value_without_item = knapsack_table[current_item - 1][current_capacity]
                if value_with_item > value_without_item:
                    knapsack_table[current_item][current_capacity] = value_with_item
                else:
                    knapsack_table[current_item][current_capacity] = value_without_item
            else:
                knapsack_table[current_item][current_capacity] = knapsack_table[current_item - 1][current_capacity]

            current_capacity += 1
        current_item += 1

    # Backtracking: generate all optimal subsets recursively
    all_valid_subsets = []

    def generate_subsets(current_item, current_capacity, current_subset, total_weight, total_value):
        if current_item == 0:
            # copy current_subset
            collected_subset = []
            index = 0
            while index < len(current_subset):
                collected_subset.append(current_subset[index])
                index += 1
            all_valid_subsets.append((collected_subset, total_weight, total_value))
            return

        item_weight = items[current_item - 1]["weight"]
        item_value = items[current_item - 1]["value"]

        # Check if the item was included in the optimal solution
        if item_weight <= current_capacity:
            if knapsack_table[current_item][current_capacity] == knapsack_table[current_item - 1][current_capacity - item_weight] + item_value:
                # Create a new subset list with the current item included
                new_subset = []
                index = 0
                while index < len(current_subset):
                    new_subset.append(current_subset[index])
                    index += 1
                new_subset.append(current_item - 1)
                generate_subsets(current_item - 1, current_capacity - item_weight, new_subset, total_weight + item_weight, total_value + item_value)

        # Check if the item was excluded in the optimal solution
        if knapsack_table[current_item][current_capacity] == knapsack_table[current_item - 1][current_capacity]:
            generate_subsets(current_item - 1, current_capacity, current_subset, total_weight, total_value)

    generate_subsets(number_of_items, capacity, [], 0, 0)

    best_value = knapsack_table[number_of_items][capacity]

    best_subset = []
    if len(all_valid_subsets) > 0:
        best_subset = all_valid_subsets[0][0]  # pick first optimal subset

    return best_subset, best_value, all_valid_subsets