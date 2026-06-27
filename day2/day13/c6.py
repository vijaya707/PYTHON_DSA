def fib(n):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]


n = 5
dp = [-1] * (n + 1)

print(fib(n))






n = int(input("Enter n: "))

dp = [-1] * (n + 1)

print(fib(n))











def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]



    