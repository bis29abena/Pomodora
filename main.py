from tkinter import *
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
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global rep

    # Resetting the timer in the canvas
    # Stopping the timer using the after_cancel method
    # Changing the label timer to its original text
    # Resetting the rep range
    # Resetting the check_mark labels
    canvas.after_cancel(timer)
    canvas.itemconfig(text_timer_, text="00:00")
    text_timer.config(text="Timer")
    rep = 0
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Setting the Lomg Break
    if rep % 8 == 0:
        text_timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    # Setting the short breaks
    elif rep % 2 == 0:
        text_timer.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    # Setting the work timer
    else:
        text_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Getting the mins and secs of the timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Getting a nice and clean format of the seconds timer
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Getting the text Canvas to count down after every one second
    canvas.itemconfig(text_timer_, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # The timer loops on its own after every session
        # And prints outs a check mark after every 2 sessions
        start_timer()
        if rep == 2 or rep == 4 or rep == 6:
            check_mark_label.config(text="✓")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# setting up the bg color
window.config(padx=100, pady=50, bg=YELLOW)

# Displaying the tomato image on the screen and the text timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer_ = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

# Creating the timer label
text_timer = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN)
text_timer.config(bg=YELLOW)
text_timer.grid(column=1, row=0)

# Creating the start  button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.config(bg="white", fg="black")
start_button.grid(column=0, row=3)

# Creating the reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.config(bg="white", fg="black")
reset_button.grid(column=2, row=3)

# Creating the check mark label
check_mark_label = Label(bg=YELLOW, fg=GREEN, font=("normal", 20, "bold"))
check_mark_label.grid(column=1, row=4)

window.mainloop()
