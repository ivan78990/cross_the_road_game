from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.high_level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.level > self.high_level:
            self.high_level = self.level
        self.goto(-200, 250)
        self.write(arg=f"Current Level: {self.level}\nHighest level: {self.high_level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.level = 1
        self.update_scoreboard()

