test=int(input())

for _ in range(test):
    n=int(input())
    line=list(map(int,input().split()))
    length=len(line)
    count=0

    for i in range(length):
        for j in range(0,length-1-i):
            if line[j]>line[j+1]:
                line[j+1],line[j]=line[j],line[j+1]
                count+=1

    print(f"Optimal train swapping takes {count} swaps.")