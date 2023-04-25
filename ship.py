import pygame

class Ship:
    def __init__(self, ai_game):
        '''initialize screen and starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #draw the screen in its current locaton
        self.screen.blit(self.image, self.rect)