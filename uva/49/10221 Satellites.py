import math

while True:
    try:
        s,a,u=input().split()
        s,a=int(s),int(a)

        if u=="min":
            a=a/60

        if a>180:
            a=360-a

        r=6440+s
        chord=2*r*math.pi*(a/360)
        anc=a*(math.pi/180)
        dis=r*math.sin(anc/2)*2

        print(f"{chord:.6f} {dis:.6f}")
    except EOFError:
        break