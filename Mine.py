from Drawable import Drawable
from Player import Player


class Mine(Drawable):
    symbol = "@"

    def on_hover(self, player: Player):
        player.destroy()
