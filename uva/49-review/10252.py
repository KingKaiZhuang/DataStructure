while True:
    try:
        s1=input()
        s2=list(input())

        rec=[]
        for i in s1:
            for j in range(len(s2)):
                if i==s2[j]:
                    rec.append(i)
                    s2[j]=""
                    break
        rec.sort()
        print("".join(rec))
    except EOFError:
        break