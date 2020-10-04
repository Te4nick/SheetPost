import pygame
import pygame_gui
import ctypes
import os
import menus
import func

pygame.init()

# Vars
pygame.display.set_caption('SheetPost')
screen = pygame.display.set_mode((800,600), pygame.NOFRAME)
mainClock = pygame.time.Clock()

is_running = True


# Event Handler
def event_handler(event):
    global is_running, fs, manager, window

    if event.type == pygame.QUIT:
            is_running = False
    elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
    


#menus.Menu.main()
# Main Loop
while is_running:
    
    for event in pygame.event.get():
        event_handler(event)
        
        #menus.manager.process_events(event)
        mainClock.tick(60)
