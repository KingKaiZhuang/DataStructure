def check_m(k,m):
    current_pos=0
    for i in range(k):
        remaining_people=2*k-i
        current_pos=(current_pos+m-1)%remaining_people

        if current_pos<k:
            return False
    
    return True

answers=[0]*14

for k in range(1,14):
    m=1
    while not check_m(k,m):
        m+=1
    answers[k]=m

while True:
    try:
        k=int(input())
        if k==0:
            break
        print(answers[k])
    except EOFError:
        break