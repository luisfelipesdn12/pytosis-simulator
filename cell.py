from random import randint
import pygame

class Cell():
    pos = None
    color = (219,224,204)
    window = None
    radius = 25

    def define_pos(self, actual_pos=None):
        if type(actual_pos) == tuple:
            x_actual = actual_pos[0]
            y_actual = actual_pos[1]

            range = 5
            x = randint(x_actual-range, x_actual+range)
            y = randint(y_actual-range, y_actual+range)
            xy = (x, y)
        else:
            xy = x, y = (300,300)

        return(xy)


    def draw(self, window):
        if window != None:
            for _ in range(5):
                    self.pos = self.define_pos((self.pos))
                    cell = pygame.draw.circle(
                        window,
                        self.color,
                        self.pos,
                        self.radius
                    )
        else: print("You have to define a window to draw.")
