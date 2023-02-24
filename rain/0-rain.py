#!/usr/bin/python3
"""
calculating how many sq units of water are retained after it rains, given a list of non-negative integers representingthe heights of walls with unit width, 1
"""

def rain(walls):
    """get unit of water caught
    """
    amnt = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        amnt += (min(left, right) - walls[i])

    return amnt
