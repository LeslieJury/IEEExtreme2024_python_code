def main():
    from itertools import combinations
    from collections import defaultdict

    MOD = 10**9 + 7

    N = int(input("Enter the number of nodes: "))  # Get number of nodes
    weights = list(map(int, input("Enter the weights: ").split()))  # Get weights of nodes

    # Create the adjacency list for the tree
    tree = defaultdict(list)

    print("Enter the edges:")
    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    # To store the results for each k
    results = [0] * (N + 1)

    # Function to perform DFS to calculate the contribution of each subset
    def dfs(node, parent, subset):
        total_weight = 0
        subtree_size = 0
        
        for neighbor in tree[node]:
            if neighbor != parent:
                weight, size = dfs(neighbor, node, subset)
                total_weight += weight
                total_weight %= MOD
                subtree_size += size
        
        # Include the weight of the current node in the subset if it's included
        if node in subset:
            total_weight += weights[node]
            total_weight %= MOD
            subtree_size += 1
        
        return total_weight, subtree_size
    
    # Calculate the contributions for each subset size
    for k in range(1, N + 1):
        for subset in combinations(range(N), k):
            # Convert subset to a set for easy access
            subset_set = set(subset)
            # We can start from any node in the subset, typically the first node
            weight_sum, _ = dfs(subset[0], -1, subset_set)
            results[k] += weight_sum
            results[k] %= MOD
    
    # Output the results
    for k in range(1, N + 1):
        print(results[k])

if __name__ == "__main__":
    main()
