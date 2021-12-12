import pygame
from pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, color, location):
        super().__init__(color, location, piece_name='Knight')
