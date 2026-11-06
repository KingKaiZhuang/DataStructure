def sort_key(c):
	return (-alphaRec[c],c)

caseNum=int(input())
rec=[]
alphaRec={}

for _ in range(caseNum):
	s=input().upper()
	
	for c in s:
		if c.isalpha():
			if c not in alphaRec:
				alphaRec[c]=1
				rec.append(c)
			else:
				alphaRec[c]+=1

rec.sort(key=sort_key)

for c in rec:
	print(c,alphaRec[c])