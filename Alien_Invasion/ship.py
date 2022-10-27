import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__ (self,ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store the decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship position based on the movement flag"""
        # Update the ship's value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.setting.ship_speed
            
        
        #Update rect object from self.x
        self.rect.x = self.x
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    

    def blitime(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
