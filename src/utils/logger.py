from enum import Enum
import random
import time
from src.utils.colors import Colors


class Logger:

    class Severity(Enum):
        INFO = "INFO"
        WARNING = "WARNING"
        ERROR = "ERROR"
        SUCCESS = "SUCCESS"

    @staticmethod
    def log(message: str, severity: Severity, end: str = "\n", flush: bool = False):

        if severity == severity.INFO:
            print(
                f"{Colors.BOLD}{Colors.INFO}[INFO]{Colors.ENDC} {message}",
                end=end,
                flush=flush,
            )
        if severity == severity.WARNING:
            print(
                f"{Colors.BOLD}{Colors.WARNING}[WARNING]{Colors.ENDC} {message}",
                end=end,
                flush=flush,
            )
        if severity == severity.ERROR:
            print(
                f"{Colors.BOLD}{Colors.FAIL}[ERROR]{Colors.ENDC} {message}",
                end=end,
                flush=flush,
            )
        if severity == severity.SUCCESS:
            print(
                f"{Colors.BOLD}{Colors.SUCCESS}[INFO]{Colors.ENDC} {message}",
                end=end,
                flush=flush,
            )

    @staticmethod
    def print_dot_animation():
        for _ in range(random.randint(3, 5)):
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.3)
            print("\b\b\b   \b\b\b", end="", flush=True)
        print("...", end="", flush=True)

    @staticmethod
    def print_separator(self):
        print("=====================================")
