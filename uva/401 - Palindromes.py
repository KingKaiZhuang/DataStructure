mirrorMap = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
    'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
    '3': 'E', '5': 'Z', '8': '8'
}

while True:
    try:
        line=input().strip()
        length=len(line)
        # palindrome,mirrored,both
        isPal=True
        isMir=True
        for i in range((length+1)//2):
            left=line[i]
            right=line[length-1-i]

            # palindrome
            if left!=right:
                isPal=False
            # mirrored
            if left not in mirrorMap or mirrorMap[left]!=right:
                isMir=False
        
        # ans
        if isPal and isMir:
            print(f"{line} -- is a mirrored palindrome.")
        elif isPal and not isMir:
            print(f"{line} -- is a regular palindrome.")
        elif not isPal and isMir:
            print(f"{line} -- is a mirrored string.")
        else:
            print(f"{line} -- is not a palindrome.")
        print()
    except EOFError:
        break