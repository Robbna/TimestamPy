from enum import Enum


class Colors(Enum):
    BOLD = "\033[1m"
    ENDC = "\033[0m"
    FAIL = "\033[91m"
    INFO = "\033[96m"
    PURPLE = "\033[95m"
    SUCCESS = "\033[92m"
    UNDERLINE = "\033[4m"
    WARNING = "\033[93m"
    WHITE = "\033[97m"


class RGBColors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    COLORS = [WHITE, BLACK, RED, GREEN, BLUE]
