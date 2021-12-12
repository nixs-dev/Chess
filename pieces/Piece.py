import pygame


class Piece(pygame.sprite.Sprite):

    pieces_icons_path = 'pieces_icons/'
    piece_size = (50, 70)
    
    def __init__(self, color, location, piece_name=''):
        super().__init__()

        sprite = pygame.image.load(self.pieces_icons_path + color + '/' + piece_name + '.png')
        sprite = pygame.transform.scale(sprite, self.piece_size)

        self.surf = pygame.surface.Surface(self.piece_size, pygame.SRCALPHA)
        self.surf.blit(sprite, (0, 0))
        self.rect = self.surf.get_rect(x=location[0], y=location[1])
