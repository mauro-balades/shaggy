import logging
from colorama import init, Fore, Style

# Initialize colorama for Windows support
init()

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('[*] %(message)s')

# Create a console handler and set the formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Set up color mappings
COLORS = {
    'DEBUG': Style.DIM + Fore.BLUE,
    'INFO': Style.NORMAL + Fore.GREEN,
    'WARNING': Style.NORMAL + Fore.YELLOW,
    'ERROR': Style.BRIGHT + Fore.RED,
    'CRITICAL': Style.BRIGHT + Fore.RED
}

# Custom logging levels with corresponding colors
logging.addLevelName(logging.DEBUG, f"{COLORS['DEBUG']}DEBUG{Style.RESET_ALL}")
logging.addLevelName(logging.INFO, f"{COLORS['INFO']}INFO{Style.RESET_ALL}")
logging.addLevelName(logging.WARNING, f"{COLORS['WARNING']}WARNING{Style.RESET_ALL}")
logging.addLevelName(logging.ERROR, f"{COLORS['ERROR']}ERROR{Style.RESET_ALL}")
logging.addLevelName(logging.CRITICAL, f"{COLORS['CRITICAL']}CRITICAL{Style.RESET_ALL}")

