import pygame
import sys
import os
from pygame.locals import *
import func

pygame.init()

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.display.set_caption('SheetPost')
font = pygame.font.SysFont('Lucida Console', 20)


class Menu:

    scr_res, scr_type = func.toggle_fs()
    screen = pygame.display.set_mode(scr_res, scr_type)

    def draw_text(self, text, font, color, surface, x, y, centered = None):
        if centered:
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect(centerx=self.scr_res[0] // 2, centery=y)
            surface.blit(textobj, textrect)
        else:
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)


    def blank(self, name):
        self.screen.fill(pygame.Color('#ffffff'))
        self.draw_text(name, font, pygame.Color('#000000'), self.screen, 20, 20)


    def draw_button(self, pos, res, text):
         button = pygame.Rect(pos, res)
         pygame.draw.rect(self.screen, pygame.Color('#000000'), button, 3)
         text = font.render(text, 1, pygame.Color('#000000'))
         text_pos = text.get_rect(centerx=pos[0] + res[0] // 2, centery=pos[1] + res[1]//2)
         self.screen.blit(text, text_pos)
         return button
    

    def if_click(self, button, event):

        mx, my = pygame.mouse.get_pos()
        click = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if button.collidepoint((mx, my)):
                if click:
                    return click
        click = False     
        return click


    def main_menu(self):
        while True:
    
            self.blank('Main Menu')
            logo = pygame.image.load(os.path.join('SheetPost', 'data', 'img', 'logo.png'))
            logo.convert()
            self.screen.blit(logo, (0, 0))
    
            start_button = self.draw_button((50, self.scr_res[1]//2-60), (150, 50), 'Start')
            options_button = self.draw_button((50, self.scr_res[1]//2), (150, 50), 'Options')
            credits_button = self.draw_button((50, self.scr_res[1]//2+60), (150, 50), 'Credits')

            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if self.if_click(start_button, event):
                    self.game()
                if self.if_click(options_button, event):
                    self.options()
                if self.if_click(credits_button, event):
                    self.credits_()
    
            pygame.display.update()
            mainClock.tick(60)
    
    def game(self):
        is_running = True
        while is_running:

            self.blank('Game')

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_running = False
            
            pygame.display.update()
            mainClock.tick(60)
    
    def options(self):
        is_running = True
        while is_running:

            self.blank('Options')

            fullsreen_button = self.draw_button((50, self.scr_res[1]//2-60), (150, 50), 'Fullscreen')
            back_button = self.draw_button((50, self.scr_res[1]-100), (150, 50), 'Back')

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_running = False
                if self.if_click(fullsreen_button, event):
                    self.scr_res, self.scr_type = func.toggle_fs(event)
                    pygame.display.set_mode(self.scr_res, self.scr_type)
                if self.if_click(back_button, event):
                    is_running = False

            pygame.display.update()
            mainClock.tick(60)


    def credits_(self):
        is_running = True
        while is_running:

            self.blank('Credits')

            self.draw_text('Created by T4', font, pygame.Color('#000000'), self.screen, 0, self.scr_res[1] // 4, True)
            self.draw_text('Special thanks:', font, pygame.Color('#000000'), self.screen, 0, self.scr_res[1] // 3, True)
            self.draw_text('nemedved 4 being my gf <3', font, pygame.Color('#000000'), self.screen, 0, self.scr_res[1] // 3 + 40, True)
            

            back_button = self.draw_button((50, self.scr_res[1]-100), (150, 50), 'Back')

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_running = False
                if self.if_click(back_button, event):
                    is_running = False
            
            pygame.display.update()
            mainClock.tick(60)
mn = Menu()
mn.main_menu()