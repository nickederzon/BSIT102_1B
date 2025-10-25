for n in range(1,7,1):
	for i in range(6,n,-1):
		print(" ",end=' ')
	for c in range(n,0,-1):
		print(c,end=' ')
	for k in range(2,n+1,1):
		print(k,end=' ')
	print()