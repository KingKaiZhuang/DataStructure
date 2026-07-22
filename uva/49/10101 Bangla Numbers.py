def bangla(n):
    if n>=10000000:
        bangla(n//10000000)
        print(" kuti",end="")
        n%=10000000
    if n>=100000:
        bangla(n//100000)
        print(" lakh",end="")
        n%=100000
    if n>=1000:
        bangla(n//1000)
        print(" hajar",end="")
        n%=1000
    if n>=100:
        bangla(n//100)
        print(" shata",end="")
        n%=100    
    if n>0:
        print(f" {n}",end="")

title=1
while True:
    try:
        line=int(input())
        print(f"{title:4}.",end="")
        if line==0:
            print(f" 0")
        else:
            bangla(line)
        print()
        title+=1
    except EOFError:
        break