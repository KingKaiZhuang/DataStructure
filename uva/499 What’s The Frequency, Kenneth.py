while True:
    try:
        line=input().strip()
        rec={}
        maxN=0
        ans=[]
        # record -> print maxString and number
        for c in line:
            if c.isalpha():
                if c not in rec:
                    rec[c]=1
                else:
                    rec[c]+=1
            
                    if rec[c]>maxN:
                        maxN=rec[c]
                        ans=[c]
                    elif rec[c]==maxN:
                        ans.append(c)
        ans.sort()
        for i in ans:
            print(f"{i}",end="")
        print(f" {maxN}")
        
    except EOFError:
        break