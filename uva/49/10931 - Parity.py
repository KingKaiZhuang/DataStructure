while True:
    n=int(input())
    if n==0:
        break
    b=bin(n)[2:]
    count=b.count('1')
    
    print(f"The parity of {b} is {count} (mod 2).")