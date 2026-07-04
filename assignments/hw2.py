def format_set(s):
    lst=list(s)
    lst.sort()
    out=""
    for char in lst:
        out+=char
    return "{"+out+"}"

line=input()
if line:
    n=int(line)

    for i in range(1,n+1):
        a=input()
        b=input()
        x=input()

        set_a=set(a)
        set_b=set(b)

        print(f"Test Case {i}:")
        print(f"A: {format_set(set_a)}")
        print(f"B: {format_set(set_b)}")
        print(f"A+B: {format_set(set_a | set_b)}")
        print(f"A*B: {format_set(set_a & set_b)}")
        print(f"A-B: {format_set(set_a - set_b)}")
        print(f"B-A: {format_set(set_b - set_a)}")
        
        if set_a >= set_b:
                print("A contains B")
        else:
            print("A does not contain B")
            
        if set_b >= set_a:
            print("B contains A")
        else:
            print("B does not contain A")
            
        if x in set_a:
            print(f"'{x}' is in A")
        else:
            print(f"'{x}' is not in A")
            
        if x in set_b:
            print(f"'{x}' is in B")
        else:
            print(f"'{x}' is not in B")
            
        if i < n:
            print() 