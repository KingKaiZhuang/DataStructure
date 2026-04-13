def fibonacci(num):
    lofib=0
    hifib=1
    for i in range(2,num+1):
        x=lofib
        lofib=hifib
        hifib=x+lofib
        
    return hifib

while True:
    n=int(input())
    fib=fibonacci(n)
    print(fib)