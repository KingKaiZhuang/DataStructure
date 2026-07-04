def transpose(elems):
    # record
    wide=len(elems)
    record=[0]*wide
    for e in elems:
        r,c,val=e
        record[c]+=1
    print(record)
    # position
    rowStart=[0]*wide
    for i in range(1,wide):
        rowStart[i]=rowStart[i-1]+record[i-1]    
    print(rowStart)
    # put in trans
    
        

elems = [
    [1, 3, 3],
    [1, 5, 4],
    [2, 3, 5],
    [2, 4, 7],
    [4, 2, 2],
    [4, 3, 6]
]

res=transpose(elems)