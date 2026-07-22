import math

testCase=int(input())
number=1

for _ in range(testCase):
    n1=int(input(),2)
    n2=int(input(),2)
    
    g=math.gcd(n1,n2)

    if g>1:
        print(f"Pair #{number}: All you need is love!")
    else:
        print(f"Pair #{number}: Love is not all you need!")
    number+=1
