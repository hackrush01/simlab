#!/usr/bin/env python3
import sys
from copy import deepcopy


def findNextSmallest(cost):
  _min = sys.maxsize
  row_col = ()
  for row_num, row in enumerate(cost):
    for col, num in enumerate(row):
      if num <= _min:
        _min = num
        row_col = (row_num, col)

  return row_col


def lcm(demand, supply, cost):
  copy_of_cost = deepcopy(cost)

  len_demand = len(demand)
  len_supply = len(supply)

  x = [[0 for _ in range(len_demand)] for _ in range(len_supply)]

  while max(demand) > 0 or max(supply) > 0:
    row, col = findNextSmallest(copy_of_cost)
    if demand[col] < supply[row]:
      x_ij = demand[col]
      for i in range(len_supply):
        copy_of_cost[i][col] = sys.maxsize
    else:
      x_ij = supply[row]
      for i in range(len_demand):
        copy_of_cost[row][i] = sys.maxsize

    demand[col] -= x_ij
    supply[row] -= x_ij
    x[row][col] = x_ij
    print((row, col),": " ,x_ij)


  print()
  for i in range(len_supply):
    print(x[i])

  print()
  res = 0
  for i in range(len_demand):
      for j in range(len_supply):
          res += x[j][i]*cost[j][i]

  print("Final result is: {}".format(res))
            
            

def main():
    demand = list(map(int, input("Enter demand: ").split()))
    supply = list(map(int, input("Enter supply: ").split()))

    cost = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    for i in range(len(supply)):
        cost[i] = list(map(int, input("Enter cost row {}: ".format(i+1)).split()))

    lcm(demand, supply, cost)

if __name__=="__main__":
    main()
