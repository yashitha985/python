a=int(input())
sum=0
b=a
while a>0:
	c=a%10
	sum=sum+c*c*c
	a=a//10
if b==sum:
	print("yes")
else:
	print("no")
