import pygame
from pygame import gfxdraw
from pieces import (Bishop, King, Knight, Pawn, Queen, Rook)


class Game:
    window = None
    window_size = (700, 700)
    sets_rects = []
    pieces_location = []
    run = True

    pieces = {
        'Bishop': Bishop.Bishop,
        'King': King.King,
        'Knight': Knight.Knight,
        'Pawn': Pawn.Pawn,
        'Queen': Queen.Queen,
        'Rook': Rook.Rook
    }

    initial_pieces_location = {
        'white': {
                'Pawn': [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
                'Rook': [(7, 0), (7, 7)],
                'Knight': [(7, 1), (7, 6)],
                'Bishop': [(7, 2), (7, 5)],
                'Queen': [(7, 3)],
                'King': [(7, 4)]
        },
        'black': {
            'Pawn': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
            'Rook': [(0, 0), (0, 7)],
            'Knight': [(0, 1), (0, 6)],
            'Bishop': [(0, 2), (0, 5)],
            'Queen': [(0, 3)],
            'King': [(0, 4)]
        }
    }

    selected_set = None
    selected_piece = None
    move_sets = None
    player_turn = 'white'

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Chess')

        self.box_positions = []

        self.draw_board()
        self.load_pieces()

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_clicked()

            self.window.fill((255, 255, 255))
            self.draw_board()
            self.draw_pieces()

            pygame.display.update()
            pygame.time.Clock().tick(40)

        pygame.quit()

    def check_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Sets clicks

        if pygame.mouse.get_pressed()[0]:
            for x, row in enumerate(self.sets_rects):
                for y, rect in enumerate(row):
                    if rect.collidepoint(mouse_x, mouse_y):
                        if self.move_sets is not None and (x, y) in self.move_sets:
                            matrix_new_coordinate = (x, y)
                            set_rect = self.sets_rects[matrix_new_coordinate[0]][matrix_new_coordinate[1]]
                            set_rect_coordinates = (set_rect.x, set_rect.y)

                            self.pieces_location = self.selected_piece.move(matrix_new_coordinate, set_rect_coordinates)

                            self.selected_set = None
                            self.selected_piece = None
                            self.move_sets = None

                        elif self.pieces_location[x][y] is not None:
                            self.selected_set = (x, y)
                            self.selected_piece = self.pieces_location[x][y]

                            available_moves = self.selected_piece.move_ways()
                            self.move_sets = [move for move in available_moves]

    def load_pieces(self):
        for x in range(8):
            row = []

            for y in range(8):
                row.append(None)

            self.pieces_location.append(row)

        for color in self.initial_pieces_location:
            for piece in self.initial_pieces_location[color]:
                for location in self.initial_pieces_location[color][piece]:
                    pos = (self.sets_rects[location[0]][location[1]].x, self.sets_rects[location[0]][location[1]].y)
                    new_piece = self.pieces[piece](color, pos, self.pieces_location)

                    self.pieces_location[location[0]][location[1]] = new_piece

    def draw_board(self):
        self.sets_rects = []
        by_row = 8
        by_column = 8
        sets_width = self.window_size[0] / by_row
        sets_height = self.window_size[1] / by_column
        set_color = True

        for x in range(by_column):
            row = []

            for y in range(by_row):
                pos_x = sets_width * y + y  # ???
                pos_y = sets_height * x + x  # ???

                color = (255, 255, 255) if set_color else (0, 0, 0)

                if self.selected_set is not None:
                    if self.selected_set == (x, y):
                        color = (0, 255, 0)

                if self.move_sets is not None:
                    if (x, y) in self.move_sets:
                        color = (0, 0, 255)

                rect = pygame.Rect(pos_x, pos_y, sets_width, sets_height)
                retangle = pygame.draw.rect(self.window, color, rect)
                row.append(retangle)

                set_color = not set_color

            set_color = not set_color
            self.sets_rects.append(row)

    def draw_pieces(self):
        for row in self.pieces_location:
            for piece in row:
                if piece is not None:
                    self.window.blit(piece.surf, piece.rect)
