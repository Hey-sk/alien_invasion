import pygame

class Ship:
    def __init__(self, ai_game):
        '''initialize screen and starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load ship and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        #movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update ship movement based on movement flag'''

        #update the ship's x value- not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
 
        #update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        #draw the screen in its current locaton
        self.screen.blit(self.image, self.rect)