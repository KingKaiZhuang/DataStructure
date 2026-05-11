print("PERFECTION OUTPUT")

while True:
    try:
        line=input().split()
        for i in line:
            n=int(i)
            if n==0:
                print("END OF OUTPUT")
                break
            total=1
            if n==1:
                total=0
            for j in range(2,int(n**0.5)+1):
                if n%j==0:
                    total+=j
                    if j!=n//j:
                        total+=n//j

            if n == total:
                print(f"{n:>5}  PERFECT")
            elif total > n:
                print(f"{n:>5}  ABUNDANT")
            else:
                print(f"{n:>5}  DEFICIENT")
            
    except EOFError:
        break