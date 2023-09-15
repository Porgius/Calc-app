from tkinter import *
from tkinter import ttk

# Variable to keep track of failed login attempts
failed_attempts = 0

# Handle login button click
def login():
    global failed_attempts

    # Get the entered username and password
    entered_username = ent_user.get()
    entered_password = ent_password.get()

    # Check if the username and password are correct
    if entered_username == "4246652" and entered_password == "1Pu21d41e":
        lbl_result.config(text="Login successful!", foreground="green")
    else:
        failed_attempts += 1
        lbl_result.config(text="Login failed. Please try again.", foreground="red")

        # If max failed attempts
        if failed_attempts >= 3:
            window.destroy()  # End Program

# Create the main window
window = Tk()
window.geometry("400x400+200+50")
window.title("Login Window")

# Create and place labels, entry widgets, and login button
lbl_title = ttk.Label(window, text="Login Window")
lbl_title.place(x=150, y=10)

lbl_user = ttk.Label(window, text="Username")
lbl_user.place(x=50, y=50)

ent_user = ttk.Entry(window)
ent_user.place(x=150, y=50)

lbl_password = ttk.Label(window, text="Password")
lbl_password.place(x=50, y=100)

ent_password = ttk.Entry(window, show="*")  # Mask the password with asterisks
ent_password.place(x=150, y=100)

btt_login = ttk.Button(window, text="Login", command=login)
btt_login.place(x=150, y=150)

lbl_result = ttk.Label(window, text="", foreground="red")
lbl_result.place(x=150, y=200)

window.mainloop()
