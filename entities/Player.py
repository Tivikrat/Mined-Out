from entities.Drawable import Drawable


class Player(Drawable):
    area = None
    position = None
    won = None

    def draw(self):
        self.symbol = self.area.count_mines(self.position)
        super().draw()

    def destroy(self):
        self.area = None
        self.won = False

    def win(self):
        self.area = None
        self.won = True
