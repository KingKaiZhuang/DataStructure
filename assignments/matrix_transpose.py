A = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9],
    [10, 11, 12]
]

rows=len(A)
columns=len(A[0])

B=[[0 for _ in range(rows)] for _ in range(columns)]

for i in range(rows):
    for j in range(columns):
        B[j][i]=A[i][j]

print("轉置後的矩陣 B:")
for row in B:
    print(row)