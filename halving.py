def count_permutations(N, C, R, B):
    MOD = 998244353
    total_count = 1
    used = [False] * (2 * N + 1)  # Tracking used numbers
    available = []

    for i in range(N):
        first = C[2 * i]
        second = C[2 * i + 1]
        b_val = B[i]
        r_val = R[i]

        if first != -1 and second != -1:
            # Both are readable
            if r_val == 0:
                if b_val != min(first, second):
                    return 0  # Impossible condition
            else:  # r_val == 1
                if b_val != max(first, second):
                    return 0  # Impossible condition
            # Mark these numbers as used
            used[first] = True
            used[second] = True
        elif first != -1:
            # Second is unreadable
            if r_val == 0:
                required = b_val
                if required >= first or required <= 0 or required > 2 * N or used[required]:
                    return 0  # Impossible
                available.append(required)
                used[first] = True
            else:  # r_val == 1
                required = b_val
                if required <= first or required <= 0 or required > 2 * N or used[required]:
                    return 0  # Impossible
                available.append(required)
                used[first] = True
        elif second != -1:
            # First is unreadable
            if r_val == 0:
                required = b_val
                if required <= second or required <= 0 or required > 2 * N or used[required]:
                    return 0  # Impossible
                available.append(required)
                used[second] = True
            else:  # r_val == 1
                required = b_val
                if required <= second or required <= 0 or required > 2 * N or used[required]:
                    return 0  # Impossible
                available.append(required)
                used[second] = True
        else:
            # Both are unreadable
            if r_val == 0:
                # Need min, can use any two available numbers
                pass  # Need to handle this case later
            else:
                # Need max, can use any two available numbers
                pass  # Need to handle this case later

    # Counting available numbers
    for number in range(1, 2 * N + 1):
        if not used[number]:
            available.append(number)

    # Counting permutations
    count_missing = len(available)  # Remaining values
    total_count = (total_count * factorial(count_missing)) % MOD

    return total_count

def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result = (result * i) % 998244353
    return result

# Read input
N = int(input())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
B = list(map(int, input().split()))

# Calculate the result
result = count_permutations(N, C, R, B)
print(result)
