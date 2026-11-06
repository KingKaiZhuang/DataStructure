atomic={
    "C":12.01,
    "H":1.008,
    "O":16.00,
    "N":14.01
}

testCase=int(input())

for _ in range(testCase):
    line=input().strip()
    tmp=0
    ele=None
    total=0

    for c in line:
        if c.isdigit():
            tmp=(tmp)*10+int(c)
        else:
            if ele!=None:
                total+=atomic[ele]*(tmp if tmp>1 else 1)
            ele=c
            tmp=0
    total+=atomic[ele]*(tmp if tmp>1 else 1)
    print(f"{total:.3f}")