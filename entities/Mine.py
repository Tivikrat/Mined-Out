from entities.Drawable import Drawable
from entities.Player import Player


class Mine(Drawable):
    symbol = "@"

    def on_hover(self, player: Player):
        player.destroy()
