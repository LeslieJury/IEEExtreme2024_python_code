def stick():
    inputNKL_string = input()
    inputNKL_list = inputNKL_string.split()
    N = inputNKL_list[0]
    K = inputNKL_list[1]
    L = inputNKL_list[2]
    print(N, K, L)


def main():
    stick()

main()