import streamlit as st
from utils.components import sorting_form, item_adder, knapsack_form, tsp_form, sequential_search_form
from algorithms.optimized import (optimized_bubble_sort, optimized_linear_search, optimized_selection_sort, knapsack_optimize, fnTSPOptimized,
                                  branch_and_bound_tsp, dynamic_programming_knapsack, fnSelfOrganizingSearch, comb_sort, bidirectional_enhanced_selection_sort)


def optimized_page():
    st.title("Optimized Algorithms")
    st.write("This is the optimized algorithms page.")

    bubble_tab, select_tab, search_tab, knap_tab, tsp_tab = st.tabs([
        "Bubble Sort",
        "Selection Sort", 
        "Sequential Search",
        "Knapsack Problem",
        "Travelling Salesman"
    ])

    with bubble_tab:
        bb_options = {
            "Comb Sort": comb_sort,
            "Cocktail Shaker Sort": optimized_bubble_sort.fnBubbleSortOptimized
        }

        # Bubble Sort
        bb_sorting_options = ["Comb Sort", "Cocktail Shaker Sort"]
        selected_optimized_bb_algo = st.segmented_control(
            "Choose optimized algorithms", bb_sorting_options, selection_mode="single", key="bubble_sort"
        )

        if selected_optimized_bb_algo:
            sorting_form(key="bubble_sort", sorting_function=bb_options[selected_optimized_bb_algo])

    # Selection Sort
    with select_tab:
        ss_options = {
            "Bidirectional Enhanced Selection Sort": bidirectional_enhanced_selection_sort,
            "Optimized Selection Sort": optimized_selection_sort.fnSelectionSortOptimized
        }

        # Selection Sort
        ss_sorting_options = ["Bidirectional Enhanced Selection Sort", "Optimized Selection Sort"]
        selected_optimized_ss_algo = st.segmented_control(
                "Choose optimized algorithms", ss_sorting_options, selection_mode="single", key="selection_sort"
        )

        if selected_optimized_ss_algo:
            sorting_form(key="selection_sort", sorting_function=ss_options[selected_optimized_ss_algo])

    # Search 
    with search_tab:
        search_options = {
            "Optimized Linear Search": optimized_linear_search.fnSentinelLinearSearch,
            "Self Organizing List": fnSelfOrganizingSearch
        }

        # Selection Sort
        search_sorting_options = ["Optimized Linear Search", "Self Organizing List"]
        selected_optimized_search_algo = st.segmented_control(
                "Choose optimized algorithms", search_sorting_options, selection_mode="single", key="search"
        )

        if selected_optimized_search_algo:
            sequential_search_form(key="search", search_function=search_options[selected_optimized_search_algo])

    # Knapsack Problem
    with knap_tab:
        knapsack_options = {
            "Dynamic Programming for Knapsack": dynamic_programming_knapsack,
            "Knapsack Optimized": knapsack_optimize
        }

        # Knapsack Problem
        knap_sorting_options = ["Dynamic Programming for Knapsack", "Knapsack Optimized"]
        selected_optimized_knap_algo = st.segmented_control(
                "Choose optimized algorithms", knap_sorting_options, selection_mode="single", key="knapsack"
        )

        if selected_optimized_knap_algo:
            knapsack_form(key="knapsack", knapsack_function=knapsack_options[selected_optimized_knap_algo]) 

    # Travelling Salesman Problem
    with tsp_tab:
        tsp_options = {
            "Dynamic Programming for TSP": fnTSPOptimized,
            "Branch and Bound": branch_and_bound_tsp
        }

        # Travelling Salesman Problem
        tsp_sorting_options = ["Dynamic Programming for TSP", "Branch and Bound"]
        selected_optimized_tsp_algo = st.segmented_control(
                "Choose optimized algorithms", tsp_sorting_options, selection_mode="single", key="tsp"
        )

        if selected_optimized_tsp_algo:
            tsp_form(key="tsp", tsp_function=tsp_options[selected_optimized_tsp_algo])
        

                        

