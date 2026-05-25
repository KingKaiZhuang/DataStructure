fingers={
    'c':[2,3,4,7,8,9,10],
    'd':[2,3,4,7,8,9],
    'e':[2,3,4,7,8],
    'f':[2,3,4,7],
    'g':[2,3,4],
    'a':[2,3],
    'b':[2],
    'C':[3],
    'D':[1,2,3,4,7,8,9],
    'E':[1,2,3,4,7,8],
    'F':[1,2,3,4,7],
    'G':[1,2,3,4],
    'A':[1,2,3],
    'B':[1,2]
}

testCase=int(input())

for _ in range(testCase):
    rec={i:0 for i in range(1,11)}
    current=[]
    line=input()
    for i in line:
        tmp=fingers[i]
        for j in tmp:
            if j not in current:
                rec[j]+=1
            else:
                continue
        current=fingers[i]
    print(*rec.values())
