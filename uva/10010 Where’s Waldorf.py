while True:
    try:
        tCase=int(input())
        emp=input()

        for caseNum in range(tCase):
            if caseNum>0:
                emp=input()

            r,c=map(int,input().split())
            rec=[]
            for _ in range(r):
                rec.append(input().strip().lower())
            
            t=int(input().strip())
            if caseNum>0:
                print()

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for _ in range(t):
                word=input().strip().lower()
                word_len=len(word)
                found=False

                for i in range(r):
                    for j in range(c):
                        if rec[i][j]==word[0]:
                            for dr,dc in dirs:
                                match=True
                                for k in range(1,word_len):
                                    nr=i+dr*k
                                    nc=j+dc*k

                                    if nr<0 or nr>=r or nc<0 or nc>=c or rec[nr][nc]!=word[k]:
                                        match=False
                                        break
    except EOFError:
        break