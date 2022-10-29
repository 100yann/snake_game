from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align="center", font=('Courier', 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Ariel', 35, "normal"))

    def addscore(self):
        self.clear()
        self.score += 1
        self.goto(0, 260)
        self.update_scoreboard()