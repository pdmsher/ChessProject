# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:48:58 2021

@author: Peyton
"""
from Board import Board
from Piece import Piece

gamestate = 1
boardState = "starting"
while (gamestate == 1):
    Game = Board(boardState)
    print(Game.toString())
    gamestate = 0