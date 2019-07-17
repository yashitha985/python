A,B=input().split()
A=int(A)
B=int(B)
l=[]
if(A>1 and B>1):
	for i in range (A,B+1):
		for j in range (2,i):
			if(i%j==0):
				break
		else:
			l.append(i)
print(len(l))
