mirrorMap = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
    'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V',
    'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S',
    '3': 'E', '5': 'Z', '8': '8'
}

while True:
    try:
        line=input()

        # pal or mirr
        pal,mir=True,True
        # abc->1 abcd->2
        length=len(line)
        for i in range((length+1)//2):
            left=line[i]
            right=line[length-1-i]

            if left!=right:
                pal=False

            if left not in mirrorMap or mirrorMap[left]!=right:
                mir=False

        if pal and mir:
            print(f"{line} -- is a mirrored palindrome.")
        elif not pal and mir:
            print(f"{line} -- is a mirrored string.")
        elif pal and not mir:
            print(f"{line} -- is a regular palindrome.")
        else:
            print(f"{line} -- is not a palindrome.")

    except EOFError:
        break