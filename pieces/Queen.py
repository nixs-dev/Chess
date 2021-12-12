import pygame
from pieces.Piece import Piece


class Queen(Piece):

    def __init__(self, color, location):
        super().__init__(color, location, piece_name='Queen')
