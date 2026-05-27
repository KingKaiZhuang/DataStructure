while True:
    try:
        line=input()
        rec=[]

        for c in line:
            if c.isalpha():
                rec.append(c)
            else:
                rec.append(" ")
        cleanWords="".join(rec)
        words=cleanWords.split()
        print(len(words))
    except EOFError:
        break