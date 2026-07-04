while True:
    try:
        n=int(input())
        step,level=0,0
        while step<n:
            level+=1
            step+=level
        duration=step-n
        
        if level%2==0:
            numerator=level-duration
            denominator=duration+1
        else:
            numerator=duration+1
            denominator=level-duration 
        print(f"TERM {n} IS {numerator}/{denominator}")
    except EOFError:
        break