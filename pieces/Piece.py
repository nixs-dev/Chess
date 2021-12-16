import pygame


class Piece(pygame.sprite.Sprite):

    pieces_matrix = []
    pieces_icons_path = 'pieces_icons/'
    piece_size = (50, 70)
    first_move = True
    color = ''

    def __init__(self, color, location, pieces_matrix, piece_name=''):
        super().__init__()

        self.color = color
        self.first_move = True
        self.pieces_matrix = pieces_matrix

        sprite = pygame.image.load(self.pieces_icons_path + color + '/' + piece_name + '.png')
        sprite = pygame.transform.scale(sprite, self.piece_size)

        self.surf = pygame.surface.Surface(self.piece_size, pygame.SRCALPHA)
        self.surf.blit(sprite, (0, 0))
        self.rect = self.surf.get_rect(x=location[0], y=location[1])

    def where_am_i(self):
        current_pos = ()

        for x, row in enumerate(self.pieces_matrix):
            if self in row:
                current_pos = (x, row.index(self))

        return current_pos

    def move_ways(self):
        available_places = []

        return available_places

    def move(self, coordinate, in_view_coordinte):
        if self.first_move:
            self.first_move = False

        current_pos = self.where_am_i()

        self.pieces_matrix[current_pos[0]][current_pos[1]] = None
        self.pieces_matrix[coordinate[0]][coordinate[1]] = self

        self.rect.x = in_view_coordinte[0]
        self.rect.y = in_view_coordinte[1]

        return self.pieces_matrix
