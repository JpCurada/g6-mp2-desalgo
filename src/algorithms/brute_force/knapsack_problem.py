def knapsack_brute_force(items, max_capacity):
    """
    Solves the 0/1 Knapsack problem using brute force approach.

    Args:
        items: List of tuples (name, weight, value)
        max_capacity: Maximum weight capacity of knapsack

    Returns:
        best_subset: List of selected item names
        best_value: Total value of the best subset
        all_valid_subsets: List of all valid subsets with their weights and values
    """
    number_of_items = len(items)
    best_value = 0
    best_subset = []
    all_valid_subsets = []

    # Include the empty subset
    all_valid_subsets.append(([], 0, 0))

    subset_index = 1
    while subset_index < 2 ** number_of_items:
        current_subset = []
        current_total_weight = 0
        current_total_value = 0
        item_index = 0

        while item_index < number_of_items:
            if subset_index & (1 << item_index):
                item_name, item_weight, item_value = items[item_index]
                current_subset.append(item_name)
                current_total_weight += item_weight
                current_total_value += item_value
            item_index += 1

        if current_total_weight <= max_capacity:
            all_valid_subsets.append((current_subset, current_total_weight, current_total_value))

            if current_total_value > best_value:
                best_value = current_total_value
                best_subset = current_subset

        subset_index += 1

    # Manual bubble sort by length of subset, then by value (ascending)
    outer = 0
    while outer < len(all_valid_subsets):
        inner = 0
        while inner < len(all_valid_subsets) - outer - 1:
            subset_a, weight_a, value_a = all_valid_subsets[inner]
            subset_b, weight_b, value_b = all_valid_subsets[inner + 1]

            if len(subset_a) > len(subset_b) or (
                len(subset_a) == len(subset_b) and value_a > value_b):
                # Swap the entries
                all_valid_subsets[inner], all_valid_subsets[inner + 1] = all_valid_subsets[inner + 1], all_valid_subsets[inner]

            inner += 1
        outer += 1

    return best_subset, best_value, all_valid_subsets


# Example usage
items = [
    ("Item 1", 3, 4),
    ("Item 2", 4, 5),
    ("Item 3", 2, 6),
]

capacity = 7

best_subset, best_value, all_valid_subsets = knapsack_brute_force(items, capacity)

print(f"\nKnapsack Capacity: {capacity}")
print(f"Best subset of items chosen: {best_subset}")
print(f"Best total value: {best_value}")
print("\nAll valid subsets: (subset item nme, total weight, total value):")
for subset_names, total_weight, total_value in all_valid_subsets:
    print(f"  {subset_names}, Weight: {total_weight}, Value: {total_value}")
