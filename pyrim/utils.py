#Pyrim-New/utils.py
import pyfiglet
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Define a function to add spacing and separators to text
def format_text(text):
    return f"{'*' * 50}\n{text}\n{'*' * 50}\n"