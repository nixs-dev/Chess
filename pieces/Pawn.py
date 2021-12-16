import pygame
from pieces.Piece import Piece


class Pawn(Piece):

    def __init__(self, color, location, pieces_matrix):
        super().__init__(color, location, pieces_matrix, piece_name='Pawn')

    def move_ways(self):
        current_pos = self.where_am_i()
        available_places = [(current_pos[0] - 1, current_pos[1]), (current_pos[0] - 2, current_pos[1])]

        if self.pieces_matrix[available_places[0][0]][available_places[0][1]] is not None:
            available_places = []
        else:
            if not self.first_move:
                available_places.pop(-1)

        return available_places
