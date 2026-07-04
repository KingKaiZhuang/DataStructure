# cache
cache={1:1}

while True:
    try:
        maxN=0
        n1,n2=map(int,input().split())
        print(n1,n2,end=" ")
        left,right=min(n1,n2),max(n1,n2)
        # for in cache? calculate length, record=[]
        for i in range(left,right+1):
            n=i
            record=[]
            length=0
            while n not in cache:
                record.append(n)
                if n%2!=0:
                    n=3*n+1
                else:
                    n=n//2
            length=len(record)+cache[n]

            if length>maxN:
                maxN=length
            # not in cache -> record cache finish
            # 0. 1. 2. 3. 4. 5. 6. 7
            # 40 20 10 5 16 8 4 2 1
            for key,value in enumerate(record):
                cache[value]=length-key
        print(maxN)
    except EOFError:
        break