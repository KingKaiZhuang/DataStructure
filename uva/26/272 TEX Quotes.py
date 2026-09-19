flag=True

while True:
    try:
        s=input()
        for c in s:
            if c=='"':
                if flag==True:
                    print("``",end="")
                    flag=False
                else:
                    print("''",end="")
                    flag=True
            else:
                print(c,end="")
        print()
    except EOFError:
        break