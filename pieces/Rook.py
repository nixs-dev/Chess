import pygame
from pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, color, location, pieces_matrix):
        super().__init__(color, location, pieces_matrix, piece_name='Rook')

    def move_ways(self):
        available_places = []
        current_pos = self.where_am_i()
        horizontal = []
        vertical = []
        add = 1

        for direction in range(2):
            for x in range(8):
                coordinate = (current_pos[0] + (x * add), current_pos[1])

                if coordinate[0] > 7 or coordinate[0] < 0:
                    break

                if coordinate != current_pos:
                    if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                        horizontal.append(coordinate)
                    else:
                        break

            add = -add

        add = 1

        for direction in range(2):
            for y in range(8):
                coordinate = (current_pos[0], current_pos[1] + (y * add))

                if coordinate[1] > 7 or coordinate[1] < 0:
                    break

                if coordinate != current_pos:
                    if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                        horizontal.append(coordinate)
                    else:
                        break

            add = -add

        available_places = horizontal + vertical

        return available_places
