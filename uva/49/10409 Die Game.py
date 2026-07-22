
curDir=0
curNum=0

while True:
    # initial
    t,n,w,e,s,b=1,2,3,4,5,6
    testCase=int(input())

    if testCase==0:
        break

    for _ in range(testCase):
        dir=input()
        if dir=="north":
            t,n,s,b=s,t,b,n
        elif dir=="south":
            t,n,s,b=n,b,t,s
        elif dir=="east":
            t,w,e,b=w,b,t,e
        else:
            t,w,e,b=e,t,b,w
        
    print(t)