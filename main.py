# Modules:
import pygame, time
# Classes:
from cell import Cell

# Properties variables:
title = "Simulador de mitose"
window_icon = pygame.image.load('./icons/cells.png')
window_size = width, height = (600, 600)
window_is_resizable = False
color4bg = (78,87,117)
initial_population = 1

# Aplication for properties variables:
if window_is_resizable: window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
else: window = pygame.display.set_mode(window_size)
pygame.display.set_icon(window_icon)
pygame.display.set_caption(title)
window.fill(color4bg)
cells = [Cell() for _ in range(initial_population)]

sleep_time = 0.07
c = 1
reproduce_in_n_frames = 100
mouse_was_pressed = False    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    window.fill(color4bg)

    if pygame.mouse.get_pressed()[0] == 1: mouse_was_pressed = True

    if mouse_was_pressed:
        population = len(cells)
        if c%reproduce_in_n_frames == 0:
            for c in range(population):
                cellMother = cells[c]
                cellCopy = Cell()
                cellCopy.pos = cellMother.pos
                cells.append(cellCopy)

        for cell in cells:
            cell.draw(window)

        time.sleep(sleep_time)
        print(f'CELLS = {population}')
        print(f'SLEEP_TIME = {sleep_time}')
        print()
        c += 1
    pygame.display.update()
