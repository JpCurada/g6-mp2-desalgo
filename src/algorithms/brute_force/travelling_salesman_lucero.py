def tsp_unoptimized(listListDistanceMatrix, intStartCity):
    """
    Solve the Traveling Salesman Problem using a recursive brute force approach.
    
    Description:
    This function finds the shortest possible route that visits each city exactly once
    and returns to the origin city, using a recursive exhaustive search algorithm.
    The time complexity is O(n!) where n is the number of cities.
    
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
        >>> tsp_unoptimized(matrix, 0)
        ([0, 1, 3, 2, 0], 80)
    """
    def tsp_helper(listBoolVisitedCities, intCurrentCity, intTotalCities, intCurrentCost, listListDistanceMatrix, intStartCity, listIntPath):
        """
        Recursive helper function to solve the TSP problem.
        
        Arguments:
            listBoolVisitedCities (list of bool): Boolean array where listBoolVisitedCities[i] is True if city i has been visited.
            intCurrentCity (int): The current city being visited.
            intTotalCities (int): Total number of cities in the problem.
            intCurrentCost (int): The cumulative cost of the path so far.
            listListDistanceMatrix (list of lists): The distance matrix between cities.
            intStartCity (int): The city from which the journey starts and must end.
            listIntPath (list of int): The path traversed so far.
            
        Returns:
            tuple: A tuple containing:
                - list: The best path found from the current state
                - int: The minimum cost of that path
        """
        if all(listBoolVisitedCities):
            return listIntPath + [intStartCity], intCurrentCost + listListDistanceMatrix[intCurrentCity][intStartCity]
        
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

    listBoolVisitedCities = [False] * intTotalCities
    listBoolVisitedCities[intStartCity] = True
    return tsp_helper([True if i == intStartCity else False for i in range(intTotalCities)], intStartCity, intTotalCities, 0, listListDistanceMatrix, intStartCity, [intStartCity])


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
    listIntPath, intCost = tsp_unoptimized(listListMatrix, 0)
    print("Best Path:", listIntPath)
    print("Minimum Cost:", intCost)