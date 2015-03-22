#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'aen'

import pygame
import sys
from pygame.locals import *


def pomodoro():
    pygame.init()
    #  set up the window
    font = pygame.font.Font(None, 72)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 153, 0)
    BLUE = (0, 0, 255)
    DISPLAY = pygame.display.set_mode((400, 300), 0, 32)

    background = pygame.Surface(DISPLAY.get_size())
    background = background.convert()
    background.fill(DARK_GREEN)

    pygame.display.set_caption('Pymodoro!')
    pomo = pygame.draw.circle(background, RED, (200, 120), 80, 0)
    text = font.render("25", 1, (255, 255, 255))
    background.blit(text, (173, 90))
    DISPLAY.blit(background, (0, 0))

    while True:  # main loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    pomodoro()