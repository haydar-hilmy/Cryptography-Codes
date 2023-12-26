import os

class Color:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    def clear_terminal():
        os_name = os.name
        if os_name == 'posix':  # Unix/Linux/MacOS
            os.system('clear')
        elif os_name == 'nt':  # Windows
            os.system('cls')
        else:
            print("\nNo OS suitable\n")