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

    initial_pieces_loaction = {
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

            self.window.fill((255, 255, 255))
            self.draw_board()
            self.draw_pieces()

            pygame.display.update()
            pygame.time.Clock().tick(40)

        pygame.quit()

    def load_pieces(self):
        for x in range(8):
            row = []

            for y in range(8):
                row.append(None)

            self.pieces_location.append(row)

        for color in self.initial_pieces_loaction:
            for piece in self.initial_pieces_loaction[color]:
                for location in self.initial_pieces_loaction[color][piece]:
                    pos = (self.sets_rects[location[0]][location[1]].x, self.sets_rects[location[0]][location[1]].y)
                    new_piece = self.pieces[piece](color, pos)

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
