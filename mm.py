import math
def bfs(i,j,moveY):
    print "here too"
    vis_ij[i][j]=1
    stp=0
    suc=0
    if(moveY):
        for ii in range(i+1,rows):
            if(stp==0):
                if(matrix[ii][j]!=0 or pij[ii][j]==cur):
                    stp=1
                    if((ii,j)==(x,y)):
                        index.append([i,j])
                        return 1
                    else:
                        if(vis_ij[ii][j]==0):
                            suc=bfs(ii,j,not moveY)
        for ii in range(i-1,-1,-1):
            if(stp==0):
                if(matrix[ii][j]!=0 or pij[ii][j]==cur):
                    stp=1
                    if((ii,j)==(x,y)):
                        index.append([i,j])
                        return 1
                    else:
                        if(vis_ij[ii][j]==0):
                            suc=bfs(ii,j,not moveY)
    else:
        for jj in range(j+1,cols):
            if(stp==0):
                if(matrix[i][jj]!=0 or pij[i][jj]==cur):
                    stp=1
                    if((i,jj)==(x,y)):
                        index.append([i,j])
                        return 1
                    else:
                        if(vis_ij[i][jj]==0):
                            suc=bfs(i,jj,not moveY)
        for jj in range(j-1,-1,-1):
            if(stp==0):
                if(matrix[i][jj]!=0 or pij[i][jj]==cur):
                    stp=1
                    if((i,jj)==(x,y)):
                        index.append([i,j])
                        return 1
                    else:
                        if(vis_ij[i][jj]==0):
                            suc=bfs(i,jj,not moveY)
    if(suc):
        index.append([i,j])
        return 1
    else:
        vis_ij[i][j]=-1
        return 0 

m=int(input("Enter No of factories: "))
n=int(input("Enter No of Warehouse: "))
print("Enter Cost Matrix:")
cost = [[0 for x in range(n)] for y in range(m)]
for i in range(m):
    a = []
    a = map(int,raw_input().split())
    cost[i] = a
print("Enter Allocation Matrix:")
matrix = [[0 for x in range(n)] for y in range(m)]
for i in range(m):
    a = []
    a = map(int,raw_input().split())
    matrix[i] = a
ans1=0
ans2=0
for i in range(m):
    for j in range(n):
        if matrix[i][j]>0:
            ans1+=(matrix[i][j]*cost[i][j])
flag = 1
while flag==1:
    ui = [-1 for x in range(m)]
    vi = [-1 for y in range(n)]
    ui[0]=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]>0:
                if (ui[i]>=0):
                    vi[j]=cost[i][j]-ui[i]
                else:
                    ui[i]=cost[i][j]-vi[j]
    flag=0
    pij=[[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0):
                pij[i][j]=cost[i][j]-ui[i]-vi[j]            
    for i in range(m):
        for j in range(n):
            if pij[i][j]<0:
                flag=1
    x=-1
    y=-1
    cur=0
    if flag==1:
        for i in range(m):
            for j in range(n):
                if pij[i][j]<0:
                    cur=pij[i][j]
                    x=i
                    y=j
        rows=m
        cols=n
        index =[]
        vis_ij=[[0 for j in range(cols)] for i in range(rows)]
        vis_ij[x][y]=1
        lp=0
        cr=0
        for j in range(y+1,cols):
            if(cr==0):
                if(matrix[x][j]!=0):
                    cr=1
                    if(vis_ij[x][j]==0):
                        lp=bfs(x,j,1)
                        print("here")
        index.append([x,y])
        cr=0
        if(lp):
            print(vis_ij)

        minimum=1000
        for i in range(len(index)):
            if(i%2==0):
                x1=index[i][0]
                y1=index[i][1]
                minimum=min(minimum,matrix[x1][y1])
        for i in range(len(index)):
            if(i%2==0):
                x1=index[i][0]
                y1=index[i][1]
                matrix[x1][y1]-=minimum
            else:
                x1=index[i][0]
                y1=index[i][1]
                matrix[x1][y1]+=minimum

for i in range(m):
    print (matrix[i])
for i in range(m):
    for j in range(n):
        if matrix[i][j]>0:
            ans2+=(matrix[i][j]*cost[i][j])
print("Old Solution is:",ans1)
print("New Solution is:",ans2)
