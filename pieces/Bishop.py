import pygame
from pieces.Piece import Piece


class Bishop(Piece):

    def __init__(self, color, location, pieces_matrix):
        super().__init__(color, location, pieces_matrix, piece_name='Bishop')

    def move_ways(self):
        available_places = []
        current_pos = self.where_am_i()
        primary = []
        secondary = []
        add = 1

        for i in range(2):
            for j in range(8):
                coordinate = (current_pos[0] - (add * j), current_pos[1] - (add * j))

                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    break

                if coordinate != current_pos:
                    if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                        primary.append(coordinate)
                    else:
                        if coordinate[0] < current_pos[0] or coordinate[1] > current_pos[1]:
                            break

            add = -add

        add = 1

        for i in range(2):

            for j in range(8):
                coordinate = (current_pos[0] - (add * j), current_pos[1] + (add * j))

                if coordinate[0] < 0 or coordinate[0] > 7 or coordinate[1] < 0 or coordinate[1] > 7:
                    break

                if coordinate != current_pos:
                    if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                        secondary.append(coordinate)
                    else:
                        if coordinate[0] < current_pos[0] or coordinate[1] > current_pos[1]:
                            break

            add = -add

        available_places = primary + secondary

        return available_places
