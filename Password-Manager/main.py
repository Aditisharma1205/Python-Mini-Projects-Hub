from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
def search():
    website=web_block.get()
    try:
        with open("password.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
            messagebox.showerror("Error","No data file found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email} \nPassword:{password}")
        else:
            messagebox.showerror("Error", "site does not exist")
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters=random.randint(0, 10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)
    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_block.delete(0, END)
    pass_block.insert(0,password)
    pyperclip.copy(password)
def save():
    website=web_block.get()
    email=email_block.get()
    password=pass_block.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if website=="" or email=="" or password=="":
        messagebox.showerror("Error","Please fill all fields")
    else:
        is_ok=messagebox.askokcancel(website,f"These are the details Entered: \n Email:{email} \n Password:{password} \n Website:{website}\n Is this correct?")
        if is_ok:
            try:
                with open("password.json","r") as file:
                    #reading old data
                    data =json.load(file)
            except FileNotFoundError:
                with open("password.json","w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                #updateing old data with new data
                data.update(new_data)
                with open("password.json","w") as file:
                    #saving updated data
                    json.dump(data,file,indent=4)
            finally:
                web_block.delete(0, END)
                pass_block.delete(0, END)
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas( width=200, height=200)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
#labels
web=Label(text="Website:")
web.grid(row=1,column=0)
email=Label(text="Email/username:")
email.grid(row=2,column=0)
passwd=Label(text="Password:")
passwd.grid(row=3,column=0)
#entries
web_block=Entry(width=35)
web_block.grid(row=1,column=1,columnspan=2)
web_block.focus()
email_block=Entry(width=35)
email_block.grid(row=2,column=1,columnspan=2)
email_block.insert(0,"abc123@gmail.com")
pass_block=Entry(width=21)
pass_block.grid(row=3,column=1)
#buttons
find=Button(text="Search",command=search)
find.grid(row=1,column=4)
generate=Button(text="Generate Password",command=generate_password)
generate.grid(row=3,column=2)
add=Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()
