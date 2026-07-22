def summing(n):
    total=0
    for i in n:
        total+=int(i)
    if total>=10:
        return summing(str(total))
    else:
        return total

while True:
    n=input()
    if n=="0":
        break

    # function -> sum -> >=10 -> function -> <10 -> return ans
    ans=summing(n)
    print(ans)