from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.new_scoreboard()

    def new_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.new_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial", 18, "normal"))