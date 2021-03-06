# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:31:43 2021

@author: Peyton
"""

class Piece:
    color  = 'e'
    def __init__(self, pType, number):
        if pType.islower():
            Piece.color = "Black"
        elif pType.isupper():
            Piece.color = "White"
        Piece.pType = pType
        self.number = number
        
        if pType == 'R' :
            self.name = "Rook" + ' ' + str(self.number)
        elif pType == 'N' :
            self.name = "Knight" + ' ' + str(self.number)
        elif pType == 'B' :
            self.name = "Bishop" + ' ' + str(self.number)
        elif pType == 'Q' :
            self.name = "Queen" 
        elif pType == 'K' :
            self.name = "King" 
        elif pType == 'P' :
            self.name = "Pawn" + ' ' + str(self.number)
        elif pType == 'r' :
            self.name = "Rook" + ' ' + str(self.number)
        elif pType == 'n' :
            self.name = "Knight" + ' ' + str(self.number)
        elif pType == 'b' :
            self.name = "Bishop" + ' ' + str(self.number)
        elif pType == 'q' :
            self.name = "Queen" 
        elif pType == 'k' :
            self.name = "King" 
        elif pType == 'p' :
            self.name = "Pawn" + ' ' + str(self.number)
        else :
            print("Invalid Piece Type")
            
        
        