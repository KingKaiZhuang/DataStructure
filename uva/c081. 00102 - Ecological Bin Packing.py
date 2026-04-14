from itertools import permutations

while True:
    try:
        arr=['B','C','G']
        # 輸入
        nList=list(map(int,input().split()))
        # 定義桶子
        container={
            "B": [nList[0],nList[3],nList[6]],
            "G": [nList[1],nList[4],nList[7]],
            "C": [nList[2],nList[5],nList[8]]
        }
        # 總數量
        total=sum(nList)
        minN=9999
        # 總數量 - 固定數量 = 變動量 (取最小)
        for p in permutations(arr):
            ans="".join(p)
            stay=container[p[0]][0]+container[p[1]][1]+container[p[2]][2]
            gap=total-stay
            
            if gap<minN:
                name=ans
                minN=gap
            
        print(f"{name} {minN}")

    except EOFError:
        break