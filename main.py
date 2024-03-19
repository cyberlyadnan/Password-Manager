from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


YELLOW = "#55C8FD"
FONT = ("arial",12, "bold")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers =['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','!','@','#','$','%','^','&','*','(',')']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '#', '$', '%', '&', '(', ')', '*', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = []

window = Tk()
window.minsize(width=600, height=600)
window.resizable(False, False)
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)
# _____________________________________________________________________________________
# search button functioning

# _____________________________________________________________________________________
# password encryption
def encode_decode(text, direction):
    shift = 7
    shift_ = 0
    end_code = ""
    if shift > 26:
        shiftt = shift % 26
        shift = shiftt

    if direction == "+":
        shift_ = (+shift)

    elif direction == "-":
        shift_ = (-shift)

    for character in text:
        if character in alphabet:
            check = alphabet.index(character)
            end_code += alphabet[check + shift_]

        if character in numbers:
            check = numbers.index(character)
            end_code += numbers[check + shift_]

        if character in symbols:
            check = symbols.index(character)
            end_code += symbols[check + shift_]

        if character in capital_letters:
            check = capital_letters.index(character)
            end_code += capital_letters[check + shift_]

        if character == ".":
            end_code += "-"

        if character == "-":
            end_code += "."
    return end_code



# _____________________________________________________________________________________
# password generator
def password_generator():
    for letter in range(15):
        letter = random.choice(all_characters)
        password.append(letter)
    password_entry.insert(END, string="".join(password))
    pyperclip.copy("".join(password))
    password.clear()

# _____________________________________________________________________________________
# add button functioning
def add():
    email_text = email_entry.get()
    password_text = password_entry.get()
    website_text = website_entry.get().lower()
    new_data = {
        encode_decode(website_text, "+"): {
            encode_decode("email", "+"): encode_decode(email_text, "+"),
            encode_decode("password", "+"): encode_decode(password_text, "+"),
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except :
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        if encode_decode(website_text, "+") in data:
            if len(website_text) == 0 or len(password_text) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            else:
                is_ok = messagebox.askokcancel(title=website_text, message=f"You Are Updating The Details! : \nEmail: {email_text} "
                                                                      f"\nPassword: {password_text} \nIs it ok to save?")
                if is_ok:

                    data[encode_decode(website_entry.get(), "+")]["lthps"] = encode_decode(email_entry.get(), "+")

                    data[encode_decode(website_entry.get(), "+")]["whzzdvyk"] = encode_decode(password_entry.get(), "+")
                    with open("data.json", "w") as datafile:
                        json.dump(data, datafile, indent=4)
                    email_entry.delete(0, END)
                    email_entry.insert(END, string="abc@gmail.com")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


        else:
            if len(website_text) == 0 or len(password_text) == 0:
                messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            else:
                is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {email_text} "
                                                                      f"\nPassword: {password_text} \nIs it ok to save?")
                if is_ok:
                    try:
                        with open("data.json", "r") as data_file:
                            # Reading old data
                            data = json.load(data_file)
                    except FileNotFoundError:
                        with open("data.json", "w") as data_file:
                            json.dump(new_data, data_file, indent=4)
                    else:
                        # Updating old data with new data
                        data.update(new_data)
                        with open("data.json", "w") as data_file:
                            # Saving updated data
                            json.dump(data, data_file, indent=4)
                    finally:
                        email_entry.delete(0, END)
                        email_entry.insert(END, string="abc@gmail.com")
                        website_entry.delete(0, END)
                        password_entry.delete(0, END)


# _____________________________________________________________________________________
# Search function
def search():
    website = website_entry.get().lower()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        for website_ in data:
            if encode_decode(website_, "-") == website:
                email_entry.delete(0, END)
                email_entry.insert(END, string=encode_decode(data[website_]["lthps"], "-"))
                password_entry.delete(0, END)
                password_entry.insert(END, string=encode_decode(data[website_]["whzzdvyk"], "-"))


# _____________________________________________________________________________________
# Creating GUI
canvas = Canvas(width=360, height=360, highlightthickness=0, bg=YELLOW)
photo = PhotoImage(file="lock.png")
canvas.create_image(180, 180, image=photo)
canvas.grid(column=0, row=0, columnspan=3, sticky="e")
# canvas.place(x=20, y=20)



# label
website = Label(text="Website: ", bg=YELLOW, font=FONT)
website.grid(column=0, row=1, sticky="E")
# website.place(x=180, y=180)

email = Label(text="Email/Username: ", bg=YELLOW, font=FONT)
email.grid(column=0, row=2, sticky="E")

email = Label(text="Password: ", bg=YELLOW, font=FONT)
email.grid(column=0, row=3, sticky="E")

# entry
website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="W")

email_entry = Entry(width=50)
email_entry.insert(END, string="abc@gmail.com")
email_entry.grid(row=2, column=1, sticky="W")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky="W")


# button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=1, columnspan=2, sticky="E")

generate_password = Button(text="Generate", width=15, command=password_generator)
generate_password.grid(row=3, column=1, sticky="E", columnspan=2)

add_button = Button(text="Add", width=40, command=add)
add_button.grid(row=5, column=1, columnspan=2)





window.mainloop()