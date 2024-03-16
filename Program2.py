import pyfiglet
import time
from colorama import Fore


def print_with_animation(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()


def print_ascii_art(text, font='isometric1', color=Fore.YELLOW, width=150, delay=0.001):
    ascii_art = pyfiglet.figlet_format(text,font=font, width=width)
    for line in ascii_art.split('\n'):
        print_with_animation(line, color, delay)


name = input("Enter your name: ")
dream_job = input("What is your dream job? ")

print_with_animation("Welcome, {}!".format(name), Fore.GREEN)
print_with_animation("Your dream job is: {}".format(dream_job), Fore.BLUE)

print_ascii_art(name, color=Fore.CYAN, width=200, delay=0.0001)
print_ascii_art(dream_job, color=Fore.MAGENTA, width=240, delay=0.0001)
