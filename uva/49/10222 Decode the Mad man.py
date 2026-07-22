keys="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

while True:
    try:
        line=input().lower()
        index=0
        ans=""
        for i in line:
            if i==" ":
                ans+=" "
            else:
                index=keys.index(i)
                ans+=keys[index-2]
        print(ans)
    except EOFError:
        break