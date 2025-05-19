def knapsack_solver(items, knapsack_capacity, number_of_items):
    """
    Solves the 0/1 Knapsack problem using dynamic programming without
    using built-in functions like len, append, or any imports.

    Parameters:
        items (list of dict): Each dictionary contains two keys:
            - "weight" (int): The weight of the item.
            - "value" (int): The value of the item.
        knapsack_capacity (int): The maximum weight the knapsack can carry.
        number_of_items (int): The total number of items available.

    Returns:
        tuple:
            max_value (int): The maximum total value that can be carried in the knapsack.
            selected_items_count (int): The number of items selected to achieve max value.
            chosen_item_list (list of int): List of indices (0-based) of the selected items.
    """

    # Creating a dynamic programming table or 2d array
    knapsack_table = []
    item_index = 0

    while item_index <= number_of_items:
        row_for_current_item = []
        current_capacity = 0
        while current_capacity <= knapsack_capacity:
            row_for_current_item += [0] 
            current_capacity += 1
        knapsack_table += [row_for_current_item]
        item_index += 1

    # Inserting the values in the table
    current_item = 1

    while current_item <= number_of_items:
        current_capacity = 0
        while current_capacity <= knapsack_capacity:
            item_weight = items[current_item - 1]["weight"]
            item_value = items[current_item - 1]["value"]

            if item_weight <= current_capacity:
                value_with_item = knapsack_table[current_item - 1][current_capacity - item_weight] + item_value
                value_without_item = knapsack_table[current_item - 1][current_capacity]
                if value_with_item > value_without_item:
                    knapsack_table[current_item][current_capacity] = value_with_item
                else:
                    knapsack_table[current_item][current_capacity] = value_without_item
            else:  # item is too heavy
                knapsack_table[current_item][current_capacity] = knapsack_table[current_item - 1][current_capacity]
            
            current_capacity += 1
        current_item += 1

    # Backtracking the chosen items and collecting the values we choose
    chosen_item_list = []
    current_item = number_of_items
    remaining_capacity = knapsack_capacity

    while current_item > 0:
        if knapsack_table[current_item][remaining_capacity] != knapsack_table[current_item - 1][remaining_capacity]:
            chosen_item_list += [current_item - 1]
            remaining_capacity -= items[current_item - 1]["weight"]
        current_item -= 1

    # Counting the number of items selected 
    selected_items_count = 0
    for item in chosen_item_list:
        selected_items_count += 1

    return knapsack_table[number_of_items][knapsack_capacity], selected_items_count, chosen_item_list


# ==== Example usage ====

items = [
    {"weight": 3, "value": 4},
    {"weight": 4, "value": 5},
    {"weight": 2, "value": 6},
]

knapsack_capacity = 7
number_of_items = 3

max_value, selected_items_count, chosen_item_list = knapsack_solver(items, knapsack_capacity, number_of_items)

print("The Knapsack Capacity:", knapsack_capacity)
print("Maximum Value of the Knapsack Problem:", max_value)
print("Number of items selected:", selected_items_count)
print("Items Chosen:")

index = 0
while index < selected_items_count:
    item_index = chosen_item_list[index]
    print("   - Item", item_index + 1,
          "Weight:", items[item_index]["weight"],
          "Value:", items[item_index]["value"])
    index += 1
