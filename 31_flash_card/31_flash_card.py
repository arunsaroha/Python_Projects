from tkinter import *
import pandas
import random
# ---------------------------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
current_card = {}
to_learn = {}

# -----READING THE WORDS FORM FILE-----
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(image_of_card, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = current_card["English"]
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(image_of_card, image=card_back)
    flip_timer = window.after(3000, func=next_card)

def learn_card():
    to_learn.remove(current_card)
    known = pandas.DataFrame(to_learn)
    known.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# -----WINDOW-----
window = Tk()
window.title("FLASH CARD GAME")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

# -----CARD-----
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image_of_card = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/4, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, text="", font=("Arial", 60, "bold"))

# -----TICK / CROSS-----
right_img = PhotoImage(file="images/right.png")
tick = Button(image=right_img, highlightthickness=0, command=learn_card)
tick.grid(row=1, column=1)
# ---------------------- #
cross_img = PhotoImage(file="images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, command=next_card)
cross.grid(row=1, column=0)

next_card()

window.mainloop()