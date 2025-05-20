import streamlit as st

def home_page():
    st.title("Machine Problem II")
    
    # Centered badges using your provided Markdown
    st.markdown(
        """
        <br>
        <div style='text-align: center;'>
            <a href="https://www.python.org/downloads/release/python-311/">
                <img src="https://img.shields.io/badge/Python-3.11-blue.svg" alt="Python 3.11"/>
            </a>
            <a href="https://streamlit.io">
                <img src="https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg" alt="Streamlit"/>
            </a>
            <a href="https://github.com/JpCurada/g6-mp2-desalgo">
                <img src="https://img.shields.io/badge/View%20on-GitHub-green.svg" alt="GitHub"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.header("Brute Force Algorithms: Review and Implementation")
    
    # Group Members
    st.subheader("Group VI Members")
    st.markdown(
        """
        - CURADA, John Paul M.
        - ZARAGOZA, Marie Criz
        - LUCERO, Ken Audie S.
        - FAELDONIA, Elias Von Isaac R.
        - OJA, Ma. Izabelle L.
        - RACELIS, Michael Richmond V.
        - CANSINO, Florence Lee F.
        - RAMILO, Gian G.
        - MAGTANONG, Gabriel Andre E.
        """
    )


    st.markdown(
        """
        This application presents a comprehensive review and implementation of Brute Force algorithms, developed by Group VI for the Machine Problem 2 assignment in Design and Analysis of Algorithms. The project is built using Python 3.11 and Streamlit, with the source code available on GitHub.
        """
    )
    
    # Introduction Section
    with st.expander("I. Introduction", expanded=True):
        st.markdown(
            """
            ### Brute Force Strategy
            
            Brute Force is a straightforward algorithmic approach that systematically explores all possible solutions to find the correct one. This method involves generating and testing each potential solution until reaching a satisfactory result.
            
            The strategy is characterized by:
            - Simplicity in concept and implementation
            - Guaranteed correctness when an optimal solution exists
            - Exhaustive exploration of the solution space
            - Generally higher computational cost compared to optimized algorithms
            
            While brute force approaches are often inefficient for large problem instances, they serve as:
            1. A baseline for algorithm performance comparison
            2. A verification tool for more sophisticated algorithms
            3. An effective approach for small-scale problems
            4. A starting point for understanding complex algorithmic concepts
            
            This document reports on the implementation, analysis, and optimization of five key brute force algorithms, providing insights into their behavior, complexity, and real-world applications.
            """
        )
    
    # Brute Force Algorithms Section
    with st.expander("II. Brute Force Algorithms"):
        st.markdown(
            """
            ### Overview of Implemented Algorithms
            
            This section provides an introduction to each of the implemented brute force algorithms:
            """
        )
        
        # Selection Sort
        st.subheader("Selection Sort")
        st.markdown(
            """
            Selection Sort is an in-place comparison sorting algorithm that divides the input into a sorted and unsorted region. The algorithm repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the sorted region.
            
            **Key Characteristics:**
            - Simple implementation with nested loops
            - Inefficient for large datasets
            - Performs the same number of comparisons regardless of input arrangement
            - In-place algorithm with O(1) auxiliary space
            """
        )
        
        # Bubble Sort
        st.subheader("Bubble Sort")
        st.markdown(
            """
            Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until no swaps are needed.
            
            **Key Characteristics:**
            - Straightforward implementation
            - Performs poorly on large datasets
            - Can detect if the list is already sorted (with optimization)
            - Stable sorting algorithm that preserves the relative order of equal elements
            """
        )
        
        # Sequential Search
        st.subheader("Sequential Search")
        st.markdown(
            """
            Sequential Search (Linear Search) is a method for finding a target value within a list by checking each element sequentially until the target is found or the list is exhausted.
            
            **Key Characteristics:**
            - Simple and applicable to unsorted collections
            - Time complexity increases linearly with collection size
            - No prerequisite on data arrangement
            - Inefficient for large datasets compared to binary search on sorted data
            """
        )
        
        # Traveling Salesman Problem
        st.subheader("Traveling Salesman Problem")
        st.markdown(
            """
            The Traveling Salesman Problem (TSP) aims to find the shortest possible route that visits each city exactly once and returns to the origin city. The brute force approach evaluates all possible permutations of cities.
            
            **Key Characteristics:**
            - NP-hard problem with factorial time complexity
            - Guarantees the optimal solution
            - Becomes computationally intractable for more than a small number of cities
            - Serves as a benchmark for approximation algorithms
            """
        )
        
        # Knapsack Problem
        st.subheader("Knapsack Problem")
        st.markdown(
            """
            The Knapsack Problem involves selecting items with given weights and values to maximize total value while keeping the total weight within a specified limit. The brute force approach evaluates all possible combinations of items.
            
            **Key Characteristics:**
            - Combinatorial optimization problem
            - Exponential time complexity
            - Guarantees the optimal solution
            - Demonstrates the concept of trade-offs between resources
            """
        )
    
    # Time Complexity Analysis
    with st.expander("III. Analysis of Time Complexity"):
        st.markdown(
            """
            ### Time Complexity Analysis
            
            This section analyzes the time complexity of each implemented brute force algorithm:
            
            | Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
            |-----------|-----------|--------------|------------|------------------|
            | Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
            | Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
            | Sequential Search | O(1) | O(n/2) | O(n) | O(1) |
            | Traveling Salesman | O(n!) | O(n!) | O(n!) | O(n) |
            | Knapsack Problem | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) | O(n) |
            
            Each algorithm's time complexity is derived from analyzing its fundamental operations:
            
            - **Selection Sort**: Uses nested loops to find the minimum element and place it in the correct position, resulting in quadratic time complexity regardless of input arrangement.
            
            - **Bubble Sort**: Performs repeated passes through the list, potentially requiring fewer iterations if the list becomes sorted early, but still has worst-case quadratic complexity.
            
            - **Sequential Search**: Examines elements one by one until finding the target, yielding linear worst-case complexity when the target is at the end or absent.
            
            - **Traveling Salesman Problem**: Examines all possible permutations of cities, resulting in factorial time complexity that grows extremely rapidly with the number of cities.
            
            - **Knapsack Problem**: Evaluates all possible item combinations, leading to exponential time complexity based on the number of items.
            
            The detailed analysis provides insights into algorithmic efficiency and the computational challenges associated with brute force approaches.
            """
        )
    
    # Algorithms Comparison
    with st.expander("IV. Algorithms Comparison"):
        st.markdown(
            """
            ### Comparative Analysis
            
            This section presents a comparative analysis of the implemented brute force algorithms:
            
            **Selection Sort:**
            - **Strengths**: Simple implementation, performs well on small lists, minimal space requirements
            - **Weaknesses**: Inefficient for large datasets, always performs O(n²) comparisons
            - **Real-world Applications**: Educational purposes, embedded systems with limited memory, small dataset sorting
            
            **Bubble Sort:**
            - **Strengths**: Simple implementation, detects already sorted arrays
            - **Weaknesses**: Poor performance on large or nearly sorted datasets
            - **Real-world Applications**: Educational purposes, detecting small errors in almost-sorted arrays
            
            **Sequential Search:**
            - **Strengths**: Works on unsorted data, simple implementation
            - **Weaknesses**: Slow for large datasets
            - **Real-world Applications**: Finding items in small lists, searching unsorted data, verifying presence of elements
            
            **Traveling Salesman Problem:**
            - **Strengths**: Guarantees optimal solution, conceptually straightforward
            - **Weaknesses**: Exponential growth in computation time, impractical for many cities
            - **Real-world Applications**: Route planning, logistics optimization, circuit board drilling
            
            **Knapsack Problem:**
            - **Strengths**: Guarantees optimal solution, handles distinct item valuations
            - **Weaknesses**: Exponential time complexity, impractical for many items
            - **Real-world Applications**: Resource allocation, investment decisions, cargo loading
            
            The comparative analysis shows that while brute force algorithms offer simplicity and guaranteed correctness, they generally face scalability challenges for real-world problems with large inputs.
            """
        )
    
    # Optimization Techniques
    with st.expander("V. Optimization Techniques"):
        st.markdown(
            """
            ### Optimization Approaches
            
            This section explores various optimization techniques that can improve the performance of brute force algorithms:
            
            **Selection Sort Optimizations:**
            - Bidirectional Enhanced Selection Sort: Finds both minimum and maximum in each pass
            - Early termination when the array becomes sorted
            
            **Bubble Sort Optimizations:**
            - Cocktail Shaker Sort: Bidirectional bubble sort that can reduce the number of iterations
            - Comb Sort: Improving bubble sort by using gap sequence to eliminate turtles (small values near the end)
            
            **Sequential Search Optimizations:**
            - Self-Organizing List: Moving frequently accessed elements toward the front
            - Sentinel Linear Search: Eliminating the boundary check in each iteration
            
            **Traveling Salesman Problem Optimizations:**
            - Dynamic Programming: Breaking down into overlapping subproblems
            - Branch and Bound: Pruning paths that cannot lead to optimal solutions
            
            **Knapsack Problem Optimizations:**
            - Dynamic Programming: Using a table to store results of subproblems
            - Greedy Approach: Selecting items based on value-to-weight ratio
            
            Each optimization technique represents a trade-off between implementation complexity and performance improvement. The most effective approach depends on specific use cases and constraints.
            """
        )
    
    # Findings and Conclusion
    with st.expander("VI. Findings and Conclusion"):
        st.markdown(
            """
            ### Key Findings
            
            The implementation and analysis of brute force algorithms revealed several important insights:
            
            1. **Performance Limitations**: Brute force approaches face significant performance challenges with large inputs due to their high time complexity
            
            2. **Optimization Impact**: Simple optimizations can dramatically improve practical performance while maintaining algorithm correctness
            
            3. **Problem Characteristics**: The effectiveness of brute force varies greatly based on problem characteristics and input size
            
            4. **Educational Value**: Implementing brute force algorithms provides a strong foundation for understanding more complex algorithmic concepts
            
            ### Conclusion
            
            Understanding brute force algorithms is essential for several reasons:
            
            - They provide a baseline for algorithm performance comparison
            - They serve as stepping stones to more sophisticated algorithmic approaches
            - They guarantee finding the optimal solution when it exists
            - They demonstrate fundamental computer science concepts like time complexity and algorithmic efficiency
            
            This project has demonstrated the implementation, analysis, and optimization of key brute force algorithms, highlighting both their utility and limitations. While brute force approaches may not always be practical for large-scale problems, they remain valuable tools in the algorithmic toolkit and provide crucial insights into computational problem-solving.
            
            The optimization techniques explored in this project further illustrate how understanding algorithm fundamentals enables the development of more efficient solutions while managing the inherent trade-offs between simplicity, correctness, and performance.
            """
        )
    
    st.markdown("The source code for this project is available on [GitHub](https://github.com/JpCurada/g6-mp2-desalgo).")
    
