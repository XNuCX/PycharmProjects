def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c



generator = fibonacci()
for i in range(5):
    print(next(generator))






def recur_fibo(n):
    a = 5
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 5
for i in range(nterms):
    print(recur_fibo(i))