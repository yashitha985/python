n1=int(input())
arr=list(map(int,input().split()))
if sum(arr)==0:
	print(0)
else:
	l=list(sorted(arr))
	l.reverse()
	print(*l,sep="")
