while True:
    n=input()
    if n=="0":
        break
    
    r1,r2=0,0
    for i in range(len(n)):
        if i%2!=0:
            r1+=int(n[i])
        else:
            r2+=int(n[i])

    g=abs(r1-r2)
    if g==0 or g%11==0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")