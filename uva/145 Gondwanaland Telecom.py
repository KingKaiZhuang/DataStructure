while True:
    line=input()
    if line=="#":
        break
    record=line.split()
    step,phone,h1,m1,h2,m2=record[0],record[1],int(record[2]),int(record[3]),int(record[4]),int(record[5])

    # calculate min bitween
    n1=h1*60+m1
    n2=h2*60+m2
    duration=0
    if n1==n2:
        duration=1440
    elif n1<n2:
        duration=n2-n1
    else:
        duration=1440-n1+n2

    # for loop analyze [day,eve,night]
    day,eve,night=0,0,0
    curTime=n1
    for _ in range(duration):
        if 480<=curTime<1080:
            day+=1
        elif 1080<=curTime<1320:
            eve+=1
        else:
            night+=1
        
        curTime=(curTime+1)%1440
    
    # difine rate
    rates={
        'A':[0.10, 0.06, 0.02],
        'B':[0.25, 0.15, 0.05],
        'C':[0.53, 0.33, 0.13],
        'D':[0.87, 0.47, 0.17],
        'E':[1.44, 0.80, 0.30]
    }

    # cal total
    r1,r2,r3=rates[step]
    total=0
    total=r1*day+r2*eve+r3*night
    print(f"{phone:>10}{day:>6}{eve:>6}{night:>6}{step:>3}{total:>8.2f}")