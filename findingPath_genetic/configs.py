import pygame as pg

#changeable
screen_width = 500
screen_height = 1000
fps = 60

DNA_length = 1500
number_population = 2
mutation = 0.01
speed = 2

#un-changeable
wall_list = pg.sprite.Group()
good_wall_list = pg.sprite.Group()