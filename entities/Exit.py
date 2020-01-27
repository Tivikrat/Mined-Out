from entities.Drawable import Drawable


class Exit(Drawable):
    symbol = ' '

    def on_hover(self, player):
        player.win()
