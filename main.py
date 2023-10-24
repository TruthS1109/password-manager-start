from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import *
def generate_password():
    passwd_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    password = "".join(password_list)

    passwd_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = wb_entry.get()
    email = username_entry.get()
    password = passwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please make sure you haven't left any fields empty.")
    elif "@" not in email:
        messagebox.showinfo("Error", "Please input valid email address.")
    else:
        try:
            with open("data.json", "r") as pwd_file:
                #Reading old data
                data = json.load(pwd_file)
        except FileNotFoundError:
            with open("data.json", "w") as pwd_file:
                json.dump(new_data, pwd_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as pwd_file:
                # saving updated data
                json.dump(data, pwd_file, indent=4)
        finally:
            wb_entry.delete(0, "end")
            passwd_entry.delete(0, "end")
        #messagebox.showinfo("OK", "The record has been saved.")
# ---------------------------- Find Password ------------------------------- #
def find_password():
    web_input = wb_entry.get()

    #Get the json record
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if web_input in data:
            user_name = data[web_input]["email"]
            password = data[web_input]["password"]
            show_msg = f"Email: {user_name}\n Password:{password}"
            messagebox.showinfo(title=web_input, message=show_msg)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web_input} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg='white')

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
#canvas.pack()
canvas.grid(column=1, row=0)

#Website info
wb_label = Label(text="Website: ", bg='white')
wb_label.grid(column=0, row=1)
wb_entry = Entry(width=21, bg='white')
wb_entry.focus()
wb_entry.grid(column=1, row=1)
#User name info
username_label = Label(text="Email/Username: ", bg='white')
username_label.grid(column=0, row=2)
username_entry = Entry(width=35, bg='white')
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "username@gmail.com")
#Password info
passwd_label = Label(text="Password: ", bg='white')
passwd_label.grid(column=0, row=3)
passwd_entry = Entry( width=21, bg='white')
passwd_entry.grid(column=1, row=3)

#Search button
generate_button = Button(text="Search", width=12, fg='blue',command=find_password)
generate_button.grid(column=2, row=1)

#Generate button
generate_button = Button(text="Generate Password", bg='white', command=generate_password)
generate_button.grid(column=2, row=3)

#Add button
add_button = Button(text="Add", width=36, bg='white', command=add_password)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()