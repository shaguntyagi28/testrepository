n=int(input("enter the no of terms"))
x=0
y=1
for i in range (0,n):
	z=x+y
	if(z%2==0):
		print(z)
	x=y
	y=z




