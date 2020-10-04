import pygame
import ctypes

pygame.init

frame = pygame.NOFRAME
clock = pygame.time.Clock()

#Fullscreen toggle
def toggle_fs(event = None):
    global frame
    window = (800, 600)
    fs_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

    try:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if frame == pygame.NOFRAME:
                pygame.display.set_mode(fs_res,pygame.FULLSCREEN)
                frame = pygame.FULLSCREEN
                return fs_res, frame
                
            elif frame == pygame.FULLSCREEN:
                pygame.display.set_mode(window, pygame.NOFRAME)
                frame = pygame.NOFRAME
                return window, frame
    except AttributeError:
        return window, frame


#Screen Update
def screen_update(window, manager):
    global clock

    time_delta = clock.tick(60)/1000.0

    manager.update(time_delta)
    manager.draw_ui(window)

    pygame.display.update()