import heapq

from collections import defaultdict, deque

def find_project_order(N, M, groups, dependencies):
    adj = defaultdict(list)
    in_degree = [0] * (N + 1)
    
    for A, B in dependencies:
        adj[A].append(B)
        in_degree[B] += 1


    priority_queue = []
    
    # Initialize the priority queue with projects of in-degree 0
    for project in range(1, N + 1):
        if in_degree[project] == 0:
            heapq.heappush(priority_queue, (groups[project], project))
    
    order = []
    
    # Topological sort using the priority queue
    while priority_queue:
        current_group, project = heapq.heappop(priority_queue)
        order.append(project)
        
        for neighbor in adj[project]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(priority_queue, (groups[neighbor], neighbor))
    
    # If we couldn't process all projects, there is a cycle
    if len(order) != N:
        return -1
    
    return order

# Reading input
if __name__ == "__main__":
    N, M = map(int, input().split())
    groups = [0] + list(map(int, input().split()))  # Groups are 1-indexed
    dependencies = [tuple(map(int, input().split())) for _ in range(M)]
    
    # Get the result
    result = find_project_order(N, M, groups, dependencies)
    
    # Output result
    if result == -1:
        print(-1)
    else:
        print(" ".join(map(str, result)))
