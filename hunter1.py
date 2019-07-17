a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
	if(b.count(i)>=2 and i not in c):
		c.append(i)
if(len(c)==0):
	print("unique")
else:
	for i in c:
		print(i,end="")
