import msvcrt
import os

from Area import Area
from Player import Player

complexities = [["Very easy", 0.9],
                ["Easy", 0.8],
                ["Normal", 0.7],
                ["Hard", 0.6],
                ["Harder", 0.5],
                ["Hardest", 0.4],
                ["Hardcore", 0.2],
                ["Almost impossible", 0.05]]


def select_option(options: list) -> int:
    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')
    return get_number(1, len(options)) - 1


def get_number(lowest, highest, message=None) -> int:
    number = None
    error_message = f"Bad value: select option from {lowest} to {highest}"
    while number is None or not (lowest <= number <= highest):
        try:
            if message is None:
                number = int(input().strip())
            else:
                number = int(input().strip(), message)
            if not (lowest <= number <= highest):
                print(error_message)
        except ValueError:
            print(error_message)
    return number


def act(area):
    char = ord(msvcrt.getch())
    if char == 72:
        area.move_player([0, -1])
    if char == 75:
        area.move_player([-1, 0])
    if char == 80:
        area.move_player([0, 1])
    if char == 77:
        area.move_player([1, 0])


def play():
    player = Player()
    os.system('cls')
    print('Select complexity:')
    options = [f'{name} (freedom: {int(complexity * 100)}%)'
               for name, complexity in complexities]
    area = Area(120, 20, complexities[select_option(options)][1], player)
    while player.area is not None:
        area.draw()
        act(area)
    if player.won:
        print("You won")
    else:
        print("Game over")


play()
