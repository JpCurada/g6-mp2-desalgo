import streamlit as st
from utils.components import sorting_form, item_adder, knapsack_form, tsp_form, sequential_search_form
<<<<<<< HEAD
from algorithms.brute_force_test import bubble_sort, selection_sort, knapsack_brute_force

def sequential_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return None
=======

from algorithms.brute_force import bubble_sort, selection_sort, linear_search, knapsack_problem, travelling_salesman

>>>>>>> 944376154df1e63de6ba480580b7fbbf05e3ee19

def brute_force_page():
    st.title("Brute Force Algorithms")

    bubble_tab, select_tab, search_tab, knap_tab, tsp_tab = st.tabs([
        "Bubble Sort",
        "Selection Sort", 
        "Sequential Search",
        "Knapsack Problem",
        "Travelling Salesman"
    ])

    with bubble_tab:
        sorting_form(key="bubble_sort", sorting_function=bubble_sort)

    with select_tab:
        sorting_form(key="selection_sort", sorting_function=selection_sort)

    with search_tab:
<<<<<<< HEAD
        sequential_search_form(key="sequential_search", search_function=sequential_search)

    with knap_tab:
        knapsack_form(key="knapsack", knapsack_function=knapsack_brute_force)

    with tsp_tab:
        tsp_form(key="tsp")
=======
        sequential_search_form(key="sequential_search", search_function=linear_search)

    with knap_tab:
        knapsack_form(key="knapsack", knapsack_function=knapsack_problem)

    with tsp_tab:
        tsp_form(key="tsp", tsp_function=travelling_salesman)
>>>>>>> 944376154df1e63de6ba480580b7fbbf05e3ee19

                        

