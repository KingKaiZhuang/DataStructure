def towers(n,A,B,C):
    if n==1:
        print(f"move disk 1 from peg",A," to peg ",C)

    towers(n-1,A,C,B)

    print(f"move disk{n} from {A} to peg {C}")

    towers(n-1,B,A,C)

n=int(input())
towers(n,'A','B','C')