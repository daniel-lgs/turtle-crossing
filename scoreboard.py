from turtle import Turtle
FONT = ("ARIAL", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = -1
        self.setposition(-250, 250)
        self.update()

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER!", font=FONT, align="center")
