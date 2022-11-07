def factorial(n):   # calculates n!
    x = 1
    for i in range(1,n+1):
        x *= i
    return x