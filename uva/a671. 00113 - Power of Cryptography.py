while True:
    try:
        n=int(input())
        p=int(input())

        left,right=0,10**9

        while left<=right:
            mid=(left+right)//2
            val=mid**n

            if val==p:
                print(mid)
                break
            elif val<p:
                left=mid+1
            else:
                right=mid-1
    except EOFError:
        break