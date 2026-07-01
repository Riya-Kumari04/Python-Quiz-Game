class Colors:

    RESET = "\033[0m"

    BOLD = "\033[1m"

    RED = "\033[91m"

    GREEN = "\033[92m"

    YELLOW = "\033[93m"

    BLUE = "\033[94m"

    CYAN = "\033[96m"

    WHITE = "\033[97m"

    GRAY = "\033[90m"


def difficulty_color(level):

    if level == "Easy":
        return Colors.GREEN

    elif level == "Medium":
        return Colors.YELLOW

    elif level == "Hard":
        return Colors.RED

    return Colors.WHITE