from utility import clr
from variables import actTable, tableEncode, tokedPeaces


""""
=== Chess program ===

  White:           |    Black:
10 = bishop        | 19 = bishop
20 = knight        | 29 = knight
50 = rook          | 59 = rook
40 = phan          | 49 = phan
30 = king          | 39 = king
60 = quin          | 69 = quin
0 = empty_square   | 0 = empty_square
"""

def drawTable():
    clr()

    for black in tokedPeaces[0]:
        print(f" {black}", end= "")
    print("\n")

    for i in range(8):
        for j in range(8):
            print(f" {tableEncode[actTable[i][j]]} ", end="")
        print("")
    print("")

    for white in tokedPeaces[1]:
        print(f" {white}", end= "")


def aiLoop():
    drawTable()
    while True:
        break


def humanLoop():
    while True:
        break



if __name__ == '__main__':
    asw: str = input(" Do you want to play against the Ai? [y/n] ").lower()
    if asw[0] == "y" or asw == "true":
        print("\n Ai selected")
        aiLoop()
    else:
        print("\n Opponent selected")
        humanLoop()
