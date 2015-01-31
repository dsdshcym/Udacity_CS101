#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

# My solution
def fibonacci(n):
    f = [1, 1]
    i = 2
    while i <= n:
        f[i % 2] = f[0] + f[1]
        i += 1
    return f[i % 2]

# Suggest solution
def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

print fibonacci(36)
#>>> 14930352
