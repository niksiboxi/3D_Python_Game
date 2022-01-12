import pygame
import sys
import os
sys.path.insert(0, './pvp_raycast')
from game import Game
import const as const
import socket
import time
import pickle
from sprite import Sprite
import threading 

pygame.init()

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))
clock = pygame.time.Clock()
game = Game()

game.game_map = const.game_map

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Main loop
while not game.done:
    events = pygame.event.get()
    game.draw(screen)
    game.input_handle()
    pygame.display.flip()
    clock.tick()
pygame.quit()