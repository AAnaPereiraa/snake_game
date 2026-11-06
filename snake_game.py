from turtle import Screen
import time
import tkinter as tk
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ana the Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


def ask_play_again():
    root = screen.getcanvas().winfo_toplevel()
    dialog = tk.Toplevel(root)
    dialog.title("Game Over")
    dialog.resizable(False, False)
    dialog.transient(root)
    dialog.attributes("-topmost", True)

    choice = {"again": False}

    def choose(again):
        choice["again"] = again
        dialog.destroy()

    tk.Label(dialog, text="Play again?").pack(padx=24, pady=(16, 8))
    buttons = tk.Frame(dialog)
    buttons.pack(padx=24, pady=(0, 16))
    yes = tk.Button(buttons, text="Yes", width=8, command=lambda: choose(True))
    no = tk.Button(buttons, text="No", width=8, command=lambda: choose(False))
    yes.pack(side="left", padx=(0, 8))
    no.pack(side="left")

    dialog.bind("<Return>", lambda event: choose(True))
    dialog.bind("<Escape>", lambda event: choose(False))
    dialog.protocol("WM_DELETE_WINDOW", lambda: choose(False))

    dialog.update_idletasks()
    x = root.winfo_rootx() + max(0, (root.winfo_width() - dialog.winfo_width()) // 2)
    y = root.winfo_rooty() + max(0, (root.winfo_height() - dialog.winfo_height()) // 2)
    dialog.geometry(f"+{x}+{y}")
    dialog.grab_set()
    yes.focus_set()
    root.wait_window(dialog)
    screen.listen()
    return choice["again"]


screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.listen()

playing = True
while playing:
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.13)

        #DETECT WALL before moving, so the snake is not drawn past the edge

        if snake.will_hit_wall():
            game_on = False
            score.game_over()
            continue

        snake.move()

        #DETECT FOOD

        if food.distance(snake.head) < 15:
            food.food_position()
            score.score_count()
            snake.grow_snake()

        #DETECT SNAKE

        for snake_parts in snake.segments[1::]:
            if snake.head.pos() == snake_parts.pos():
                game_on = False
                score.game_over()

    screen.update()
    if ask_play_again():
        snake.reset()
        food.food_position()
        score.reset()
    else:
        playing = False

screen.exitonclick()
