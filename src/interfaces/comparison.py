import streamlit as st

def comparison():
    st.title("Comparison")

    st.header("Algorithms Comparisons")

    # Example: Markdown table for comparison (simplified for clarity)
    st.markdown("""
| Algorithm                | Strengths                                         | Weaknesses                                         | Real-World Applications                |
|--------------------------|---------------------------------------------------|----------------------------------------------------|----------------------------------------|
| Selection Sort           | Simple, easy to implement, constant memory        | Inefficient on large data, unstable, not adaptive  | Small leaderboards, embedded systems   |
| Bubble Sort              | Easy to grasp, stable, no extra memory            | Inefficient, many swaps, poor scalability          | Sorting playlists, visual demos        |
| Sequential Search        | Works on unsorted data, simple, no extra memory   | Inefficient on large data, slow                    | Contact search, file lookup            |
| Traveling Salesman (TSP) | Simple concept, optimal for small graphs          | NP-hard, exponential time, poor scalability        | Routing, tour planning, circuit design |
| Knapsack Problem         | Straightforward, optimal with DP/greedy           | NP-complete, expensive for large data              | Portfolio optimization, resource alloc |
""")

    st.header("Time Complexity Analysis")

    st.subheader("Selection Sort")
    st.write("Iteratively selects the minimum element from the unsorted portion and swaps it with the beginning element.")
    st.latex(r"\text{Best, Average, Worst Case: } O(n^2)")
    st.code(
        """for i in range(len(arr)):               
    intMinIndex  = i                    
    for j in range(i + 1, len(arr)):    
        a = arr[j].lower() if isinstance(arr[j], str) else arr[j]
        b = arr[intMinIndex].lower() if isinstance(arr[intMinIndex], str) else arr[intMinIndex]
        if a < b:
            intMinIndex = j
    if intMinIndex != i:
        arr[i], arr[intMinIndex] = arr[intMinIndex], arr[i]
return arr"""
    )

    st.subheader("Bubble Sort")
    st.write("Repeatedly swaps the adjacent elements if they are in the wrong position.")
    st.latex(r"\text{Best Case: } O(n) \qquad \text{Average/Worst Case: } O(n^2)")
    st.code(
        """for i in range(intSize): 
    for j in range(0, intSize - i - 1):
        if listInput[j] > listInput[j+1]:
            listInput[j], listInput[j+1] = listInput[j+1], listInput[j]"""
    )

    st.subheader("Sequential Search")
    st.write("Iterates through the dataset and checks whether the target value exists.")
    st.latex(r"\text{Best Case: } O(1) \qquad \text{Average/Worst Case: } O(n)")
    st.code(
        """def search(arrArray, intTarget):
    for i in range(len(arrArray)):
        if arrArray[i] == intTarget:
            return True
    return False"""
    )

    st.subheader("Traveling Salesman Problem (TSP)")
    st.write("Recursively finds the shortest possible route that visits each city exactly once and returns to the origin city.")
    st.latex(r"\text{Best, Average, Worst Case: } O(n!)")
    st.latex(r"\text{Number of combinations: } (n-1)!")

    st.subheader("Knapsack Problem")
    st.write("Given n items with weights and values, and a capacity, find the most valuable subset that fits.")
    st.latex(r"\text{Best, Average, Worst Case: } O(2^n)")
    st.latex(r"\text{Number of combinations: } 2^n - 1")