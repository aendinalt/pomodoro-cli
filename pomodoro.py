#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'aen'

import pygame
import sys
from pygame.locals import USEREVENT, QUIT, MOUSEBUTTONDOWN


def pomodoro():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
    pygame.init()

    #  set up the window
    font = pygame.font.Font('freesansbold.ttf', 48)  # initialize a font

    #  define a colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)
    red = (255, 0, 0)
    gree = (0, 255, 0)
    dark_green = (0, 100, 0)
    blue = (0, 0, 255)

    #  define a sounds
    global pomo_start_sound, pomo_tick_sound, pomo_end_sound
    pomo_start_sound = pygame.mixer.Sound('sounds/pomo_start.wav')
    pomo_tick_sound = pygame.mixer.Sound('sounds/pomo_tick.wav')
    pomo_end_sound = pygame.mixer.Sound('sounds/pomo_ring.wav')

    #  define a defaults
    pomodoro_time = 25
    d_width = 400
    d_height = 300
    image_dir = 'images/'
    start_icon_x = 10
    start_icon_y = 10
    stop_icon_x = d_width - 10 - 64
    stop_icon_y = 10
    in_pomodoro = False

    #  create main window
    screen = pygame.display.set_mode((d_width, d_height), 0, 32)
    pygame.display.set_caption('Pymodoro!')
    pomo_start_icon = pygame.image.load(image_dir + 'pomo_start.png')
    pomo_stop_icon = pygame.image.load(image_dir + 'pomo_stop.png')
    icon = pygame.image.load(image_dir + 'largeicon.png')
    pygame.display.set_icon(icon)

    #  create background
    background = pygame.Surface(screen.get_size())

    while True:  # main loop

        for event in pygame.event.get():
            # print event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_x = event.pos[0]
                    click_y = event.pos[1]
                    if click_on_start(click_x, click_y, start_icon_x, start_icon_y) and not in_pomodoro:
                        timeleft = pomodoro_run(pomodoro_time)
                        in_pomodoro = True
                    elif click_on_stop(click_x, click_y, stop_icon_x, stop_icon_y) and in_pomodoro:
                        pomodoro_stop()
                        in_pomodoro = False

            if event.type == USEREVENT + 1:
                timeleft -= 1
                text = font.render(str(timeleft), 1, dark_green)
                if timeleft == 0:
                    pomodoro_end()
                    in_pomodoro = False

            if event.type == USEREVENT +2:
                pomo_tick_sound.play()

        # draw section
        background.fill(dark_green)
        background.blit(icon, ((d_width-256)/2, (d_height-256)/2))
        if in_pomodoro:
            background.blit(pomo_stop_icon, (stop_icon_x, stop_icon_y))
            text = font.render(str(timeleft), 1, dark_green)
            background.blit(text, ((d_width-54)/2, (d_height-50)/2))
        elif not in_pomodoro:
            background.blit(pomo_start_icon, (start_icon_x, start_icon_y))

        background = background.convert()
        screen.blit(background, (0, 0))

        pygame.display.flip()
        pygame.display.update()


def click_on_start(click_x, click_y, start_icon_x, start_icon_y):
    if (start_icon_x <= click_x <= start_icon_x + 64) \
            and (start_icon_y <= click_y <= start_icon_y + 64):
        return True
    else:
        return False


def click_on_stop(click_x, click_y, stop_icon_x, stop_icon_y):
    if (stop_icon_x <= click_x <= stop_icon_x + 64) \
            and (stop_icon_y <= click_y <= stop_icon_y + 64):
        return True
    else:
        return False


def pomodoro_run(pomodoro_time):
    pomo_start_sound.play()
    timeleft = pomodoro_time
    pygame.time.set_timer(USEREVENT + 1, 1000 * 60)
    pygame.time.set_timer(USEREVENT + 2, 867)
    return timeleft


def pomodoro_stop():
    pygame.time.set_timer(USEREVENT + 1, 0)
    pygame.time.set_timer(USEREVENT + 2, 0)


def pomodoro_end():
    pomo_end_sound.play()
    pomodoro_stop()


if __name__ == '__main__':
    pomodoro()