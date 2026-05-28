while True:
    try:
        set1=set(map(int,input().split()))
        set2=set(map(int,input().split()))

        # equal
        if set1==set2:
            print("A equals B")
        # A in B
        elif set1 <= set2:
            print("A is a proper subset of B")
        # B in A
        elif set2 <= set1:
            print("B is a proper subset of A")
        # disjoint
        elif set1.isdisjoint(set2):
            print("A and B are disjoint")
        # no
        else:
            print("I'm confused!")
    except EOFError:
        break