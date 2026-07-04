rec=[]
while True:
    line=input()
    if line=="*":
        break
    # record every position
    
    fourPos=list(map(float,line.split()[1:]))
    rec.append(fourPos)

point=1
while True:
    x,y=map(float,input().split())
    if x==9999.9 and y==9999.9:
        break
    # for loop -> every figure -> if on the figure -> print
    figure=1
    haveFigure=False
    
    for x1,y1,x2,y2 in rec:
        if (x>x1 and y<y1) and (x<x2 and y>y2):
            haveFigure=True
            print(f"Point {point} is contained in figure {figure}")
        figure+=1
    if not haveFigure:
        print(f"Point {point} is not contained in any figure")
    point+=1