#------appending elements using numpy----------
import numpy as np
a=np.array([1,3,4,5,6,2.3])
b=np.array([2,3,8,0,-3.4,4])
d=np.array([5,7,0,9,8,7])
e=np.array([1,4,2,3,5,8,0])
f=np.array([0,7,8,9,5,6,4,3,2])
c=len(a)
print a
print b
for i in range(0,c):
	b=np.append(a[i],b)
print b
for j in range(0,c):
	if(a[i]<=10):
		d=np.append(a[i],d)
print d
for k in range(0,c):
	if(a[i]%2==0):
		e=np.append(a[i],e)
	else:
		f=np.append(a[i],f)
print f


