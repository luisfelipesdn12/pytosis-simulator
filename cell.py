# Modules:
import pygame
from random import randint
from json import load

with open("preferences.json", "r") as preferences_json:
    preferences = load(preferences_json)["cell"]

class Cell():
    # Default variables for the objects:
    pos = None
    window = None
    color = tuple(
        rgb for rgb in preferences["color"].values()
    )
    radius = preferences["radius"]

    def define_pos(self, actual_pos=None, how_far = 5):
        '''
        Arguments:
            `actual_pos`: a tuple that contains two values
        representing a position 2D (x, y) or None (by default);
            `how_far`: how many pixel far from the initial
        position can be retuned, (5 pixels by default).

        Returns: other (x, y) position tuple, 0 to `how_far` far
        from the initial (x, y) position, or a default value of 
        (300, 300) if the `actual_pos` was None.
        '''
        if isinstance(actual_pos, tuple):
            x_actual = actual_pos[0]
            y_actual = actual_pos[1]

            x = randint(x_actual-how_far, x_actual+how_far)
            y = randint(y_actual-how_far, y_actual+how_far)
            xy = (x, y)
        else:
            xy = x, y = (300,300)

        return(xy)


    def draw(self, window):
        '''
        Given: a pygame.window() object.
        Draw the cell in the screen with the attributes:
        color, pos and radius defined above.
        '''
        if window is not None:
            for _ in range(5):
                    self.pos = self.define_pos((self.pos))
                    cell = pygame.draw.circle(
                        window,
                        self.color,
                        self.pos,
                        self.radius
                    )
