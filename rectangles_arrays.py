def largest_area(heights):
    """ Calculate the largest rectangle area in a histogram. """
    heights = [0] + heights + [0]
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1 
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

def post_modification(A, X):
    N = len(A)
    
    initial_max_area = largest_area(A)
    
    post_modification = initial_max_area

    for i in range(N):
        original_value = A[i]
        
        for new_value in range(1, X + 1):
            A[i] = new_value
            modified_area = largest_area(A)
            post_modification = max(post_modification, modified_area)
        
        A[i] = original_value

    return post_modification

N, X = map(int, input().split())  
A = list(map(int, input().split())) 
result = post_modification(A, X)
print(result)
