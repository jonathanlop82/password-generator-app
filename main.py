from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0,END)
    password_input.insert(0,password)

    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if website == '' or email == '' or password == '':
        messagebox.showinfo(title="Oops", message="Please dont't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIt is ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    dict_data = json.load(data)
                    dict_data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", "w") as data:
                    #data.write(f"{website} | {email} | {password}\n")
                    json.dump(dict_data, data, indent=4)

            website_input.delete(0,'end')
            password_input.delete(0,'end')
            website_input.focus()


# ----------------------------- GET DATA ------------------------------#

def get_password():
    try:
        with open("data.json", "r") as data:
            dict_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(message="File not found")

    website_search = website_input.get()
    print(website_search)
    try:
        messagebox.showinfo(title=website_search,message=f"Email: {dict_data[website_search]['email']}\nPassword: {dict_data[website_search]['password']}")
    except KeyError:
        messagebox.showinfo(message="Website not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#put image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"jonathanlop82@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generator_pass_button = Button(text="Generate Password", command=generate_password)
generator_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search",  width=13, command=get_password)
search_button.grid(column=2, row=1)





window.mainloop()