# fibs
fibs=[1,2]
# complete fibs
for i in range(38):
    fibs.append(fibs[i]+fibs[i+1])
# input
n=int(input())
for _ in range(n):
    num=int(input())
    orig_num=num
    ans=""
    isStart=False
    # analyze
    for j in reversed(fibs):
        if j<=num:
            ans+='1'
            isStart=True
            num-=j
        elif j>num and isStart==True:
            ans+='0'
    print(f"{orig_num} = {ans} (fib)")