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
                
                
    
main()
