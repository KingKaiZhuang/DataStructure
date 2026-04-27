ugly=[1]
p2,p3,p5=0,0,0

while len(ugly)<1500:
    next2=ugly[p2]*2
    next3=ugly[p3]*3
    next5=ugly[p5]*5

    nextUgly=min(next2,next3,next5)
    ugly.append(nextUgly)
    if next2==nextUgly:
        p2+=1
    if next3==nextUgly:
        p3+=1
    if next5==nextUgly:
        p5+=1

print(f"The 1500'th ugly number is {ugly[-1]}.")