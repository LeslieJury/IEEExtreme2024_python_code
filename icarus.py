from collections import defaultdict

def construct_binary_tree(S):
    # Data structures to manage the binary tree
    tree = defaultdict(lambda: [0, 0])  # {node: [left, right]}
    parent = {}  # {child: parent}
    
    current_node = 1
    node_count = 1  # Start with node 1
    visited = set()
    
    # Initialize starting node
    A = 1  # Starting node is always 1
    visited.add(A)
    
    # Function to create a new node
    def create_node():
        nonlocal node_count
        node_count += 1
        return node_count

    # Navigate the tree based on the input string
    for direction in S:
        if direction == 'L':
            if tree[current_node][0] == 0:  # No left child exists
                new_node = create_node()
                tree[current_node][0] = new_node
                parent[new_node] = current_node
            current_node = tree[current_node][0]
        
        elif direction == 'R':
            if tree[current_node][1] == 0:  # No right child exists
                new_node = create_node()
                tree[current_node][1] = new_node
                parent[new_node] = current_node
            current_node = tree[current_node][1]
        
        elif direction == 'U':
            if current_node in parent:
                current_node = parent[current_node]
        
        # Mark the node as visited
        visited.add(current_node)
    
    # Determine an exit node B that is not visited
    B = None
    for i in range(1, node_count + 2):  # Go one node beyond current count
        if i not in visited:
            B = i
            break
    
    # Construct the output tree structure
    N = max(node_count, B)  # Ensure the number of nodes includes the isolated node B
    result = [(tree[i][0], tree[i][1]) for i in range(1, N + 1)]
    
    # Output the results
    print(N, A, B)
    for left, right in result:
        print(left, right)

# Example input handling
if __name__ == "__main__":
    S = input().strip()
    construct_binary_tree(S)
