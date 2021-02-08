from unittest import TestCase

from cube import Cube


class TestCube(TestCase):
    """Test the Cube."""

    def test_constructor(self):
        """Test it gets the right data."""
        cube = Cube()
        self.assertEqual(cube.grid, [(0, 0, 0)] * 27)

    def test_data_parsing(self):
        """Test it correctly locates the lights."""
        cube = Cube()
        data = [
            [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [255, 0, 0]],
            ],
            [
                [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 255, 0], [0, 0, 0]],
            ],
            [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[255, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ],
        ]
        cube.display(data)
        self.assertEqual(
            cube.grid,
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [255, 0, 0],
                [0, 0, 0],
                [0, 255, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 255, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 255, 0],
                [0, 0, 0],
                [0, 0, 0],
                [255, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
        )
