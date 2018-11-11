#!/usr/bin/env python3
import sys
import math
from copy import deepcopy

def findRowMiniMax(cost):
    maximin = -sys.maxsize
    for i, row in enumerate(cost):
        if min(row) > maximin:
            maximin = min(row)
            index = i

    return (i, maximin)

def findColMaxiMin(cost):
    minimax = sys.maxsize
    index = None

    for col in range(len(cost)):
        column = list()
        for row in range(len(cost)):
            column.append(cost[row][col])

        if max(column) < minimax:
            minimax = max(column)
            index = col

    return (index, minimax)

def tpzs(cost):
    row_minimax = findRowMiniMax(cost)
    col_maximin = findColMaxiMin(cost)
    
    if not row_minimax[1] == col_maximin[1]:
        print("No saddle point found") 

    row_vector = list(0 for _ in range(len(cost)))
    row_vector[row_minimax[0]] = 1

    col_vector = list(0 for _ in range(len(cost)))
    col_vector[col_maximin[0]] = 1

    print("Row Vector:", row_vector)
    print("Col Vector:", col_vector)
            

def main():
    num_of_players = n = int(input("Enter number of players: "))
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i] = list(map(int, input("Enter stratergy for player {}: ".format(i+1)).split()))

    tpzs(cost)

if __name__=="__main__":
    main()
