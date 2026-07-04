# define rates price
rates={
    'A':[0.10,0.06,0.02],
    'B':[0.25,0.15,0.05],
    'C':[0.53,0.33,0.13],
    'D':[0.87,0.47,0.17],
    'E':[1.44,0.80,0.30]
}


while True:
    line=input()
    if line=="#":
        break
    
    step,phone,h1,m1,h2,m2=line.split()
    h1,m1,h2,m2=int(h1),int(m1),int(h2),int(m2)
    day,eve,night=0,0,0
    # switch to minutes
    n1=h1*60+m1
    n2=h2*60+m2
    duration=0
    if n1>n2:
        duration=60*24-n1+n2
    elif n1<n2:
        duration=n2-n1
    else:
        duration=24*60
    # analyze time section
    total=0
    start=n1
    for _ in range(duration):
        if 8*60<=start<18*60:
            day+=1
        elif 18*60<=start<22*60:
            eve+=1
        else:
            night+=1
        start=(start+1)%(24*60)
    total=rates[step][0]*day+rates[step][1]*eve+rates[step][2]*night
    print(f"{phone:>10}{day:>6}{eve:>6}{night:>6}{step:>3}{total:>8.2f}")