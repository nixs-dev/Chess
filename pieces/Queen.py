import pygame
from pieces.Piece import Piece


class Queen(Piece):

    def __init__(self, color, location, pieces_matrix):
        super().__init__(color, location, pieces_matrix, piece_name='Queen')

    def move_ways(self):
        available_places = []
        current_pos = self.where_am_i()
        horizontal = []
        vertical = []
        primary = []
        secondary = []

        # Horizontal and vertical

        for x in range(7, 0, -1):
            coordinate = (x, current_pos[1])

            if coordinate != current_pos:
                if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                    vertical.append(coordinate)
                else:
                    if x < current_pos[0]:
                        break

        for y in range(8):
            coordinate = (current_pos[0], y)

            if coordinate != current_pos:
                if self.pieces_matrix[coordinate[0]][coordinate[1]] is None:
                    horizontal.append(coordinate)
                else:
                    if y > current_pos[1]:
                        break

        available_places += horizontal + vertical

        # Diagonal

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

        available_places += primary + secondary

        return available_places
