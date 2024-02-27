#!/usr/bin/python3
'''Given heap of coins of dicide values,
    decide the smallets number of coins necessary to reach
    a specific amount total.
'''
import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total equals 0 or less, return 0
    Else, return -1
    '''
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]
