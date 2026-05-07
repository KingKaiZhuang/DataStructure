p2,p3,p5=0,0,0
ugly=[1]

while len(ugly)<1500:
    next2=ugly[p2]*2
    next3=ugly[p3]*3
    next5=ugly[p5]*5

    minN=min(next2,next3,next5)
    ugly.append(minN)

    if next2==minN:
        p2+=1
    if next3==minN:
        p3+=1
    if next5==minN:
        p5+=1
print(f"The 1500'th ugly number is {ugly[-1]}.")