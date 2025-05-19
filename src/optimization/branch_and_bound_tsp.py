class Node:
    """
    This represents a node in the search tree for the branch and bound TSP algorithm. It stores the current path, reduced cost matrix, total cost, current vertex, and level in the tree.
    """
    def __init__(self, path, reduced_matrix, cost, vertex, level):
        self.path = path
        self.reduced_matrix = reduced_matrix
        self.cost = cost
        self.vertex = vertex
        self.level = level

def copy_matrix(matrix):
    """
    This creates and returns a copy of a 2D matrix. To ensures that modifications to the new matrix do not affect the original.
    
    Args:
        matrix (list of list of float): The matrix to copy.

    Returns:
        list of list of float: The copied matrix.
    """
    return [row[:] for row in matrix]

def reduce_matrix(matrix):
    """
    This reduces the given cost matrix by subtracting the minimum value from each row and column and returns the total reduction cost, which is used as a lower bound in the branch and bound algorithm.
    
    Args:
        matrix (list of list of float): The cost matrix to reduce.

    Returns:
        float: The sum of all reductions (lower bound cost).
    """

    length = len(matrix)
    INFINITE = float('inf')

    #decrease the row
    row_min = [min([matrix[i][j] if matrix[i][j] != INFINITE else INFINITE for j in range(length)]) for i in range(length)]

    for i in range(length):
        if(row_min[i] != INFINITE and row_min[i] > 0):
            for j in range(length):
                if (matrix[i][j] != INFINITE):
                    matrix[i][j] -= row_min[i]
    
    #decrease the column
    col_min = [min([matrix[j][i] if matrix[j][i] != INFINITE else INFINITE for j in range(length)]) for i in range(length)]

    for i in range(length):
        if(col_min[i] != INFINITE and col_min[i] > 0):
            for j in range(length):
                if (matrix[j][i] != INFINITE):
                    matrix[j][i] -= col_min[i]

    cost = sum([value for value in row_min if value != INFINITE]) + sum([value for value in col_min if value != INFINITE])
    return cost

def get_min_node(priority):
    """
    This finds and removes the node with the lowest cost from the priority list and this simulates a priority queue for the branch and bound algorithm.
    
    Args:
        priority (list of Node): The list of nodes to search.

    Returns:
        Node: The node with the minimum cost.
    """

    min_index = 0
    for i in range(1, len(priority)):
        if(priority[i].cost < priority[min_index].cost):
            min_index = i
    return priority.pop(min_index)

def calculate_path_cost(path, cost_matrix):
    """
    Calculates the total cost of a given path based on the provided cost matrix.

    Args:
        path (list of int): The sequence of vertices representing the path.
        cost_matrix (list of list of float): The cost matrix representing the graph.

    Returns:
        float: The total cost of traversing the given path.
    """
        
    total = 0
    for i in range(len(path) - 1):
        total += cost_matrix[path[i]][path[i + 1]]
    return total

def branch_and_bound_tsp(cost_matrix):
    """
    This is the main function that solves the Traveling Salesman Problem using the branch and bound method and returns the minimum cost and the best path found.
    
    Args:
        cost_matrix (list of list of float): The cost matrix representing the graph.
        
    Returns:
        tuple: (minimum cost, best path as a list of vertices)
    """
    length = len(cost_matrix)
    INFINITE = float('inf')
    priority = []

    initial_matrix = copy_matrix(cost_matrix)
    cost = reduce_matrix(initial_matrix)
    root = Node(path = [0], reduced_matrix = initial_matrix, cost = cost, vertex = 0, level = 0)
    priority.append(root)
    min_cost = INFINITE
    best_path = []

    while priority:
        min_node = get_min_node(priority)
        if min_node.level == length - 1:
            last = min_node.vertex
            for i in range(length):
                if i not in min_node.path:
                    min_node.path.append(i)
                    min_node.cost += min_node.reduced_matrix[last][i]
                    last = i
            
            min_node.path.append(0)
            min_node.cost += cost_matrix[last][0]
            
            if min_node.cost < min_cost:
                min_cost = min_node.cost
                best_path = min_node.path[:]
            continue

        for i in range(length):
            if i not in min_node.path and min_node.reduced_matrix[min_node.vertex][i] != INFINITE:
                new_path = min_node.path + [i]
                new_matrix = copy_matrix(min_node.reduced_matrix)
                for k in range(length):
                    new_matrix[min_node.vertex][k] = INFINITE
                    new_matrix[k][i] = INFINITE
                new_matrix[i][0] = INFINITE
                cost_to_i = min_node.reduced_matrix[min_node.vertex][i]
                new_cost = min_node.cost + cost_to_i + reduce_matrix(new_matrix)
                
                child = Node(new_path, new_matrix, new_cost, i, min_node.level + 1)
                priority.append(child)

    if best_path:
        min_cost = calculate_path_cost(best_path, cost_matrix)

    return min_cost, best_path