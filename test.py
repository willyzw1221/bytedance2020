

a="[[1,2],[2,3]]"
lista=eval(a)
print(lista)

g='111222111222222'
import itertools
l = [(k, list(g)) for k, g in itertools.groupby(g)]
print(l)

n=5
res=[]
for i in range(n):
	if i==0: 
		res=[1]
	elif i==1: 
		res=[1,1]
	else:
		z=len(res)
		temp=[]
		res.append(0)
		j=0
		while j < z :
			t=1
			while  res[j]==res[j+1]:
				t=t+1
				j=j+1
			temp.append(t)
			temp.append(res[j])
			j=j+1
		res=[]
		res=temp[:]
		print(res)





