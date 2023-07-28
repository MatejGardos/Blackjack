import pygame as pg
import random
import cfg

class CreateCard(pg.sprite.Sprite):
    def __init__(self, x, y, hidden=False):
        super().__init__()

        self.x = x
        self.y = y
        self.hidden = hidden

        self.value = random.randint(1, 13)
        self.type = random.choice(["Black Hearts", "Clubs", "Diamonds", "Red Hearts"])

        # Changing value of a card to a name
        self.card = self.value
        if self.card == 1:
            self.card = "A"
        if self.card == 11:
            self.card = "J"
        if self.card == 12:
            self.card = "K"
        if self.card == 13:
            self.card = "Q"

        short_cuts = {"Black Hearts": "H", "Clubs": "C", "Diamonds": "D", "Red Hearts": "H"}
        self.type_short =  short_cuts[self.type]

        self.value = min(self.value, 10)

        self.image = pg.image.load(f"assets/Pixel Classic Cards/{self.type}/{self.type_short}{self.card}.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() * cfg.CARD_SCALE, self.image.get_height() * cfg.CARD_SCALE)) # resizing
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.x, self.y)

        if hidden:
            self.image = pg.image.load("assets/Pixel Classic Cards/BackSide.png")
            self.image = pg.transform.scale(self.image, (self.image.get_width() * 1.35, self.image.get_height() * 1.21)) # resizing
            self.rect = self.image.get_rect()
            self.rect.bottomright = (self.x, self.y)

    def show(self):
        self.image = pg.image.load(f"assets/Pixel Classic Cards/{self.type}/{self.type_short}{self.card}.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() * cfg.CARD_SCALE, self.image.get_height() * cfg.CARD_SCALE)) # resizing
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.x, self.y)