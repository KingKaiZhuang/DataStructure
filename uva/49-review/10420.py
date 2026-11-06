testCase=int(input())

country={}
for i in range(testCase):
    s=list(map(str,input().split()))
    if s[0] not in country:
        country[s[0]]=1
    else:
        country[s[0]]+=1

for name in sorted(country):
    print(name,country[name])