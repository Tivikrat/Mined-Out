from random import random

from entities.Empty import Empty
from entities.Exit import Exit
from entities.Field import Field
from entities.Mine import Mine
from entities.Player import Player
from entities.Wall import Wall


class Area:
    area = None
    player = None

    def __init__(self, width: int, height: int, freedom: float, player: Player):
        self.area = [[(Empty() if random() < freedom else Mine())
                      for _ in range(width)] for _ in range(height)]
        for index in [-2, -1, 0, 1]:
            for cell_index in range(width):
                if isinstance(self.area[index][cell_index], Mine):
                    self.area[index][cell_index] = Empty()
        for index in range(height):
            self.area[index][0] = self.area[index][-1] = Wall()
        for index in range(width):
            self.area[0][index] = self.area[-1][index] = Wall()
        self.area[0][width // 2] = Exit()
        self.area[-1][width // 2] = Empty()
        self.area[0][-1 + width // 2] = Exit()
        self.area[-1][-1 + width // 2] = Empty()
        if width % 2 == 1:
            self.area[0][1 + width // 2] = Exit()
            self.area[-1][1 + width // 2] = Empty()
        self.player = player
        player.area = self
        player.position = [len(self.area[0]) // 2, len(self.area) - 1]

    def count_mines(self, position):
        top = left = right = bottom = None
        if position[0] + 1 < len(self.area[0]):
            top = self.area[position[1]][position[0] + 1]
        if position[1] - 1 < len(self.area):
            left = self.area[position[1] - 1][position[0]]
        if position[1] + 1 < len(self.area):
            right = self.area[position[1] + 1][position[0]]
        if position[0] - 1 < len(self.area[0]):
            bottom = self.area[position[1]][position[0] - 1]
        return sum([1 for entity in [top, left, right, bottom] if
                    isinstance(entity, Mine)])

    def move_player(self, change):
        new_position = [self.player.position[0] + change[0],
                        self.player.position[1] + change[1]]
        if 0 <= new_position[0] < len(self.area[0]) \
                and 0 <= new_position[1] < len(self.area) \
                and not isinstance(self.area[new_position[1]][new_position[0]],
                                   Wall):
            self.player.position = new_position
            self.area[new_position[1]][new_position[0]].on_hover(self.player)
            self.area[new_position[1]][new_position[0]] = Field()

    def draw(self):
        print("\033[0;0H")
        for row_index, row in enumerate(self.area):
            for index, drawable in enumerate(row):
                if self.player.position == [index, row_index]:
                    self.player.draw()
                else:
                    drawable.draw()
            print()
