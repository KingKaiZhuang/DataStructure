while True:
    try:
        t=int(input())

        for _ in range(t):
            emp=input()
            line=input().strip()
            length=len(line)

            for i in range(1,length+1):
                if length%i==0:
                    tmp=line[:i]
                    if tmp*(length//i)==line:
                        print(i)
                        break
    except EOFError:
        break