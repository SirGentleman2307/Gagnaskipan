
def factorial(n, output = 0):

    if output:
        output = output * n
    else:
        output += n

    n -= 1
    if n == 0:
        return output
    else:
        return factorial(n, output)

# print(factorial(int(input('Input number: '))))

def multiply(a, b):

    MAX = a if a > b else b
    MIN = b if b < a else a

    if b == 1:
        return a

    MID = MAX//2

    if MID % 2 == 1:
        return multiply(MIN,MID) + multiply(MIN, MID) + MID
    else:
        return multiply(MIN,MID) + multiply(MIN, MID)

print(multiply(6, 2))


