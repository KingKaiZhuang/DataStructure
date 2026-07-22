while True:
    try:
        line1=input()
        line2=list(input())
        ans=[]
        for i in range(len(line1)):
            for j in range(len(line2)):
                if line1[i]==line2[j]:
                    ans.append(line1[i])
                    line2[j]=""
                    break
        ans.sort()
        
        for j in ans:
            print(j,end="")
        print()

    except EOFError:
        break