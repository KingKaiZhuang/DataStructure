caseNum=1

while True:
    try:
        t=int(input())
        for _ in range(t):
            arr=[]
            isSym=True
            line=input().strip().split()
            size=int(line[2])
            
            for _ in range(size):
                arr+=list(map(int,input().split()))

            for i in range(len(arr)):
                if arr[i]<0 or arr[len(arr)-1-i]<0:
                    isSym=False
                    break
                if arr[i]!=arr[len(arr)-1-i]:
                    isSym=False
                    break
            
            if isSym:
                print(f"Test #{caseNum}: Symmetric.")
            else:
                print(f"Test #{caseNum}: Non-symmetric.")
            caseNum+=1

    except EOFError:
        break