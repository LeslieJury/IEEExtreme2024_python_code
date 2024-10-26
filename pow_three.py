def find_x(N):
    if N == 1:
        return 0  # 3^0 = 1
    
    x = 0
    while N > 1:
        if N % 3 != 0:
            return -1
        N //= 3
        x += 1
    
    return x

# Input
N = int(input())

# Output
result = find_x(N)
print(result)
