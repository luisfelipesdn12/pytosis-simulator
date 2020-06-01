# Modules:
import pygame, time, random, math, json
# Classes:
from cell import Cell

# Fetch the preferences in the json file:
with open("preferences.json", "r") as preferences_json:
    preferences = json.load(preferences_json)["main"]

# Properties variables:
title = preferences["title"]
window_icon = pygame.image.load(preferences["icon_dir"])
window_size = width, height = tuple(
    i for i in list(preferences["window_size"].values())
)
window_is_resizable = preferences["is_resizable"]
color4bg = tuple(
    rgb for rgb in preferences["color4bg"].values()
)
initial_population = preferences["initial_population"]
overpopulation_point = preferences["overpopulation_point"]

# Aplication for properties variables:
if window_is_resizable: window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
else: window = pygame.display.set_mode(window_size)
pygame.display.set_icon(window_icon)
pygame.display.set_caption(title)

if overpopulation_point:
    def returnMaxPopulation(window_size:tuple, cell_radius):
        '''
        Given: the tuple of window size with two
        values representing the width and height;
        the cell object default radius.

        Returns: the minimum n of cells to fill the
        screen, then, the max n of cells to not be
        overpopulated.
        '''
        width, height = window_size
        cell_diameter = cell_radius*2

        return(
            (width*height) / (cell_radius**2)
        )
    
    max_population = returnMaxPopulation(
        window_size, Cell().radius
    )

    deaths_percent_in_overpopulation_control = preferences[
        "deaths_percent_in_overpopulation_control"
    ]

# cells variable is a list that contains all the Cell() objects
# it will be used to "plot" all the itens in the runtime bellow
cells = [Cell() for _ in range(initial_population)]

# Properties of runtime:
frame_rate = preferences["frame_rate"]
reproduce_in_n_frames = preferences["reproduce_in_n_frames"]
death_in_n_frames = preferences["death_in_n_frames"]
# the variables bellow is apercentage value
# and values must be like (0.27)
# the final value must be >= 1.00, otherwise
# the program breaks in the runtime   
mortality_rate = preferences["mortality_rate"]
reproduction_rate = preferences["reproduction_rate"]

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
        # delete random cells of the population following
        # the value assigmented in ´mortality_rate´ and
        # happen each ´death_in_n_frames´ frames
        if frame%death_in_n_frames == 0:
            # the loop runs for ´mortalit_rate´ percet of 
            # population breaks case the ´mortality_rate´ > 1.00
            cells_to_be_killed = math.ceil(population*mortality_rate)
            for _ in range(cells_to_be_killed):
                cell_to_be_killed = random.choice(cells)
                cells.remove(cell_to_be_killed)
        else: cells_to_be_killed = 0

        # Overpopulation control:
        # delete random cells of the population following
        # the value of assigmented in `deaths_percent_in_
        # overpopulation_control` and happen when the cells
        # fill the scren as defined in returnMaxPopulation()
        if overpopulation_point and population > max_population:
            catastrofe_victims = math.ceil(
                population * deaths_percent_in_overpopulation_control
            )

            for _ in range(catastrofe_victims):
                victim = random.choice(cells)
                cells.remove(victim)
        else: catastrofe_victims = 0

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
        deaths += (cells_to_be_killed + catastrofe_victims)

    pygame.display.update()
