print("enter the no of strings you want to insert")
n=int(input(""))
di=dict()
for i in range(n):
	p=(input ("enter string="))
	if p[0] not in di:
		di[p[0]]=[]
	di[p[0]].append(p)
ch=input("choice")
if ch in di:
	print(di[ch])
else:
	print("invalid") 