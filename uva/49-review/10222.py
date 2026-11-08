keys="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

while True:
    try:
        s=input().lower()

        for c in s:
            if c==" ":
                print(" ",end="")
            else:
                index=keys.index(c)-2
                print(keys[index],end="")
        print()
    except EOFError:
        break