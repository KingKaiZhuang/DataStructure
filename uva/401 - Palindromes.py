mirrorMap = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
    'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
    '3': 'E', '5': 'Z', '8': '8'
}

while True:
    try:
        s=input().strip()
        if not s:
            continue

        isPal=True
        isMir=True
        length=len(s)

        for i in range((length+1)//2):
            leftChar=s[i]
            rightChar=s[length-1-i]

            if leftChar!=rightChar:
                isPal=False

            if leftChar not in mirrorMap or mirrorMap[leftChar]!=rightChar:
                isMir=False

        if isPal and isMir:
            print(f"{s} -- is a mirrored palindrome.")
        elif isPal and not isMir:
            print(f"{s} -- is a regular palindrome.")
        elif not isPal and isMir:
            print(f"{s} -- is a mirrored string.")
        else:
            print(f"{s} -- is not a palindrome.")
        print()

    except EOFError:
        break