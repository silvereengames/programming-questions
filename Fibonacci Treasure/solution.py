def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

num_values = int(input())
values = list(map(int, input().split()))

if all(is_fibonacci(values[i]) for i in range(1, len(values), 2)):
    print("I love me numbers!")
else:
    print("These numbers suck!")