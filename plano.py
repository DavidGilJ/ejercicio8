def print_ways(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    print("Formas posibles de subir la escalera con", n, "peldaños:")
    stack = [(n, [])]
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
