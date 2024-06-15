import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import _json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for cha in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for ch in range(nr_numbers)]
    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json","r") as file:
            data = json.load(file)
            if input_website.get() in data:
                messagebox.showinfo(title="Info",message=f"{input_website.get()}\n{data[input_website.get()]['password']}")
            else:
                messagebox.showinfo(title="Info",message="No found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Info", message="No entries to search ")
def add():
    new_data = {
        input_website.get():{
        "email":input_username.get(),
        "password":password_entry.get()
        }
    }
    if len(input_website.get())==0 or len(password_entry.get())==0:
        messagebox.showinfo(title="password",message="Please enter the fields properly")
    else:
        try:
             with open("data.json", mode="r") as file:
                 data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data,file,indent=4)
        finally:
            input_website.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)
website = Label(text="Website:")
website.grid(column=0,row=1)
input_website = Entry()
input_website.grid(column=1,row=1,columnspan=2,sticky=EW)
input_website.focus()
search = Button(text="Search",command=search)
search.grid(column=2,row=1,sticky=EW)
user_name = Label(text="Email/Username: ")
user_name.grid(column=0,row=2)
input_username = Entry()
input_username.insert(0,"veereshhubballi496@.gmail.com")
input_username.grid(column=1,row=2,columnspan=2,sticky=EW)
password = Label(text="Password:")
password.grid(column=0,row=3)
password_entry = Entry()
password_entry.grid(column=1,row=3,sticky=EW)
generate = Button(text="Generate Password",command=generate_password)
generate.grid(column=2,row=3)
add = Button(text="Add",command=add)
add.grid(column=1,row=4,columnspan=2,sticky=EW)
window.mainloop()