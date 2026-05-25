while True:
    try:
        line=input()
        # for loop -> total
        total=0
        maxN=0
        for i in line:
            d=-1
            if '0'<=i<='9':
                d=ord(i)-ord('0')
            elif 'A'<=i<='Z':
                d=ord(i)-ord('A')+10
            elif 'a'<=i<='z':
                d=ord(i)-ord('a')+36
            
            if d!=-1:
                total+=d
                if maxN<d:
                    maxN=d
        
        ok=False
        for j in range(maxN+1,63):
            if total%(j-1)==0:
                print(j)
                ok=True
                break

        if not ok:
            print("such number is impossible!")

    except EOFError:
        break