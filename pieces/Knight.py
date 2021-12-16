import pygame
from pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, color, location, pieces_matrix):
        super().__init__(color, location, pieces_matrix, piece_name='Knight')

    def move_ways(self):
        current_pos = self.where_am_i()
        available_places = [
            (current_pos[0] - 2, current_pos[1] + 1),
            (current_pos[0] - 2, current_pos[1] - 1),
            (current_pos[0] - 1, current_pos[1] + 2),
            (current_pos[0] - 1, current_pos[1] - 2),
            (current_pos[0] + 1, current_pos[1] - 2),
            (current_pos[0] + 1, current_pos[1] + 2),
            (current_pos[0] + 2, current_pos[1] + 1),
            (current_pos[0] + 2, current_pos[1] - 1),

        ]

        manipulated_list = [i for i in available_places]

        for place in manipulated_list:
            if place[0] > 7 or place[0] < 0 or place[1] > 7 or place[1] < 0:
                available_places.remove(place)

        manipulated_list = [i for i in available_places]

        for place in manipulated_list:
            if self.pieces_matrix[place[0]][place[1]] is not None:
                available_places.remove(place)

        return available_places
