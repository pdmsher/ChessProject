# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:48:58 2021

@author: Peyton
"""
from Board import Board
from Piece import Piece
import pygame as p
import time

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
numToLet = { "P":Piece.Pawn,  "R":Piece.Rook , "N":Piece.Knight, "B": Piece.Bishop,  "Q" :Piece.Queen, "K" :Piece.King}
letToCol = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

def loadImages():
    pieces = ["r", "n", "b", "q", "k", "p", "R1", "N1", "B1", "Q1", "K1", "P1"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    

def main():
    p.init()
    screen = p.display.set_mode((HEIGHT, WIDTH))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    board = Board() 
    loadImages()
    done = False
    while done != True:
        for e in p.event.get():
            if e.type == p.QUIT:
                done = True
        clock.tick(MAX_FPS)
        p.display.flip()
        
        drawGame(screen, board)
        

def drawGame(screen, board):
    drawBack(screen)
    drawPieces(screen, board)


def drawBack(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
    
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board.boardAr[(r*8) + c]
            if piece != 0:
                if Piece.Rook | Piece.Black == piece:
                    screen.blit(IMAGES["r"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Knight | Piece.Black == piece:
                    screen.blit(IMAGES["n"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Bishop | Piece.Black == piece:
                    screen.blit(IMAGES["b"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Queen | Piece.Black == piece:
                    screen.blit(IMAGES["q"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.King | Piece.Black == piece:
                    screen.blit(IMAGES["k"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Pawn | Piece.Black == piece:
                    screen.blit(IMAGES["p"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Rook | Piece.White == piece:
                    screen.blit(IMAGES["R1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Knight | Piece.White == piece:
                    screen.blit(IMAGES["N1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Bishop | Piece.White == piece:
                    screen.blit(IMAGES["B1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Queen | Piece.White == piece:
                    screen.blit(IMAGES["Q1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.King | Piece.White == piece:
                    screen.blit(IMAGES["K1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                elif Piece.Pawn | Piece.White == piece:
                    screen.blit(IMAGES["P1"], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                
                
def breakString(move, color):
    start = move[0]
    piece = 0
    check = 0
    mate = 0
    if len(move) < 2: #error handling, Very bad error handling
        print("invalid move")
        return 0
    #Castling logic not complete yet. mainly cause i have no idea how yet
    if move == "O-O" or "O-O-O": 
        pass
        #this will be castling and super annoying
     
    #This strips off checks and mates which are special symbols
    if move[len(move) -1] == '+': 
        move = move.replace('+', '')
        check = 1
    elif move[len(move) - 1] == '#': 
        move = move.replace('#', '')
        mate = 1
    
    
    #This is for the move, I noticed moved are in pairs of 2 always in the end 
    #so we just take the last 2 letters if there is a number in the end of the string
    #after, we translate that into a position number, then strip it off
    if str(move[len(move) -1]).isdigit() == True: 
        pos = move[len(move) -2:]
        pos = translate(pos)
        move = move[:(len(move) - 2)]
        print(pos)
        
    #This sets what kind of piece it is. The piece type is always at the front 
    #of the move string. Color will just be determined by who's turn it is, and 
    #passed in
    if start.isupper():
        piece = numToLet[start] + color
        move = move[1:]
    else:
        piece = numToLet["P"] + color
     
    
    move = move.replace("x", '')
    
    #Last thing that can be in the string is either a row or a column needed for 
    #take logic, so we check if its a letter or number, which gives us our answer
    #for whether its a row or a column and we set that
    if len(move) != 0:
        if move.isdigit() == True:
            col = int(move)
            print(col)
        else:
            row = move
            print(row)
    

    #instead of returning we may just call our move function from here, which 
    #means i may need to change names because breakString and move
    #don't make sense for what they may do     
    return piece 


def translate(posInStr):
    
    pos = int(letToCol[posInStr[0]]) + ((8-int(posInStr[1])) * 8)
    return pos


print(breakString("e5", 16))
#print(breakString("asdfgsdfghR5", 16))
#main()
