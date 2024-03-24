# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:12:54 2024

@author: yorda
"""

n = int(input("How many lines of result do you want: "))
outerList = []


def setMatrix(n):
    for i in range(n):
        innerList = []
        for j in range(3):
            innerList.append(int(input(f"Enter the {i+1}th row {j+1} item: ")))
        outerList.append(innerList)

def evalTruth():
    # I have used bitwise operators (&,|)
    # 1 is True and 0 is False
    for i in range(0, n):
        # & has higher precedence than |
        outerList[i].append((outerList[i][0] & outerList[i][1] | outerList[i][2]))
def showTable():
    print("\n\t\tTruth Table")
    print("\t a\t b\t c\t(a&b|c)")
    for i in range(n):
        for j in range(4):
            print("\t", outerList[i][j], end='')
        print()

setMatrix(n)
evalTruth()
showTable()

