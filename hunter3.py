a=int(input())
b=list(map(int,input().split()))
flag=0
l=[]
for i in range(0,a):
	if(b[i]==i):
		temp=b[i]
		flag=1
		l.append(temp)
		l=sorted(l)
print(*l)

if(flag==0):
	print(-1)
