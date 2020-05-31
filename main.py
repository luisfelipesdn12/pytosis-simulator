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

# cells variable is a list that contains all the Cell() objects
# it will be used to "plot" all the itens in the runtime bellow
cells = [Cell() for _ in range(initial_population)]

# Properties of runtime:
frame_rate = 0.07
reproduce_in_n_frames = 100

frame = 1
mouse_was_pressed = False

# Runtime:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    window.fill(color4bg)

    # once the mouse pressed, it will be true forever in runtime
    # it is used to start the simulation when identif a click
    if pygame.mouse.get_pressed()[0] == 1: mouse_was_pressed = True

    if mouse_was_pressed:
        population = len(cells)

        # Reprodution:
        # happen each `reproduce_in_n_frames` frames 
        if frame%reproduce_in_n_frames == 0:
            # this loop runs for each existing cell
            for c in range(population):
                # the existing cell is attributed to this variable
                cellMother = cells[c]
                # create a Cell() object, with default position
                cellCopy = Cell()
                # change that position to the mother position
                cellCopy.pos = cellMother.pos
                # put the new cell to the the population (cells list)
                cells.append(cellCopy)

        for cell in cells:
            cell.draw(window)

        time.sleep(frame_rate)
        print(f'FRAME: {frame}')
        print(f'POPULATION: {population}')
        print(f'FRAME_RATE = {frame_rate}')
        print(f'REPRODUCE_EACH = {reproduce_in_n_frames} frames')
        print()
        frame += 1
    pygame.display.update()
