from unittest import TestCase

from cube import Cube, flatten, reorder


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


def test_flattening():
    """Test it flattens the 3x3x3 lists into a single list."""
    data = [[["foo", "bar", "baz"], [1, 2, 3], [True, False, None]]]
    assert flatten(data) == ["foo", "bar", "baz", 1, 2, 3, True, False, None]


def test_reorder():
    """Test it reorders a list."""
    data = list(
        map(lambda x: chr(x + 32), range(27))
    )  # the first 27 printable ASCII chars
    assert reorder(data) == [
        " ",
        "#",
        "&",
        "'",
        "$",
        "!",
        '"',
        "%",
        "(",
        "1",
        "0",
        "/",
        ",",
        "-",
        ".",
        "+",
        "*",
        ")",
        "2",
        "5",
        "8",
        "9",
        "6",
        "3",
        "4",
        "7",
        ":",
    ]
