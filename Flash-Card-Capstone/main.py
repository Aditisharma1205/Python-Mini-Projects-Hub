import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
to_learn=[]
current_card={}

try:
    data=pd.read_csv("./data/words_to_learn.csv")
    
except FileNotFoundError:
    original_data=pd.read_csv("./data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
    
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")
    flip_timer=window.after(3000,func=card_flip)

def card_flip():
    global current_card
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white" )
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flash Capstone Project")
flip_timer=window.after(3000,func=card_flip)

canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Arial",60,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

right=PhotoImage(file="./images/right.png")
r_button=Button(image=right,highlightbackground=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
r_button.grid(row=1,column=1)
wrong=PhotoImage(file="./images/wrong.png")
w_button=Button(image=wrong,highlightbackground=BACKGROUND_COLOR,highlightthickness=0,command=next_card)
w_button.grid(row=1,column=0)
next_card()
window.mainloop()
