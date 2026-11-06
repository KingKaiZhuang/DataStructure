while True:
    try:
        n1,n2=map(int,input().split())
        if n1==0 and n2==0:
            break

        carry=0
        add=0
        while n1>0 or n2>0:
            
            tail1=n1%10
            tail2=n2%10
            n1//=10
            n2//=10

            if tail1+tail2+add>=10:
                add=1
                carry+=1
            else:
                add=0

        if carry==0:
            print("No carry operation.")
        elif carry==1:
            print(f"{carry} carry operation.")
        else:
            print(f"{carry} carry operations.")

    except EOFError:
        break