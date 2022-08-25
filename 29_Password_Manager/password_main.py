from tkinter import *
from tkinter import messagebox
import random
import pyperclip
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
    proceed = False

    if len(user_web) == 0 or len(user_pswd) == 0:
        messagebox.showerror(title="Incomplete information", message=f"Please don't leave any fields empty!")
    else:
        proceed = messagebox.askokcancel(title=user_web, message=f"These are the details entered:\nEmail: {user_email}"
                                                                 f"\nPassword: "f"{user_pswd}\nWebsite: {user_web}\n(: "
                                                                 f"Proceed :)")
    if proceed:
        with open("Passwords.txt", "a") as passwords:
            passwords.write(f"{user_web} | {user_email} | {user_pswd}\n")
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

website = Label(text="Website: ", font="Arial", bg="white", fg="blue")
website.grid(row=1, column=0)

web = Entry(width=70)
web.focus()
web.grid(row=1, column=1, columnspan=2)

email = Label(text="Email/Username: ", font="Arial", bg="white", fg="blue")
email.grid(row=2, column=0)

em = Entry(width=70)
em.insert(END, "arunsaroha94@gmail.com")
em.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ", font="Arial", bg="white", fg="blue")
password.grid(row=3, column=0)

pswd = Entry(width=45)
pswd.grid(row=3, column=1)

generate = Button(text="Generate Password", font="Arial", bg="orange", command=generate_password)
generate.grid(row=3, column=2, columnspan=1)

addd = Button(text="ADD", font="Arial", bg="orange", width=47, command=save_password)
addd.grid(row=4, column=1, columnspan=2)

window.mainloop()