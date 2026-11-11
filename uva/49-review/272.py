flag=True
while True:
    try:
        s=input()

        for c in s:
            if c=='"' and flag==True:
                print("``",end="")
                flag=False
            elif c=='"' and flag==False:
                print("''",end="")
                flag=True
            else:
                print(c,end="")
        print()
    except EOFError:
        break