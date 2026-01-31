import tkinter as tk
from tkinter import messagebox
import random

# Excuses dictionary
excuses = {
    "school": [
        "My dog ate my homework.",
        "I was absent yesterday.",
        "I forgot my notebook at home.",
        "Coffee spill on my notes.",
        "I had to attend a family event.",  
        "I was sick and couldn't complete the assignment."
    ],
    "work": [
        "I was stuck in traffic.",
        "My computer crashed.",
        "I had a sudden meeting.",
        "WiFi got disconnected.",
        "System update took longer than expected.",
        "I had a power outage at home."
    ],
    "personal": [
        "I had a family emergency.",
        "I was feeling unwell.",
        "I overslept today.",
        "I have fractured my arm.",
        "I had to take care of a personal matter."
    ]
}

# Function to show excuse
def show_excuse():
    category = category_var.get().lower()
    if category in excuses:
        choice = choice_var.get().strip()
        if choice == "":  # Random excuse
            result = random.choice(excuses[category])
        else:
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(excuses[category]):
                    result = excuses[category][index]
                else:
                    result = "❌ Invalid number."
            else:
                result = "❌ Enter a valid number."
        messagebox.showinfo("Your Excuse", result)
    else:
        messagebox.showerror("Error", "❌ Select a valid category")

# Build GUI
root = tk.Tk()
root.title("Random Excuse Generator")
root.geometry("400x250")
root.resizable(False, False)

# Category label and dropdown
tk.Label(root, text="Select Category:", font=("Arial", 12)).pack(pady=5)
category_var = tk.StringVar()
category_var.set("school")  # Default value
category_menu = tk.OptionMenu(root, category_var, *excuses.keys())
category_menu.pack()

# Excuse number label and entry
tk.Label(root, text="Excuse number (leave blank for random):", font=("Arial", 12)).pack(pady=5)
choice_var = tk.StringVar()
tk.Entry(root, textvariable=choice_var).pack()

# Button to get excuse
tk.Button(root, text="Get Excuse", font=("Arial", 12), bg="skyblue", command=show_excuse).pack(pady=20)

root.mainloop()
