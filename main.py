import tkinter as t
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer_clock = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repetitions
    repetitions = 0
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    check_label.config(text=" ")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1
    if repetitions % 8 == 0:
        # Long Break
        count_down(count=(LONG_BREAK_MIN*60))
        timer_label.config(text="BREAK", fg=RED)
        repetitions = 0
    elif repetitions % 2 == 0:
        # Short Break
        count_down(count=(SHORT_BREAK_MIN*60))
        timer_label.config(text="BREAK", fg=PINK)
    else:
        # Work
        count_down(count=(WORK_MIN*60))
        timer_label.config(text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global repetitions
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_clock
        timer_clock = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = " "
        for sessions in range(math.floor(repetitions/2)):
            marks += "✔"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Canvas
tomato_img = t.PhotoImage(file="tomato.png")

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 135, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Labels
timer_label = t.Label()
timer_label.config(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = t.Label()
check_label.config(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
# Buttons
start_button = t.Button()
start_button.config(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = t.Button()
reset_button.config(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()