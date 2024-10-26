def calculate_optimal_cost(A, l, r):
    # Calculate the optimal cost for the subarray A[l:r+1]
    k = r - l + 1
    mid = (l + r) // 2
    max_cost = 0
    
    # If k is even
    if k % 2 == 0:
        for i in range(k // 2):
            max_cost = max(max_cost, A[l + i] + A[r - i])
    else:
        # If k is odd, handle the middle element
        for i in range(k // 2):
            max_cost = max(max_cost, A[l + i] + A[r - i])
        max_cost = max(max_cost, A[mid])  # Include the middle element for odd length
    
    return max_cost

def solve(N, Q, A, queries):
    optimal_costs = []
    
    # Calculate optimal costs for all subarrays
    for l in range(N):
        for r in range(l, N):
            cost = calculate_optimal_cost(A, l, r)
            optimal_costs.append((cost, A[r] - A[l]))  # Store (cost, difference)

    # Sort by cost to efficiently answer queries
    optimal_costs.sort()

    results = []

    # Process each query
    for x in queries:
        total_sum = 0
        for cost, diff in optimal_costs:
            if cost <= x:
                total_sum += diff
            else:
                break
        results.append(total_sum)

    return results

# Input reading
N, Q = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
queries = [int(input().strip()) for _ in range(Q)]

# Get results
results = solve(N, Q, A, queries)

# Print results for each query
for result in results:
    print(result)