#!/usr/bin/env python3
import math
from copy import deepcopy

def find_penalty(elements: list):
    if len(elements) == 1:
        return element[0]
    temp = sorted(elements)
    return temp[1] - temp[0]

def find_max_penalty(row_penalty: list, col_penalty: list):
    max_row_p = max((v,i) for (i,v) in enumerate(row_penalty))
    max_col_p = max((v,i) for (i,v) in enumerate(col_penalty))
    return max_row_p, max_col_p

def check_balanced(demand, supply):
    total_demand = sum(demand)
    total_supply = sum(supply)
    
    return abs(total_demand - total_supply)
    
def balance_matrix(cost, demand, supply):
    total_demand = sum(demand)
    total_supply = sum(supply)
    diff = abs(total_demand - total_supply)

    if total_demand < total_supply:
        demand.append(diff)
        for row in cost:
            row.append(0)
    else:
        supply.append(diff)
        row_to_append = [0 for _ in range(len(cost[0]))]
        cost.append(row_to_append)
        
    return cost, demand, supply

def vam(demand, supply, cost):
    n = len(demand)
    m = len(supply)
    copy_cost = deepcopy(cost)
    
    x = [[0 for _ in range(n)] for _ in range(m)]
    
    while sum(supply) > 0:
        row_penalty = []
        for row in copy_cost:
            row_penalty.append(find_penalty(row))
        
        col_penalty = []
        for i in range(len(copy_cost[0])):
            col_penalty.append(find_penalty([copy_cost[j][i] for j in range(len(copy_cost))]))

        max_row_p, max_col_p = find_max_penalty(row_penalty, col_penalty)
        if max_row_p[0] > max_col_p[0]:
            min_cost = min((v,i) for (i,v) in enumerate(copy_cost[max_row_p[1]]))
            x[max_row_p[1]][min_cost[1]] = min(supply[max_row_p[1]], demand[min_cost[1]])
            supply[max_row_p[1]] -= x[max_row_p[1]][min_cost[1]]
            demand[min_cost[1]] -= x[max_row_p[1]][min_cost[1]]
            
            if supply[max_row_p[1]] == 0:
                for i in range(len(demand)):
                    copy_cost[max_row_p[1]][i] = 999999999
            else:
                for i in range(len(supply)):
                    copy_cost[i][min_cost[1]] = 999999999
        else:
            col = [copy_cost[i][max_col_p[1]] for i in range(len(copy_cost))]
            min_cost = min((v,i) for (i,v) in enumerate(col))
            x[min_cost[1]][max_col_p[1]] = min(supply[min_cost[1]], demand[max_col_p[1]])
            supply[min_cost[1]] -= x[min_cost[1]][max_col_p[1]]
            demand[max_col_p[1]] -= x[min_cost[1]][max_col_p[1]]
            
            if supply[min_cost[1]] == 0:
                for i in range(len(demand)):
                    copy_cost[min_cost[1]][i] = 999999999
            else:
                for i in range(len(supply)):
                    copy_cost[i][max_col_p[1]] = 999999999


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

    diff = check_balanced(demand, supply)

    if diff > 0:
        cost, demand, supply = balance_matrix(cost, demand, supply)

    vam(demand, supply, cost)

if __name__=="__main__":
    main()
