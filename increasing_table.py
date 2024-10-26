MOD = 998244353

def factorial_and_inverse(n):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, 0, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    
    return fact, inv

def binomial(n, k, fact, inv):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD

def number_of_ways(N, A, B):
    len_A = len(A)
    len_B = len(B)
    
    # Number of numbers left for free placement
    total_numbers = 2 * N
    remaining_numbers = total_numbers - (len_A + len_B)

    # Precompute factorials and inverses
    fact, inv = factorial_and_inverse(total_numbers)

    # Calculate the number of valid ways
    ways = 1
    for i in range(len_A + len_B + 1, N + 1):
        ways = (ways * binomial(remaining_numbers, N - i, fact, inv)) % MOD

    return ways

# Input reading
N = int(input().strip())
data_A = list(map(int, input().strip().split()))
data_B = list(map(int, input().strip().split()))

# Extracting A and B
X = data_A[0]
A = data_A[1:X + 1]
Y = data_B[0]
B = data_B[1:Y + 1]

# Get the result
result = number_of_ways(N, A, B)

# Print the output
print(result + 1)
