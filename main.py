# Modules:
import pygame, time, random, math
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
death_in_n_frames = 200
# the variables bellow is apercentage value
# and values must be like (0.27), (27/100) etc
# the final value must be >= 1.00, otherwise
# the program breaks in the runtime   
mortality_rate = 0.10 
reproduction_rate = 85/100

frame = 1
deaths = 0
reproductions = 0
mouse_was_pressed = False

print("\n || CLICK IN THE WINDOW TO START || \n")
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
        # create a new child cell for each Mother cells
        # happen each `reproduce_in_n_frames` frames 
        if frame%reproduce_in_n_frames == 0:
            # this loop runs for each existing cell if the reproduction rate == 1.00,
            # otherwise, runs for `reproduction_rate` percent of cells
            # the loop breaks case the ´reproduction_rate´ > 1.00
            cells_to_be_mothers = math.ceil(population*reproduction_rate)
            for c in range(cells_to_be_mothers):
                # the existing cell is attributed to this variable
                cellMother = cells[c]
                # create a Cell() object, with default position
                cellCopy = Cell()
                # change that position to the mother position
                cellCopy.pos = cellMother.pos
                # put the new cell to the the population (cells list)
                cells.append(cellCopy)
        else: cells_to_be_mothers = 0

        # Death:
        # delete random cells of the population follows
        # the value of assigmented in ´mortality_rate´
        # happen each ´death_in_n_frames´ frames
        if frame%death_in_n_frames == 0:
            # the loop runs for ´mortalit_rate´ percet of 
            # population breaks case the ´mortality_rate´ > 1.00
            cells_to_be_killed = math.ceil(population*mortality_rate)
            for _ in range(cells_to_be_killed):
                cell_to_be_killed = random.choice(cells)
                cells.remove(cell_to_be_killed)
        else: cells_to_be_killed = 0

        # Plots
        for cell in cells:
            cell.draw(window)

        # Logs:
        time.sleep(frame_rate)

        log_strings = [
            f'FRAME: {frame}',
            f'POPULATION: {population}',
            f'REPRODUCTIONS: {reproductions}',
            f'DEATHS: {deaths}',
            f'FRAME_RATE = {frame_rate}',
            f'REPRODUCE_EACH = {reproduce_in_n_frames} frames',
            f'REPRODUTION_RATE = {reproduction_rate}',
            f'MORTALITY_RATE = {mortality_rate}',
            f'DEATH_EACH = {death_in_n_frames} frames'
        ]

        for log_string in log_strings: print(log_string)
        print('\n=======================\n')

        frame += 1
        reproductions += cells_to_be_mothers
        deaths += cells_to_be_killed

    pygame.display.update()
