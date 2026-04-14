from itertools import permutations

while True:
    try:
        arr=['B','C','G']
        # 輸入桶子內有多少瓶子，三個一組，B G C
        container=list(map(int,input().split()))
        record={
            "B": [container[0],container[3],container[6]],
            "G": [container[1],container[4],container[7]],
            "C": [container[2],container[5],container[8]]
        }
        # 總數
        total=sum(container)

        minN=9999
        # 計算每個排列的移動次數，總共-不動
        for p in permutations(arr):
            s="".join(p)
            stay=record[p[0]][0]+record[p[1]][1]+record[p[2]][2]
            gap=total-stay

            if minN>gap:
                ans=s
                minN=gap
        print(f"{ans} {minN}")
    except EOFError:
        break