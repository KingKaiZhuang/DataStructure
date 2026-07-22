t=int(input())
isFirst=True

for _ in range(t):
    if not isFirst:
        print()
    isFirst=False

    emp=input()
    n=int(input())
    # the input string
    rec=[]
    for _ in range(n):
        rec.append(input())
    sortRec=[(r,sorted(r)) for r in rec]
    # test string
    # print("into test case")
    while True:
        caseNum=1
        line=input()
        ans=[]
        if line=="END":
            break
        s1=sorted(list(line))
        # check the string -> if in the rec -> destroy -> next
        for origRec,r in sortRec:
            s2=sorted(list(r))
            if s1==s2:
                ans.append(origRec)
        
        print(f"Anagrams for: {line}")
        if len(ans)>0:
            for anagrams in ans:
                print(f"{caseNum:3}) {anagrams}")
                caseNum+=1
        else:
            print(f"No anagrams for: {line}")           
        