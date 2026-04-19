from itertools import permutations

while True:
    try:
        # input
        s=list(map(int,input().split()))
    except EOFError:
        break
    
    # condition sum sort
    alpha=['B','C','G']
    containers={
        'B':[s[0],s[3],s[6]],
        'G':[s[1],s[4],s[7]],
        'C':[s[2],s[5],s[8]]
    }
    # def
    total=sum(s)
    minN=99999
    ans=""

    for i in permutations(alpha):
        a1,a2,a3=int(containers[i[0]][0]),int(containers[i[1]][1]),int(containers[i[2]][2])
        stay=a1+a2+a3

        if total-stay<minN:
            minN=total-stay
            ans=i[0]+i[1]+i[2]
    print(ans,minN)