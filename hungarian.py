import math
m=int(input("Enter No of workers: "))
n=int(input("Enter No of jobs: "))
print("Enter Assignment Matrix:")
matrix= [[0 for x in range(n)] for y in range(m)]
cost=[[0 for x in range(n)] for y in range(m)]
for i in range(m):
	aux = []
	aux = map(int, raw_input().split())
	matrix[i]=aux
for i in range(m):
	for j in range(n):
		cost[i][j]=matrix[i][j]
for i in range(m):
	mini = 1000001
	for j in range(n):
		mini = min(mini,matrix[i][j])
	for j in range(n):
		matrix[i][j] -= mini
for i in range(n):
	mini = 1000001
	for j in range(m):
		mini = min(mini,matrix[j][i])
	for j in range(m):
		matrix[j][i] -= mini
k=0
while(k!=m):
	k=0
	count=1
	mark = [[0 for x in range(n)] for y in range(m)]
	while(count!=0):
		a=[]
		b=[]
		c=0
		for i in range(m):
			c=0
			for j in range(n):
				if (matrix[i][j]==0 and mark[i][j]==0):
					c=c+1
			a.append(c)
		for i in range(n):
			c=0
			for j in range(m):
				if (matrix[j][i]==0 and mark[j][i]==0):
					c=c+1
			b.append(c)
		maxx=0
		row=-1
		col=-1

		for i in range(m):
			if (a[i]>maxx):
				maxx=a[i]
				row=i
				col=-1
			if (b[i]>maxx):
				maxx=b[i]
				col=i
				row=-1
		if (row==-1 and col==-1):
			count=0
			break
		if (row!=-1):
			for i in range(n):
				mark[row][i]=mark[row][i]-1
			k=k+1
		else:
			for i in range(m):
				mark[i][col]=mark[i][col]-1
			k=k+1
	if(k==m):
		break
	mi=10000000
	for i in range(m):
		for j in range(n):
			if(matrix[i][j]<mi and mark[i][j]==0):
				mi=matrix[i][j]

	for i in range(m):
		for j in range(n):
			if(mark[i][j]==-2):
				matrix[i][j]+=mi
	for i in range(m):
		for j in range(n):
			if(mark[i][j]==0):
				matrix[i][j]-=mi
k=0
cc=0
while(k<m):
	u=-1
	for i in range(m):
		cc=0
		for j in range (n):
			if(matrix[i][j]==0):
				cc=cc+1
				u=j
		if(cc==1):
			k+=1
			for j in range(m):
				if(j!=i):
					if(matrix[j][u]==0):
						matrix[j][u]=12000
s=0
for i in range(m):
	for j in range(n):
		if(matrix[i][j]==0):
			s=s+cost[i][j]
			print((i+1),"-->",(j+1))
print("Total cost:",s)

