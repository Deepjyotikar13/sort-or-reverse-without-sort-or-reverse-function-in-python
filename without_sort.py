lis=[67,90,23,99,45,89]
manum=max(lis)#find max of list
minum=min(lis)#find min of lis
newlis=[]
for i in range(minum,manum+1):
	if i in lis:
		newlis.append(i)
	else:
		pass
print(newlis)