import itertools

from utils import get_grid


class Cube:
    """Class representing the Cube::Bit."""

    def __init__(self):
        """Construct."""
        self.grid = get_grid()

    def display(self, colours):
        """Realign and display a 3x3 grid of colours."""
        fixed_colours = reorder(flatten(colours))
        for i in range(27):
            self.grid[i] = fixed_colours[i]

        self.grid.show()


def reorder(colours):
    """
    Reorder the colours to fit the Cube::Bit's weird space-filling curve.

    This is horribly hard-coded - if I ever get a cube that's not a 3x3x3, I'll
    do it properly
    """
    indeces = [
        0,
        3,
        6,
        7,
        4,
        1,
        2,
        5,
        8,
        17,
        16,
        15,
        12,
        13,
        14,
        11,
        10,
        9,
        18,
        21,
        24,
        25,
        22,
        19,
        20,
        23,
        26,
    ]
    reordered = []
    for i in range(27):
        reordered.append(colours[indeces[i]])
    return reordered


def flatten(colours):
    """Flatten the cubular array into one long list."""
    return list(itertools.chain.from_iterable(itertools.chain.from_iterable(colours)))
