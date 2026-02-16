import numpy as np

class Arclogic:

    @staticmethod
    def background(grid, bg_colour=0):
        coords = np.argwhere(grid!=bg_colour)
        if coords.size == 0: return grid
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)
        return grid[y_min:y_max+1, x_min:x_max+1]

    @staticmethod
    def replace_colour(grid, bg_color=0):
        objects=[]
        unique_colors = np.unique(grid)
        for color in unique_colors:
            if color == bg_color: continue
            mask = (grid==color)
            objects.append((color, mask))
        return objects

    @staticmethod
    def replace_color(grid, old_colour, new_color):
        new_grid = np.copy(grid)
        new_grid[grid==old_colour] = new_color
        return new_grid