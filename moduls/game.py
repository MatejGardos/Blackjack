import pygame as pg
import cfg
from .cards import CreateCard


class Game:
    def __init__(self, player_group, dealer_group):
        self.player_group = player_group
        self.dealer_group = dealer_group
        self.font = pg.font.Font("assets/Font/Franxurter.ttf", 50)

    def draw_cards(self, surface):
        """drawing sprite groups"""
        self.player_group.draw(surface)
        self.dealer_group.draw(surface)

    def start_round(self):
        self.player_group.empty()
        self.dealer_group.empty()

        for i in range(2):
            # player cards
            card = CreateCard( (cfg.WIDTH//2) + ((len(self.player_group))*50) , cfg.HEIGHT-160)
            self.player_group.add(card)

            # dealer cards
            card = CreateCard( (cfg.WIDTH//2) + ((len(self.dealer_group))*50), 150, hidden= True if i % 2 != 0 else False)
            self.dealer_group.add(card)        

    def hit(self, card_group):
        """create new card"""
        height = cfg.HEIGHT-160 if card_group == self.player_group else 150

        card = CreateCard( (cfg.WIDTH//2) + ((len(card_group))*50) , height)
        card_group.add(card)

    def check_sum(self, card_group):
        """sum up all cards and check value for ace"""
        total = 0
        for card in card_group:
            total += card.value

        # check if Ace can be 11
        for card in card_group:
            if card.card == "A":
                if total + 10 <= 21:
                    total += 10

        return total


    def check_bust(self):
        if self.check_sum(self.player_group) > 21:
            return True
        return False
    
    def who_won(self):
        if self.check_sum(self.player_group) > 21:
            return "Bust!"
        elif len(self.player_group) == 2 and self.check_sum(self.player_group) == 21:
            return "Blackjack!"
        elif self.check_sum(self.dealer_group) > 21:
            return "Player won!"    
        elif self.check_sum(self.dealer_group) < self.check_sum(self.player_group):
            return "Player won!"
        elif self.check_sum(self.dealer_group) > self.check_sum(self.player_group):
            return "Dealer won!" 
        elif self.check_sum(self.dealer_group) == self.check_sum(self.player_group):
            return "Draw!"
        
    def result_screen(self, result_text, surface):
        # game result
        text =  self.font.render(result_text, True, cfg.BLACK)
        rect = text.get_rect()
        rect.center = (cfg.WIDTH//2-20, cfg.HEIGHT//2-60)
        surface.blit(text, rect)

        # Dealer points
        dealer_text =  self.font.render(f"{self.check_sum(self.dealer_group)}", True, cfg.BLACK)
        dealer_rect = dealer_text.get_rect()
        dealer_rect.center = (cfg.WIDTH//2-20, cfg.HEIGHT//2-120)
        surface.blit(dealer_text, dealer_rect)

        # Player points
        player_text = self.font.render(f"{self.check_sum(self.player_group)}", True, cfg.BLACK)
        player_rect = player_text.get_rect()
        player_rect.center = (cfg.WIDTH//2-20, cfg.HEIGHT//2)
        surface.blit(player_text, player_rect)