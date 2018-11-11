#!/usr/bin/env python3

def nwcm(demand, supply, cost):
    n = len(demand)
    m = len(supply)

    x = [[0 for _ in range(n)] for _ in range(m)]

    i, j = 0, 0
    while i<n or j<m:
        if i>=n:
            x_ij = supply[j]
        elif j>=m:
            x_if = demand[i]
        else:
            x_ij = min(demand[i], supply[j])

        x[j][i] = x_ij

        if not i>=n:
            demand[i] -= x_ij
            if demand[i] == 0:
                i += 1
        if not j>=m:
            supply[j] -= x_ij
            if supply[j] == 0:
                j += 1
        
    for i in range(m):
        print(x[i])

    print()
    res = 0
    for i in range(n):
        for j in range(m):
            res += x[j][i]*cost[j][i]

    print("Final result is: {}".format(res))
            
            

def main():
    demand = list(map(int, input("Enter demand: ").split()))
    supply = list(map(int, input("Enter supply: ").split()))
    cost = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    for i in range(len(supply)):
        cost[i] = list(map(int, input("Enter cost row {}: ".format(i+1)).split()))

    nwcm(demand, supply, cost)

if __name__=="__main__":
    main()
