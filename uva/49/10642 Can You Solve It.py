testCase=int(input())
caseNum=1

for _ in range(testCase):
    x1,y1,x2,y2=map(int,input().split())
    n1=((x1+y1)*(x1+y1+1))//2+x1
    n2=((x2+y2)*(x2+y2+1))//2+x2
    print(f"Case {caseNum}: {n2-n1}")
    caseNum+=1