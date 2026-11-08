def f(n):
    if len(n)==1:
        return n
    else:
        total=0
        for i in n:
            total+=int(i)
        return f(str(total))

while True:
    try:
        n=input()
        if n=="0":
            break
        ans=f(n)
        print(ans)
    except EOFError:
        break