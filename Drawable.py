class Drawable:
    symbol = '.'
    color = None

    def draw(self):
        print(self.symbol, end='')

    def on_hover(self, player):
        pass
