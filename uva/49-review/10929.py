while True:
    n=input()
    if n=="0":
        break
    odd,eve=0,0

    for i in range(len(n)):
        if i%2!=0:
            odd+=int(n[i])
        else:
            eve+=int(n[i])

    gap=abs(odd-eve)
    if gap==0 or gap%11==0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")
    