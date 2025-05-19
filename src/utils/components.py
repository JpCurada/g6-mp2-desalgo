import streamlit as st
import random

@st.fragment
def sorting_form(key, sorting_function):
    col1, col2 = st.columns([1, 3])
    with col1:
        list_generator = st.radio(
            "Select an option",
            ["Generate Random Values", "Enter Values Manually"],
            key=f"{key}_radio"
        )
        is_number_range = st.toggle(
            "Use Numbers",
            key=f"{key}_toggle_numbers"
        )
        is_ascending = st.toggle(
            "Sort Ascending",
            key=f"{key}_toggle_ascending"
        )

        input_values = ""
        list_length = 5

        if list_generator == "Generate Random Values":
            list_length = st.number_input(
                "Enter the length of the list",
                min_value=1,
                value=5,
                step=1,
                format="%d",
                key=f"{key}_number_input"
            )
        else:
            if is_number_range:
                input_values = st.text_input(
                    "Enter numbers separated by commas",
                    key=f"{key}_text_input_numbers"
                )
            else:
                input_values = st.text_input(
                    "Enter characters separated by commas",
                    key=f"{key}_text_input_chars"
                )

        if st.button("Generate", key=f"{key}_generate_btn"):
            with col2.container(border=True):
                list_values = []
                if list_generator == "Generate Random Values":
                    if is_number_range:
                        list_values = [random.randint(1, 100) for _ in range(int(list_length))]
                    else:
                        list_values = [chr(random.randint(65, 90)) for _ in range(int(list_length))]
                else:
                    if input_values:
                        if is_number_range:
                            try:
                                list_values = [int(item.strip()) for item in input_values.split(",") if item.strip()]
                                if not list_values:
                                    st.error("Please enter at least one valid number")
                                    return
                            except ValueError:
                                st.error("Please enter valid numbers separated by commas")
                                return
                        else:
                            list_values = [item.strip() for item in input_values.split(",") if item.strip()]
                            if not list_values:
                                st.error("Please enter at least one character")
                                return
                    else:
                        st.error("Please enter some values or choose 'Generate Random Values'")
                        return

                unsorted_col, sorted_col = st.columns(2)

                with unsorted_col:
                    st.write("Unsorted list:")
                    st.write(list_values)

                with sorted_col:
                    sorted_list, sorting_steps = sorting_function(list_values, is_ascending)
                    st.write("Sorted list:")
                    st.write(sorted_list)

                with st.expander("Click this to view the sorting steps", expanded=False):
                    if sorting_steps:
                        for i, step in enumerate(sorting_steps):
                            st.write(f"Step {i+1}: {step}")
                    else:
                        st.write("The list was already sorted.")

@st.fragment
def item_adder(item_key, on_delete):
    with st.container(border=True):
        weight_col, value_col, delete_col = st.columns([2, 2, 1])
        with weight_col:
            weight = st.number_input(
                label="Weight",
                key=f"{item_key}_weight",
                min_value=1,
                step=1,
                format="%d"
            )
        with value_col:
            value = st.number_input(
                label="Value",
                key=f"{item_key}_value",
                min_value=1,
                step=1,
                format="%d"
            )
        
        delete_col.empty()
        with delete_col:
            if st.button("Delete", key=f"{item_key}_delete_btn", use_container_width=True):
                on_delete(item_key)

def knapsack_form(key, knapsack_function):
    # Initialize session state variables if they don't exist
    if f"{key}_items" not in st.session_state:
        st.session_state[f"{key}_items"] = []  # list of (item_name, weight, value)
        st.session_state[f"{key}_capacity"] = 5
        st.session_state[f"{key}_next_item_id"] = 1
        st.session_state[f"{key}_results"] = None
        st.session_state[f"{key}_formatted_items"] = []  # Store the formatted items

    left_col, right_col = st.columns([1, 1])
    
    def add_item():
        item_id = st.session_state[f"{key}_next_item_id"]
        st.session_state[f"{key}_items"].append((item_id, 1, 1))  # Default weight and value
        st.session_state[f"{key}_next_item_id"] += 1

    with left_col:
        with st.container(border=True):
            # Capacity input
            capacity_col, add_col = st.columns([2, 1])
            with capacity_col:
                st.session_state[f"{key}_capacity"] = st.number_input(
                    "Capacity", 
                    min_value=1, 
                    value=st.session_state[f"{key}_capacity"],
                    step=1,
                    key=f"{key}_capacity_input"
                )
            with add_col:
                st.button("Add", on_click=add_item, key=f"{key}_add_item")
            
            # Items section
            st.subheader("Items")
            
            # Display each item with input fields
            for idx, (item_id, weight, value) in enumerate(st.session_state[f"{key}_items"]):
                item_col, weight_col, value_col, remove_col = st.columns([2, 1, 1, 0.5])
                
                with item_col:
                    st.text_input(
                        "Item", 
                        value=f"Item {item_id}", 
                        key=f"{key}_item_name_{idx}",
                        disabled=True
                    )
                
                with weight_col:
                    new_weight = st.number_input(
                        "Weight", 
                        value=weight,
                        min_value=1,
                        step=1,
                        key=f"{key}_item_weight_{idx}"
                    )
                    st.session_state[f"{key}_items"][idx] = (item_id, new_weight, st.session_state[f"{key}_items"][idx][2])
                
                with value_col:
                    new_value = st.number_input(
                        "Value", 
                        value=value,
                        min_value=1,
                        step=1,
                        key=f"{key}_item_value_{idx}"
                    )
                    st.session_state[f"{key}_items"][idx] = (item_id, st.session_state[f"{key}_items"][idx][1], new_value)
                
                with remove_col:
                    if st.button("Delete", key=f"{key}_remove_item_{idx}"):
                        st.session_state[f"{key}_items"].pop(idx)
                        st.rerun()
            
            # Action buttons
            reset_col, solve_col = st.columns(2)
            with reset_col:
                if st.button("Reset", use_container_width=True, key=f"{key}_reset_btn"):
                    for k in [
                        f"{key}_items",
                        f"{key}_capacity",
                        f"{key}_next_item_id",
                        f"{key}_results",
                        f"{key}_formatted_items"
                    ]:
                        if k in st.session_state:
                            del st.session_state[k]
                    st.rerun()
            
            with solve_col:
                if st.button("Solve", use_container_width=True, key=f"{key}_solve_btn"):
                    if st.session_state[f"{key}_items"]:
                        formatted_items = [(f"Item {item_id}", weight, value) 
                                         for item_id, weight, value in st.session_state[f"{key}_items"]]
                        st.session_state[f"{key}_formatted_items"] = formatted_items  # Store in session state
                        best_subset, best_value, all_valid_subsets = knapsack_function(
                            formatted_items, 
                            st.session_state[f"{key}_capacity"]
                        )
                        st.session_state[f"{key}_results"] = (best_subset, best_value, all_valid_subsets)
                        st.rerun()

    with right_col:
        if st.session_state.get(f"{key}_results"):
            best_subset, best_value, all_valid_subsets = st.session_state[f"{key}_results"]
            formatted_items = st.session_state[f"{key}_formatted_items"]
            # Display results table
            with st.container(border=True):
                # Table header
                subset_col, weight_col, value_col = st.columns(3)
                with subset_col:
                    st.subheader("Subset")
                with weight_col:
                    st.subheader("Total Weight")
                with value_col:
                    st.subheader("Total Value")
                # Display each subset row
                for subset, weight, value in all_valid_subsets:
                    subset_text = "∅" if not subset else ", ".join(subset)
                    row_col1, row_col2, row_col3 = st.columns(3)
                    is_optimal = subset == best_subset
                    background_color = "rgba(255, 200, 210, 0.3)" if is_optimal else "white"
                    with row_col1:
                        st.markdown(f'<div style="background-color: {background_color}; padding: 8px;">{subset_text}</div>', unsafe_allow_html=True)
                    with row_col2:
                        st.markdown(f'<div style="background-color: {background_color}; padding: 8px;">{weight}</div>', unsafe_allow_html=True)
                    with row_col3:
                        st.markdown(f'<div style="background-color: {background_color}; padding: 8px;">{value}</div>', unsafe_allow_html=True)
            # Display the solution message
            if best_subset:
                with st.container(border=True):
                    total_weight = sum(item[1] for item in formatted_items if item[0] in best_subset)
                    st.markdown(f"""
                    I found the optimal solution! The best combination is to take **{', '.join(best_subset)}**
                    with a total value of **{best_value}** and weight of **{total_weight}**.
                    """)

def tsp_form(key):
    input_col, output_col = st.columns([2, 3])
    with input_col:
        num_cities = st.number_input("Enter the number of cities", min_value=3, step=1, key=f"{key}_num_cities")
        if num_cities:
            # Initialize distances matrix in session state if not present or if num_cities changed
            if f"{key}_distances" not in st.session_state or len(st.session_state[f"{key}_distances"]) != num_cities:
                st.session_state[f"{key}_distances"] = [[0 if i == j else None for j in range(int(num_cities))] for i in range(int(num_cities))]

            with st.form(key=f"{key}_distance_form"):
                st.write("Enter the distances between each unique pair of cities:")
                pairs = [(i, j) for i in range(int(num_cities)) for j in range(i+1, int(num_cities))]
                max_cols = 4
                for row_start in range(0, len(pairs), max_cols):
                    row_pairs = pairs[row_start:row_start+max_cols]
                    cols = st.columns(max_cols)
                    for col_idx in range(max_cols):
                        if col_idx < len(row_pairs):
                            i, j = row_pairs[col_idx]
                            val = st.session_state[f"{key}_distances"][i][j] if st.session_state[f"{key}_distances"][i][j] is not None else 1
                            new_val = cols[col_idx].number_input(
                                f"City {i+1} → City {j+1}",
                                min_value=1,
                                step=1,
                                value=val,
                                key=f"{key}_{i}_{j}",
                                label_visibility="visible",
                                placeholder="0"
                            )
                            st.session_state[f"{key}_distances"][i][j] = new_val
                            st.session_state[f"{key}_distances"][j][i] = new_val
                        else:
                            cols[col_idx].empty()
                submitted = st.form_submit_button("Submit Distances")
                if submitted:
                    output_col.success("Distances updated! You can now solve the TSP.")
                    output_col.write(st.session_state[f"{key}_distances"])

def sequential_search_form(key, search_function):
    col1, col2 = st.columns([1, 3])
    with col1:
        list_generator = st.radio(
            "Select an option",
            ["Generate Random Values", "Enter Values Manually"],
            key=f"{key}_radio"
        )
        is_number_range = st.toggle(
            "Use Numbers",
            key=f"{key}_toggle_numbers"
        )

        input_values = ""
        list_length = 5

        if list_generator == "Generate Random Values":
            list_length = st.number_input(
                "Enter the length of the list",
                min_value=1,
                value=5,
                step=1,
                format="%d",
                key=f"{key}_number_input"
            )
        else:
            if is_number_range:
                input_values = st.text_input(
                    "Enter numbers separated by commas",
                    key=f"{key}_text_input_numbers"
                )
            else:
                input_values = st.text_input(
                    "Enter characters separated by commas",
                    key=f"{key}_text_input_chars"
                )

        # Generate button
        if st.button("Generate List", key=f"{key}_generate_btn"):
            list_values = []
            if list_generator == "Generate Random Values":
                if is_number_range:
                    list_values = [random.randint(1, 100) for _ in range(int(list_length))]
                else:
                    list_values = [chr(random.randint(65, 90)) for _ in range(int(list_length))]
            else:
                if input_values:
                    if is_number_range:
                        try:
                            list_values = [int(item.strip()) for item in input_values.split(",") if item.strip()]
                            if not list_values:
                                st.error("Please enter at least one valid number")
                                return
                        except ValueError:
                            st.error("Please enter valid numbers separated by commas")
                            return
                    else:
                        list_values = [item.strip() for item in input_values.split(",") if item.strip()]
                        if not list_values:
                            st.error("Please enter at least one character")
                            return
                else:
                    st.error("Please enter some values or choose 'Generate Random Values'")
                    return
            st.session_state[f"{key}_list_values"] = list_values

        # Show the generated list if present
        list_values = st.session_state.get(f"{key}_list_values", [])
        if list_values:
            st.write("List:")
            st.write(list_values)

        # Target input and search button (only if list is present)
        if list_values:
            search_target = st.text_input(
                "Enter the value to search for",
                key=f"{key}_search_target"
            )
            if st.button("Search", key=f"{key}_search_btn"):
                with col2.container(border=True):
                    if not search_target:
                        st.error("Please enter a value to search for.")
                        return
                    # Convert search_target to correct type
                    if is_number_range:
                        try:
                            target = int(search_target)
                        except ValueError:
                            st.error("Please enter a valid number to search for.")
                            return
                    else:
                        target = search_target.strip()
                    result = search_function(list_values, target)
                    if result is not None:
                        st.success(f"Value '{target}' found at index {result}.")
                    else:
                        st.warning(f"Value '{target}' not found in the list.")
        else:
            st.info("Generate a list first before searching.")


