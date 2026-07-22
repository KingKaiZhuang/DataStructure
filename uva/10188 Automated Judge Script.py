number=1

while True:
    try:
        # input
        n1=int(input())
        if n1==0:
            break
        rec1=[]
        for _ in range(n1):
            rec1.append(input())

        n2=int(input())
        rec2=[]
        for _ in range(n2):
            rec2.append(input())
        # compare
        if n1==n2 and rec1==rec2:
            print(f"Run #{number}: Accepted")
        else:
            # Presentation Error
            digits1=""
            for line in rec1:
                for char in line:
                    if char.isdigit():
                        digits1+=char
            
            digits2=""
            for line in rec2:
                for char in line:
                    if char.isdigit():
                        digits2+=char

            if digits1==digits2:
                print(f"Run #{number}: Presentation Error")
            else:
                print(f"Run #{number}: Wrong Answer")

        number+=1

    except EOFError:
        break