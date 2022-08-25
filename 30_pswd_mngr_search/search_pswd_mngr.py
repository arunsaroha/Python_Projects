from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    genrated_password = "".join(password_list)
    if pswd.get() != 0:
        pswd.delete(0, END)
    pswd.insert(0, genrated_password)
    pyperclip.copy(genrated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user_web = web.get()
    user_email = em.get()
    user_pswd = pswd.get()
    new_data = {
        user_web: {
            "email": user_email,
            "password": user_pswd,
        }
    }

    if len(user_web) == 0 or len(user_pswd) == 0:
        messagebox.showerror(title="Incomplete information", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web.delete(0, END)
            pswd.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------ #

def find_password():
    search_website = web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Invalid Search", message="Sorry, the data file does not exist")
    else:
        if search_website in data:
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            messagebox.showinfo(title="Found data", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=":)", message="No data found")
    finally:
        web.delete(0, END)
        pswd.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

picture = Canvas(width=200,height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
picture.create_image(100, 100, image=img)
picture.grid(row=0, column=1)

# LABELS
website_label = Label(text="Website: ", font="Arial", bg="white", fg="blue")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ", font="Arial", bg="white", fg="blue")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ", font="Arial", bg="white", fg="blue")
password_label.grid(row=3, column=0)

# ENTRIES
web = Entry(width=50)
web.grid(row=1, column=1, columnspan=1)
web.focus()
em = Entry(width=50)
em.grid(row=2, column=1, columnspan=1)
em.insert(0, "arunsaroha94@gmail.com")
pswd = Entry(width=50)
pswd.grid(row=3, column=1)

# BUTTONS
generate = Button(text="Generate Password", font="Arial", bg="orange", command=generate_password)
generate.grid(row=3, column=2, columnspan=1)
addd = Button(text="ADD", font="Arial", bg="orange", width=47, command=save_password)
addd.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", font="Arial", bg="orange", command=find_password, width=17)
search.grid(row=1, column=2, columnspan=1)

window.mainloop()