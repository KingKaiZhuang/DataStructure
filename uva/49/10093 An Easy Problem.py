while True:
    try:
        line=input()
        total=0
        maxN=1

        for c in line:
            d=-1
            if '0'<=c<='9':
                d=ord(c)-ord('0')
            elif 'A'<=c<='Z':
                d=ord(c)-ord('A')+10
            elif 'a'<=c<='z':
                d=ord(c)-ord('a')+36

            if d!=-1:
                total+=d
                if d>maxN:
                    maxN=d
        
        found=False
        for i in range(maxN+1,63):
            if (total%(i-1))==0:
                print(i)
                found=True
                break

        if not found:
            print("such number is impossible!")

    except EOFError:
        break