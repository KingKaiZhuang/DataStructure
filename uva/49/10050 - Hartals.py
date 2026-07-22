tCase=int(input())

for _ in range(tCase):
    d=int(input())
    n=int(input())
    rec=set()
    ans=0

    for i in range(n):
        r=int(input())
        step=r

        while step<=d:
            if step%7!=6 and step%7!=0:
                if step not in rec:
                    rec.add(step)
                    ans+=1
            step+=r
    print(ans)