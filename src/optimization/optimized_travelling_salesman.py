def tsp_optimized(listListDistanceMatrix, intStartCity):
    """
    Solve the Traveling Salesman Problem using dynamic programming with bit manipulation.
    
    Description:
    This function computes the shortest possible route that visits each city exactly once
    and returns to the origin city, using the Held-Karp algorithm.
    The time complexity is O(n²·2ⁿ) where n is the number of cities.
    
    Arguments:
        listListDistanceMatrix (list of lists): A square matrix where element [i][j] 
                                              represents the distance from city i to city j.
        intStartCity (int): The index of the starting city (0-indexed).
        
    Returns:
        tuple: A tuple containing:
            - list: The optimal path as a list of city indices (starting and ending with intStartCity)
            - int: The minimum total cost of the optimal path
            
    Example:
        >>> matrix = [
        ...     [0, 10, 15, 20],
        ...     [10, 0, 35, 25],
        ...     [15, 35, 0, 30],
        ...     [20, 25, 30, 0]
        ... ]
        >>> tsp_optimized(matrix, 0)
        ([0, 1, 3, 2, 0], 80)
    """
    # Input validation
    if not listListDistanceMatrix or not isinstance(listListDistanceMatrix, list):
        raise ValueError("listListDistanceMatrix must be a non-empty 2D list")

    intTotalCities = len(listListDistanceMatrix)
    for listRow in listListDistanceMatrix:
        if not isinstance(listRow, list) or len(listRow) != intTotalCities:
            raise ValueError("listListDistanceMatrix must be a square matrix")

    if not isinstance(intStartCity, int) or intStartCity < 0 or intStartCity >= intTotalCities:
        raise ValueError("intStartCity must be a valid index within the distance matrix")
    
    # Initialize DP array and path tracking array
    # dp[mask][city] = minimum cost to visit all cities in mask ending at city
    intTotalMasks = 1 << intTotalCities  # 2^n
    dpMinCost = [[999999 for _ in range(intTotalCities)] for _ in range(intTotalMasks)]
    dpPrevCity = [[None for _ in range(intTotalCities)] for _ in range(intTotalMasks)]
    
    # Base case: starting position
    dpMinCost[1 << intStartCity][intStartCity] = 0
    
    # Fill DP table using bottom-up approach
    for intMask in range(1, intTotalMasks):
        # Skip if starting city is not in the subset
        if not (intMask & (1 << intStartCity)):
            continue
            
        # For each city in the current subset
        for intCurrentCity in range(intTotalCities):
            # Skip if current city is not in the subset
            if not (intMask & (1 << intCurrentCity)):
                continue
                
            # Calculate the subset without the current city
            intPrevMask = intMask ^ (1 << intCurrentCity)
            
            # Skip if prev_mask is empty (only happens when current city is start city and mask only contains start city)
            if intPrevMask == 0:
                continue
                
            # Try all possible previous cities
            for intPrevCity in range(intTotalCities):
                # Skip if previous city is not in the subset or is the same as current city
                if not (intPrevMask & (1 << intPrevCity)) or intPrevCity == intCurrentCity:
                    continue
                    
                # Calculate new cost
                intNewCost = dpMinCost[intPrevMask][intPrevCity] + listListDistanceMatrix[intPrevCity][intCurrentCity]
                
                # Update if better
                if intNewCost < dpMinCost[intMask][intCurrentCity]:
                    dpMinCost[intMask][intCurrentCity] = intNewCost
                    dpPrevCity[intMask][intCurrentCity] = intPrevCity
    
    # Find optimal last city before returning to start
    intFinalMask = (1 << intTotalCities) - 1  # Bitmask with all cities visited
    intMinCost = 999999
    intLastCity = None
    
    for intCity in range(intTotalCities):
        if intCity == intStartCity:
            continue
            
        intTotalCost = dpMinCost[intFinalMask][intCity] + listListDistanceMatrix[intCity][intStartCity]
        if intTotalCost < intMinCost:
            intMinCost = intTotalCost
            intLastCity = intCity
    
    # Reconstruct the path
    if intLastCity is None:
        return [intStartCity], 0  # Only one city
    
    # Build the path backwards
    listIntPath = [intStartCity]
    intCurrentCity = intLastCity
    intCurrentMask = intFinalMask
    
    while intCurrentCity != intStartCity:
        listIntPath.insert(1, intCurrentCity)  # Insert at position 1 to build path in correct order
        intTempCity = dpPrevCity[intCurrentMask][intCurrentCity]
        intCurrentMask ^= (1 << intCurrentCity)  # Remove current city from mask
        intCurrentCity = intTempCity
    
    return listIntPath, intMinCost


# Example usage
if __name__ == "__main__":
    # Sample distance matrix
    listListMatrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Test the implementation
    listIntPath, intCost = tsp_optimized(listListMatrix, 0)
    print("Best Path:", listIntPath)
    print("Minimum Cost:", intCost)