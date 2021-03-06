# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:25:13 2021

@author: Peyton
"""
import numpy as np
from Piece import Piece


class Board: 
    def __init__(self, boardState):
        Board.boardAr = np.empty(shape = (8,8), dtype = "object")
        if boardState == "empty":
            print('empty')
        elif boardState == "starting":
            Board.boardAr[0][0] = Piece("R", 1)
            Board.boardAr[0][1] = Piece("N", 1)
            Board.boardAr[0][2] = Piece("B", 1)
            Board.boardAr[0][3] = Piece("Q", 1)
            Board.boardAr[0][4] = Piece("K", 1)
            Board.boardAr[0][5] = Piece("B", 2)
            Board.boardAr[0][6] = Piece("N", 2)
            Board.boardAr[0][7] = Piece("R", 2)
            
            for i in range (7):
                Board.boardAr[1][i] = Piece("P",i + 1)
                Board.boardAr[6][i] = Piece("p", i+1)
                
            Board.boardAr[7][0] = Piece("r", 1)
            Board.boardAr[7][1] = Piece("n", 1)
            Board.boardAr[7][2] = Piece("b", 1)
            Board.boardAr[7][3] = Piece("q", 1)
            Board.boardAr[7][4] = Piece("k", 1)
            Board.boardAr[7][5] = Piece("b", 2)
            Board.boardAr[7][6] = Piece("n", 2)
            Board.boardAr[7][7] = Piece("r", 2)
            
    def toString(self):
        retString = "["
        for i in range(7):
            for j in range(7):
                retString = retString + ' ' + self.boardAr[i][j].pType
                
            retString = retString + ']\n'
        return retString