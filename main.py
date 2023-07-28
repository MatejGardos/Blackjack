import pygame as pg
from moduls import *
import cfg

pg.init()

clock = pg.time.Clock()
font = pg.font.Font("assets/Font/Franxurter.ttf", 50)

screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
pg.display.set_caption("Blackjack")

card_sound = pg.mixer.Sound("assets/sound/CardSound.wav")

# Sprites Group
player_group = pg.sprite.Group()
dealer_group = pg.sprite.Group()

# Buttons
button_list = []
hit_button = Button(screen, "Hit", cfg.WIDTH//2 - 180, cfg.HEIGHT-100)
button_list.append(hit_button)
stand_button = Button(screen, "Stand", cfg.WIDTH//2, cfg.HEIGHT-100)
button_list.append(stand_button)


game = Game(player_group, dealer_group)
game.start_round()
card_sound.play()

end_round = False
running = True
while running:
    button_pressed = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            button_pressed = True
               

    screen.fill(cfg.BG_COLOR)
    pg.draw.rect(screen, cfg.HUD_COLOR, (0, cfg.HEIGHT-140, cfg.WIDTH,cfg.HEIGHT))
    pg.draw.line(screen, cfg.BLACK, (0, cfg.HEIGHT-140), (cfg.WIDTH, cfg.HEIGHT-140), 2)

    # updatig and drawing buttons
    for button in button_list:
        if button.update(button_pressed):
            if button.txt == "Hit":
                game.hit(player_group)
                card_sound.play()
            
            elif button.txt == "Stand":
                end_round = True
                card_sound.play()
                while game.check_sum(dealer_group) < 17:
                    game.hit(dealer_group)

        button.draw()

    game.draw_cards(screen)

    if end_round or game.check_bust() or game.check_sum(player_group) == 21:
        for card in dealer_group:
            card.show()

        end_round = False
        result_text = game.who_won()

        game.draw_cards(screen)

        paused = True
        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    paused = False
                    running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    paused = False
                    game.start_round()
                    card_sound.play()

                game.result_screen(result_text, screen)

                clock.tick(cfg.FPS)
                pg.display.update()

    clock.tick(cfg.FPS)
    pg.display.update()

pg.quit()