n,k=input.split
n=int(n)
k=int(k)
m=list(map(int,input().split()))[:p]
sum=0
for i in range(k):
		sum=sum+m[i]
print(sum)
