def fibonacci(n):
    result = []
    a = 1 
    b = 1
    for i in range(n):
        result.append(a)
        temp = a + b 
        a = b
        b = temp
    return result 

fibonacci(6)