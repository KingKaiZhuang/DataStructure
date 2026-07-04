def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

while True:
    try:
        n=input()
        n1=int(n)

        if not isPrime(n1):
            print(f"{n} is not prime.")
        else:
            n2=int(n[::-1])
            
            if n1!=n2 and isPrime(n2):
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")

        
    except EOFError:
        break