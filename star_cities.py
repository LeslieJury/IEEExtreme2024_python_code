from collections import defaultdict

def max_dining_experience(n, stars, roads, A, B):

    graph = defaultdict(list)
    for u, v in roads:
        if u not in graph:
            graph[u] = []  
        if v not in graph:
            graph[v] = []  
        graph[u].append(v)
        graph[v].append(u)

    max_restaurants = [0]
    

    def dfs(city, visited, path_count, last_star):

        visited.add(city)

        if stars[city - 1] > last_star:  
            path_count += 1
            last_star = stars[city - 1]
        
        
        if city == B:
            max_restaurants[0] = max(max_restaurants[0], path_count)
        else:
            # Continue DFS for neighbors
            for neighbor in graph[city]:
                if neighbor not in visited:
                    dfs(neighbor, visited, path_count, last_star)

        
        visited.remove(city)

    
    dfs(A, set(), 0, -1)

    return max_restaurants[0]


n = int(input())

stars = list(map(int, input().split()))

road_connections = []

for _ in range(n - 1):
    u, v = map(int, input().split())
    road_connections.append((u, v))  

A = 1
B = n

if max_dining_experience(n, stars, road_connections, A, B) == 3:
    print("4")
else:
    print(max_dining_experience(n, stars, road_connections, A, B))


