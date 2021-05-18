from tkinter import *
from pandas import *
import random
from time import sleep

random_number = 1
BACKGROUND_COLOR = "#B1DDC6"
# --------------------- Reading data ----------------------#


data = pandas.read_csv("data/french_words.csv")
data2 = data.to_dict(orient="records")

# --------------------- reset everything -----------------------#

def reset():
    begin_button["command"] = change_data
    begin_button["text"] = "Begin"
    canvas.itemconfig(language_text, text="Press the begin to start")
    canvas.itemconfig(word_text, text="")

# --------------------- Changing data ------------------------#


def change_data():
    canvas.itemconfig(canvas_image, image=old_image)
    begin_button["text"] = "Reset"
    begin_button["command"] = reset
    global random_number
    random_number = random.randint(1, 100)
    new_data = data2[random_number]
    canvas.itemconfig(word_text, text=new_data["French"])
    canvas.itemconfig(language_text, text="French")
    window.after(3000, change_language)

# --------------------- update image ------------------ #


def change_language():
    global random_number
    canvas.itemconfig(canvas_image, image=new_image)
    new_data = data2[random_number]
    canvas.itemconfig(word_text, text=new_data["English"])
    canvas.itemconfig(language_text, text="English")

# --------------------- UI Design --------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#b1ddc6")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#b1ddc6")
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)
language_text = canvas.create_text(400, 150, text="Press begin to start", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_data)
right_button = Button(image=right_image, highlightthickness=0, command=change_data)
wrong_button.grid(row=2, column=0)
right_button.grid(row=2, column = 1)
canvas.grid(row=1, column=0, columnspan=2)
begin_button = Button(text="Begin", command=change_data)
begin_button.grid(row=2, column=2)

window.mainloop()