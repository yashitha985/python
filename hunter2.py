y=int(input())
z=list(map(int,input.split()))
z.sort(reverse=True)
for i in range(len(z)):
		print(z[i],end='')
