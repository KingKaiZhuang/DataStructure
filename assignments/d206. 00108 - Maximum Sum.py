buffer=[]

while True:
    try:
        while not buffer:
            buffer.extend(input().split())
        N=int(buffer.pop(0))

        matrix=[]
        for i in range(N):
            row=[]
            while len(row)<N:
                while not buffer:
                    buffer.extend(input().split())
                row.append(int(buffer.pop(0)))

        # 觀察點：列印出 N 與矩陣，確認讀取邏輯正確
        print(f"Read N = {N}")
        for r in matrix:
            print(r)
    except EOFError:
        break