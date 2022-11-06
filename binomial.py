def factorial(n):   # calculates n!
    x = 1
    for i in range(1,n+1):
        x *= i
    return x


def n_choose_k(n, k):       # calculates C(n,k)
    return factorial(n)/(factorial(k)*factorial(n-k))


def binomial_distribution(n, k, p):
    # Calculates binomial distribution
    # n = number of trials, k = number of successes, p = probability of a single success
    choose = n_choose_k(n, k)
    probability = (p**k)*(1-p)**(n-k)
    return choose*probability


def binomial_fewer_than(n, k, p):
    # Calculates the probability of k or fewer successes
    total = 0
    for i in range(0, k+1):
        total += binomial_distribution(n, i, p)
    return total


print(binomial_fewer_than(200, 16, 0.12))
