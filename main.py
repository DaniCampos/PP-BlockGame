#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

from Basic_Controller import Controller
from Menu import game_intro
from shapely.geometry import Point
from shapely.geometry import*
program = Controller(game_intro())


while True:
    program.update()

    pygame.time.wait(1000/30)


