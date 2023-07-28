import pygame as pg
import cfg

class Button():
    def __init__(self, surface, txt, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.txt = txt
        self.button_color = cfg.BUTTON_COLOR
        self.font = pg.font.Font("assets/Font/Franxurter.ttf", 50)
        
        
        self.text = self.font.render(txt, True, cfg.BLACK)
        self.rect = self.text.get_rect()
        self.rect.center = (x+75,y+35)
        self.surface.blit(self.text, self.rect)



    def update(self, button_pressed):
        """change color of button if mouse is hovering and check if it is pressed"""
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.button_color = (90, 90, 90)
            if button_pressed:
                return True

        else:
            self.button_color = cfg.BUTTON_COLOR


    def draw(self):
        pg.draw.rect(self.surface, self.button_color, (self.x, self.y, 150,70))
        pg.draw.rect(self.surface, cfg.BLACK, (self.x, self.y, 150,70), 2)
        self.surface.blit(self.text, self.rect)