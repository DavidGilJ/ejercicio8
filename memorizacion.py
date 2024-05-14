def count_ways(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
    return memo[n]

def print_ways(n):
    memo = [-1] * (n + 1)
    count_ways(n, memo)
    stack = [(n, [])]
    print("Formas posibles de subir la escalera con", n, "peldaños:")
    while stack:
        current_n, path = stack.pop()
        if current_n == 0:
            print(path)
        else:
            if current_n >= 1:
                stack.append((current_n - 1, path + [1]))
            if current_n >= 2:
                stack.append((current_n - 2, path + [2]))
            if current_n >= 3:
                stack.append((current_n - 3, path + [3]))

n = 3
print_ways(n)
