while True:
    try:
        line=input().strip()
        if line=="0:00":
            break
        h,m=map(int,line.split(":"))

        # conversion angle 
        hourAng=30
        minuteAng=0.5

        hourAng=h*hourAng+m*minuteAng
        minAng=m*6

        # print(hourAng,minAng)
        ans=abs(hourAng-minAng)
        if ans>180:
            ans=360-ans
        print(f"{ans:.3f}")
    except EOFError:
        break