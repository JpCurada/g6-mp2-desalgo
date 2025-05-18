import streamlit as st
import random

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
        st.write("This is the bubble sort page.")
        list_generator = st.radio("Select an option", ["Generate Random Values", "Enter Values Manually"])

        list_values = []

        if list_generator == "Generate Random Values":
            list_length = st.number_input("Enter the length of the list", min_value=1, step=1, format="%d")
            if list_length:
                # Generate random integers between -100 and 100
                list_values = [random.randint(-100, 100) for _ in range(int(list_length))]
        elif list_generator == "Enter Values Manually":
            input_str = st.text_input("Enter the values separated by commas")
            if input_str:
                try:
                    list_values = [int(num.strip()) for num in input_str.split(",") if num.strip()]
                except ValueError:
                    st.error("Please enter only integers separated by commas.")

        st.write(list_values)

    with select_tab:
        st.write("This is the selection sort page.")
    with search_tab:
        st.write("This is the sequential search page.")
    with knap_tab:
        st.write("This is the knapsack problem page.")
    with tsp_tab:
        st.write("This is the travelling salesman problem page.")

