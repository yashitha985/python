a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
  if (b.count(i)>1):
    if i not in c:
      c.append(i)
if (len(c)==0):
  print('unique')
else:
  print(c[0]
