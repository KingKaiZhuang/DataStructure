while True:
    try:
        # input
        n=int(input())
        total,level=1,1
        # line、total - current line
        while total<n:
            level+=1
            total+=level
        # duration
        duration=total-n
        if level%2==1:
            numerator=1+duration
            denominator=level-duration
        else:
            numerator=level-duration
            denominator=1+duration
        # result x/x
        print(f"TERM {n} IS {numerator}/{denominator}")    

    except EOFError:
        break