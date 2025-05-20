import streamlit as st

def analysis():
    st.title("Algorithm Analysis")

    selection, bubble, linear, tsp, kp  = st.tabs(["Selection Sort", "Bubble Sort", "Sequential Search", 
                                                   "Traveling Salesman Problem", "Knapsack Problem"])
    
    with selection:     
        st.subheader("Time Complexity Analysis")
        st.markdown("""
            Iteratively selects the minimum element from the unsorted portion and swaps it in the beginning element.
                    
            **Best Case:** O(n²) - Occurs when the array provided is already sorted \n 
            **Average Case:** O(n²) - Arises when the elements in the array are in a random order \n   
            **Worst Case:** O(n²) - Occurs when the array must be in ascending order but the array is in descending order or vice versa 
        """)
        codeCol1, descripCol1 = st.columns(2, gap="small")
        with codeCol1:
            st.code(
                body="""
                    for i in range(len(arr)):               
                        intMinIndex  = i                    
                        for j in range(i + 1, len(arr)):    
                            a = arr[j].lower() if isinstance(arr[j], str) else arr[j]
                            b = arr[intMinIndex].lower() if isinstance(arr[intMinIndex], str) else arr[intMinIndex]
                            if a < b:
                                intMinIndex = j
                        if intMinIndex != i:
                            arr[i], arr[intMinIndex] = arr[intMinIndex], arr[i]
                    return arr
                """,
                language="python",
                line_numbers=True
            )
       
        with descripCol1:
            col1, col2 = st.columns(2, gap="small")
            with col1:
                st.markdown("""
                    Calculate the Time Complexity of each Operations \n
                        Line 1:  1 + n = n  
                        Line 2: 1 
                        Line 3: n * n = n² 
                        Line 4, Line 5:  1 
                        Line 7, Line 8: 1
                        Line 9, Line 10: 1 
                """)
            with col2: 
                st.markdown("""
                        Add up all the Big O of each operations \n 
                            = n + 1 + n² + 1 + 1 + 1 \n
                            = n² + n + 4 \n
                        Remove Constant, Choose the Higher Order Term \n
                            = n² \n
                            = O(n²)
                """)
        
    with bubble: 
        st.subheader("Time Complexity Analysis")
        st.markdown("""
            Repeatedly swaps the adjacenet elements if they are in the wrong position.
                    
            **Best Case:** O(n) - Occurs when the array is already sorted\n
            **Average Case:** O(n²) - Arises when the array is in random or irrespective arrangement of elements\n 
            **Worst Case:** O(n²) - Occurs when the array must be in ascending order but the array is in descending order or vice versa\n 
        """)
        codeCol2, descripCol2 = st.columns(2, gap="small")
        with codeCol2:
            st.code(
                body="""
                for i in range(intSize): 
                for j in range(0, intSize - i - 1):
                    if listInput[j] > listInput[j+1]:
                        listInput[j], listInput[j+1] = listInput[j+1], listInput[j]
                """,
                language="python",
                line_numbers=True
            )
            st.write("""
                    Calculate the Time Complexity of each Operations \n 
                        Line 1: 1 
                        Line 2: 1 + n = n 
                        Line 3: n * n = n² 
                        Line 4: n² 
                        Line 5: n² 
                """)       

        with descripCol2:
                st.markdown("""
                    Add up all the Big O of each operations \n 
                        = 1 + 1 + n + n² + n² + n² 
                        = 3n² + n + 2
                    Remove Constant, Choose the Higher Order Term \n
                        = n² + n + 2
                        = n² 
                        = O(n²) 
                """)
    with linear:
        st.subheader("Time Complexity Analysis")
        st.markdown("""
            Iterates through the dataset and checks whether the target value exists.
                    
            **Best Case:** O(1) - If the target value is in the beginning of the array \n
            **Average Case:** O(n) - Arises when the target value is in a random placement or in the middle of the array\n 
            **Worst Case:** O(n) - Occurs when the target value is in the last index of the array \n 
        """)
        codeCol3, descripCol3 = st.columns(2, gap="small")
        with codeCol3:
            st.code(
                body="""
                def search(arrArray, intTarget):
                    for i in range(len(arrArray)):
                        if arrArray[i] == intTarget:
                            return True
                    return False
                """,
                language="python",
                line_numbers=True
            )
            st.write("""   
                Calculate the Time Complexity of each Operations \n 
                    Line 2: 1 + n = n 
                    Line 3: 1 * n = n 
                    Line 4: 1 
                    Line 5: 1 
            """)
        
        with descripCol3:
            st.markdown("""
                Add up all the Big O of each operations \n 
                    = n + n + 1 + 1 
                    = 2n + 2 
                Remove Constant, Choose the Higher Order Term \n
                    = n
                    = O(n) 
            """)
         
    with tsp:
        st.subheader("Time Complexity Analysis")
        st.markdown("""
            Recursively finds the shortest path possible route that visits each city exactly once and returns to the origin city.  
                    
            The given must be a complete graph wherein each vertex must be connected to every other vertex. Brute force approach 
            generate all the permutations of each node then calculate cost of each permutation and select the minimum cost among 
            the permutations.

            **Best Case:** O(n!) - Factorial \n
            **Average Case:** O(n!) - Factorial \n 
            **Worst Case:** O(n!) - Factorial
        """)
        st.markdown("""
            Formula in finding the number of combinations in the traveling salesman problem. \n 
                = (n - 1)!
            For example: \n
                n = 5
            Where n is the number of vertices or cities in the graph since, the algorithm utilizes combination to generate all 
                all the possible permutations in the vertex set.\n
                = (5 - 1)!
                = (4)!
                = 4 * 3 * 2 * 1
                = 24 possible combinations
            To get the time complexity, we just need to remove the constant and get the higher order term. \n
                = (n - 1)!
                = (n)!
                = O(n!)
        """)        
        
        st.code(
            body="""
                def tsp_unoptimized(listListDistanceMatrix, intStartCity):
                        def tsp_helper(listBoolVisitedCities, intCurrentCity, intTotalCities, intCurrentCost, listListDistanceMatrix, intStartCity, listIntPath):
                            
                            intMinCost = 999999
                            listIntBestPath = []
                            for intNextCity in range(intTotalCities):
                                if not listBoolVisitedCities[intNextCity]:
                                    listBoolVisitedCities[intNextCity] = True
                                    listIntUpdatedPath, intNewCost = tsp_helper(
                                        listBoolVisitedCities,
                                        intNextCity,
                                        intTotalCities,
                                        intCurrentCost + listListDistanceMatrix[intCurrentCity][intNextCity],
                                        listListDistanceMatrix,
                                        intStartCity,
                                        listIntPath + [intNextCity]
                                    )
                                    if intNewCost < intMinCost:
                                        intMinCost = intNewCost
                                        listIntBestPath = listIntUpdatedPath
                                    listBoolVisitedCities[intNextCity] = False
                            return listIntBestPath, intMinCost

                        if not listListDistanceMatrix or not isinstance(listListDistanceMatrix, list):
                            raise ValueError("listListDistanceMatrix must be a non-empty 2D list")

                        intTotalCities = len(listListDistanceMatrix)
                        for listRow in listListDistanceMatrix:
                            if not isinstance(listRow, list) or len(listRow) != intTotalCities:
                                raise ValueError("listListDistanceMatrix must be a square matrix")

                        if not isinstance(intStartCity, int) or intStartCity < 0 or intStartCity >= intTotalCities:
                            raise ValueError("intStartCity must be a valid index within the distance matrix")

                        return tsp_helper([True if i == intStartCity else False for i in range(intTotalCities)], intStartCity, intTotalCities, 0, listListDistanceMatrix, intStartCity, [intStartCity])
                        listBoolVisitedCities = [False] * intTotalCities
                        listBoolVisitedCities[intStartCity] = True
                """,
                language="python",
                line_numbers=True
            )

    with kp:
        st.subheader("Time Complexity Analysis")
        st.markdown("""
            Given n items where each item has an equivalent weight and value, and a capacity, find the most valuable subset of the items that can fit into the knapsack.  

            **Best Case:** O$(2^n)$ — Exponential time  
            **Average Case:** O$(2^n)$ — Exponential time  
            **Worst Case:** O$(2^n)$ — Exponential time, the combinations are checked recursively. The number of computations doubles for each extra item that needs to be considered.
        """)

        st.markdown("""
            Given: \n
                n = item
                w[i] = weight of the item 
                v[i] = value of the item
                w = knapsack capacity
            Using the brute-force approach, we must try all the possible subsets of n. Each item has a chance to be included or excluded in the knapsack. \n 
            The formula to find the number of combinations:\n 
        """)

        st.markdown("= $2^n$ - 1")
        st.markdown("To get the time complexity, we just need to remove the constant and get the higher order term.")
        st.markdown("= $2^n$")
        st.markdown("= O$(2^n)$")

        st.code(
            body="""
                def knapsack_brute_force(items, max_capacity):
                
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
            """,
            language="python",
            line_numbers=True
        )
    
        st.write("""

        """)