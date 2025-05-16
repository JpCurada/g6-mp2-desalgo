def travelling_salesman(graph, start):
    """
    Travelling Salesman Problem using Lucero's algorithm
    """
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    path = [start]
    min_cost = float('inf')
    
    def dfs(current, cost, count):
        if count == n:  
            nonlocal min_cost
            if cost + graph[current][start] < min_cost:
                min_cost = cost + graph[current][start]
                return
            
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                path.append(i)
                dfs(i, cost + graph[current][i], count + 1)
                visited[i] = False
                path.pop()  
            
    dfs(start, 0, 1)
    return min_cost, path
