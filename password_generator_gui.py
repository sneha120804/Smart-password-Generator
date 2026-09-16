import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a number."
        )
        return

    if length < 8:
        messagebox.showerror(
            "Invalid Length",
            "Minimum password length is 8."
        )
        return

    elif length > 16:
        messagebox.showerror(
            "Invalid Length",
            "Maximum password length is 16."
        )
        return


    special = random.choice(string.punctuation)


    numbers = ''.join(random.choices(string.digits, k=3))

    
    remaining_length = length - 4
    letters = ''.join(
        random.choices(string.ascii_letters, k=remaining_length)
    )

    
    password_list = list(special + numbers + letters)

    
    random.shuffle(password_list)

    password = ''.join(password_list)


    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    status_label.config(
        text="✓ Password Generated Successfully!",
        fg="#22C55E"
    )

def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Please generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    status_label.config(
        text="✓ Password copied successfully!",
        fg="#38BDF8"
    )


def clear_password():

    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    status_label.config(
        text=""
    )

root = tk.Tk()

root.title("Smart Password Generator")
root.geometry("620x650")
root.resizable(False, False)
root.configure(bg="#1E293B")

title_label = tk.Label(
    root,
    text="Smart Password Generator",
    font=("Arial", 25, "bold"),
    bg="#1E293B",
    fg="#FACC15"
)

title_label.pack(pady=(35, 5))

description_label = tk.Label(
    root,
    text="Create a strong and secure password in seconds",
    font=("Arial", 12),
    bg="#1E293B",
    fg="#CBD5E1"
)

description_label.pack(pady=(0, 25))

main_frame = tk.Frame(
    root,
    bg="#334155",
    width=500,
    height=380
)

main_frame.pack()

main_frame.pack_propagate(False)

length_label = tk.Label(
    main_frame,
    text="Enter Password Length",
    font=("Arial", 13, "bold"),
    bg="#334155",
    fg="white"
)

length_label.pack(pady=(30, 8))

length_entry = tk.Entry(
    main_frame,
    font=("Arial", 13),
    width=25,
    justify="center",
    bg="#F8FAFC",
    fg="#1E293B",
    relief="flat"
)

length_entry.pack()

info_label = tk.Label(
    main_frame,
    text="Minimum: 8    |    Maximum: 16",
    font=("Arial", 9),
    bg="#334155",
    fg="#94A3B8"
)

info_label.pack(pady=5)

generate_button = tk.Button(
    main_frame,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password,
    bg="#FACC15",
    fg="#1E293B",
    activebackground="#FDE047",
    activeforeground="#1E293B",
    relief="flat",
    padx=25,
    pady=10,
    cursor="hand2"
)

generate_button.pack(pady=15)

password_label = tk.Label(
    main_frame,
    text="Your Generated Password",
    font=("Arial", 12, "bold"),
    bg="#334155",
    fg="white"
)

password_label.pack(pady=(5, 8))

password_entry = tk.Entry(
    main_frame,
    font=("Consolas", 15, "bold"),
    width=32,
    justify="center",
    bg="#F8FAFC",
    fg="#1E293B",
    relief="flat"
)

password_entry.pack()

button_frame = tk.Frame(
    main_frame,
    bg="#334155"
)

button_frame.pack(pady=15)

copy_button = tk.Button(
    button_frame,
    text="Copy Password",
    font=("Arial", 10, "bold"),
    command=copy_password,
    bg="#38BDF8",
    fg="#0F172A",
    activebackground="#7DD3FC",
    relief="flat",
    padx=18,
    pady=7,
    cursor="hand2"
)

copy_button.pack(side="left", padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    command=clear_password,
    bg="#64748B",
    fg="white",
    activebackground="#94A3B8",
    relief="flat",
    padx=18,
    pady=7,
    cursor="hand2"
)

clear_button.pack(side="left", padx=5)

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "bold"),
    bg="#1E293B"
)

status_label.pack(pady=15)

root.mainloop()