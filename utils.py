import platform

if "arm" in platform.platform():  # nocov
    import board  # pylint: disable=E0401
    from neopixel import NeoPixel  # pylint: disable=E0401


def get_grid():
    """Return real or fake pixels depending on our platform."""
    if "arm" in platform.platform():
        return NeoPixel(board.D18, 27, auto_write=False)  # nocov
    else:
        return FakeGrid(27)


class FakeGrid(list):
    """Fake Cube::Bit for testing."""

    def __init__(self, length):  # pylint: disable=W0231
        """Construct."""
        self.length = length
        for _ in range(self.length):
            self.append((0, 0, 0))

    def show(self):
        """Pretend to show the colours."""
        # pass
