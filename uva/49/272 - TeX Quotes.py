count=False

while True:
    try:
        line=input().strip()

        for i in line:
            if i=='"' and count==False:
                print('``',end="")
                count=True
            elif i=='"' and count==True:
                print("''",end="")
                count=False
            else:
                print(i,end="")
        print()
    except EOFError:
        break