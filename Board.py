# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:25:13 2021

@author: Peyton
"""
import numpy as np
from Piece import Piece

startingFenString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";

class Board: 
    def __init__(self):
        Board.boardAr = np.zeros(64); 
        startingBoard = startingFenString.split(' ')[0]
        boardIter = 0
        Board.turn = 0; 
        for x in startingBoard:
            if x == '/' :
                boardIter -=1
            elif x == 'r':
                Board.boardAr[boardIter] = Piece.Rook | Piece.Black
            elif x == 'n':
                Board.boardAr[boardIter] = Piece.Knight | Piece.Black
            elif x == 'b':
                Board.boardAr[boardIter] = Piece.Bishop | Piece.Black
            elif x == 'q':
                Board.boardAr[boardIter] = Piece.Queen | Piece.Black
            elif x == 'k':
                Board.boardAr[boardIter] = Piece.King | Piece.Black
            elif x == 'p':
                Board.boardAr[boardIter] = Piece.Pawn | Piece.Black
            elif x == 'R':
                Board.boardAr[boardIter] = Piece.Rook | Piece.White
            elif x == 'N':
                Board.boardAr[boardIter] = Piece.Knight | Piece.White
            elif x == 'B':
                Board.boardAr[boardIter] = Piece.Bishop | Piece.White
            elif x == 'Q':
                Board.boardAr[boardIter] = Piece.Queen | Piece.White
            elif x == 'K':
                Board.boardAr[boardIter] = Piece.King | Piece.White
            elif x == 'P':
                Board.boardAr[boardIter] = Piece.Pawn | Piece.White
            elif x >= '1' or x <= '64':
                boardIter = boardIter + int(x) - 1
            
            boardIter += 1
            
    def toString(self):
        count = 0
        wholeIter = 0
        retString = ''
        for x in self.boardAr:
            if x != 0 and count != 0:
                retString += str(count)
                count = 0
                   
            
            if x == 0:
                count = count + 1
            elif x == Piece.Rook | Piece.Black:
                retString += 'r'
            elif x == Piece.Knight | Piece.Black:
                retString += 'n'
            elif x == Piece.Bishop | Piece.Black:
                retString += 'b'
            elif x == Piece.Queen | Piece.Black:
                retString += 'q'
            elif x == Piece.King | Piece.Black:
                retString += 'k'
            elif x == Piece.Pawn | Piece.Black:
                retString += 'p'
            elif x == Piece.Rook | Piece.White:
                retString += 'R'
            elif x == Piece.Knight | Piece.White:
                retString += 'N'
            elif x == Piece.Bishop | Piece.White:
                retString += 'B'
            elif x == Piece.Queen | Piece.White:
                retString += 'Q'
            elif x == Piece.King | Piece.White:
                retString += 'K'
            elif x == Piece.Pawn | Piece.White:
                retString += 'P'
            wholeIter += 1
            
            
            if ((wholeIter) % 8 == 0):
                if count != 0:
                    retString += str(count)
                    count = 0
                if wholeIter != 64:
                    retString+='/'
        return retString
    
    def movePiece(self, piece, position):
        if piece > 16:
            color = 16
        elif piece != 0:
            color = 8
        else:
            color = 0
        if Piece.Pawn | color ==  piece:
            self.movePawn(position, color)
        elif Piece.Bishop | color == piece:
            self.moveBishop(position, color)
        elif Piece.Knight | color == piece:
            self.moveKnight(position, color, 0, 0)
        self.turn += self.turn
            
    def movePawn(self, position, color):
        if color == 16:
            goalP = (Piece.Pawn | Piece.Black);
            if self.boardAr[position] == 0:
                if self.boardAr[position - 8] == goalP:
                    self.boardAr[position - 8] = 0;
                    self.boardAr[position] = goalP;
                elif self.boardAr[position - 16] == goalP and (position >= 24 and position <= 21):
                    self.boardAr[position - 16] = 0;
                    self.boardAr[position] = goalP;
            
        elif color == 8:
            goalP = (Piece.Pawn | Piece.White);
            
            if self.boardAr[position] == 0:
                if self.boardAr[position + 8] == goalP:
                    self.boardAr[position + 8] = 0;
                    self.boardAr[position] = goalP;
                elif self.boardAr[position + 16] == goalP and (position >= 32 and position <= 39):
                    self.boardAr[position + 16] = 0;
                    self.boardAr[position] = goalP;
            elif self.boardAr[position] > 16: 
                if self.boardAr[position + 7] == goalP:
                    self.boardAr[position] = goalP;
                    self.boardAr[position + 7] = 0;
                elif self.boardAr[position + 9] == goalP:
                    self.boardAr[position] = goalP;
                    self.boardAr[position + 9] = 0;
                    
        #En Passent here
    
    def moveBishop(self, position, color):
        if position < 0 or position > 63:
            print("invalid position")
            return False
        holder = position
        done = 0
        if color == 16:
            pass
        if color == 8:
            direction = [-9, -7, 7, 9]
            goalP = Piece.Bishop | Piece.White
            
            if self.boardAr[position] <= 14 and self.boardAr[position] != 0: 
                return False
            for x in direction:
                while holder >= 0 and holder <= 63 and done == 0:
                    if (holder + x > -1) and (holder + x < 64): 
                        if (self.boardAr[holder + x] == 0):
                            holder += x
                        elif (self.boardAr[holder + x] != goalP and self.boardAr[holder + x] > 0):
                            break
                        elif (self.boardAr[holder + x] == goalP):
                            self.boardAr[holder + x] = 0
                            self.boardAr[position] = goalP
                            done = 1
                holder = position
                     
    def moveKnight(self, position, color, row, col):
        if position < 0 or position > 63:
            print("invalid position")
            return False
        
        directions = [-17, -15, -10, -6, 6, 10, 15, 17]
        two = np.zeros(2)
        counter = 0
        if color == 16:
            pass
        if color == 8:
            goalP = Piece.Knight | Piece.White
            
            if self.boardAr[position] <= 14 and self.boardAr[position] != 0: 
                print("invalid move, friendly piece in the way")
                return False
            for x in directions:
                if position + x < 64 and position + x > -1:  
                    if self.boardAr[position + x] == goalP:
                        two[counter] = position + x
                        counter += 1
            
            if counter == 1:
                temp = two[0]
                
                self.boardAr[int(temp)] = 0
                self.boardAr[position] = goalP
            else:
                pass 
                #this is where we will figure out if there is 2 knights that can attack that position which one it is
            
                            
game = Board()
game.movePiece(game.boardAr[61], 52)
print(game.toString())
game.movePiece(game.boardAr[61], 54)
print(game.toString())
game.movePiece(game.boardAr[48], 36)
print(game.toString())
game.movePiece(game.boardAr[61], 52)
print(game.toString())
game.movePiece(game.boardAr[52], 65)
print(game.toString())

game.movePiece(game.boardAr[57], 42)
print(game.toString())
game.movePiece(game.boardAr[42], 57)
print(game.toString())