while True:
    try:
        line=input().strip()
        rec={}
        # record O(N)
        for c in line:
            if c.isalpha():
                if c not in rec:
                    rec[c]=1
                else:
                    rec[c]+=1
        # calculate the max
        maxN=-1
        ans=[]
        # O(K)，也就是 O(1)
        for k,v in rec.items():
            if v>maxN:
                maxN=v
                ans=[k]
            elif v==maxN:
                ans.append(k)
        # O(K log K)
        ans.sort()
        
        print(f"{''.join(ans)} {maxN}")

    except EOFError:
        break