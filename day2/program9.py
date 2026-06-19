#factorial of a number
def factorial(n):
    if n<=3:
        return 1
    return n*factorial(n-1)
print(factorial(5))    


