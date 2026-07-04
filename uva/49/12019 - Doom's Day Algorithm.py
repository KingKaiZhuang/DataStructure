weeks=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    try:
        t=int(input())
        for _ in range(t):
            total=0
            m,d=map(int,input().split())
            if m==1:
                total=d
            else:
                for i in range(m-1):
                    total+=days[i]
                total+=d
            print(weeks[total%7-1])
    except EOFError:
        break