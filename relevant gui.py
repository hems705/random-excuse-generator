import tkinter as tk
from tkinter import messagebox
import random

# Replies with excuses
excuses = {
    "school": [
        "I couldn't submit it because my dog ate my homework.",
        "I missed it as I was absent yesterday.",
        "I forgot my notebook at home.",
        "Coffee spilled on my notes.",
        "I had to attend a family event.",
        "I was sick and couldn't complete the assignment."
    ],
    "work": [
        "I was late because I was stuck in traffic.",
        "The task got delayed because my computer crashed.",
        "I had to attend a sudden meeting.",
        "My WiFi got disconnected.",
        "A system update took longer than expected.",
        "There was a power outage at my home."
    ],
    "personal": [
        "I couldn't manage it due to a family emergency.",
        "I was feeling unwell.",
        "I overslept today.",
        "I have fractured my arm.",
        "I had to take care of a personal matter."
    ]
}

def generate_reply():
    question = question_var.get().strip()
    category = category_var.get().lower()

    if question == "":
        messagebox.showerror("Error", "Please enter the problem/question.")
        return

    excuse = random.choice(excuses[category])

    reply = f"Regarding your question:\n\"{question}\"\n\nMy response:\n{excuse}"

    messagebox.showinfo("Generated Reply", reply)

# GUI setup
root = tk.Tk()
root.title("Excuse Assistant")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(root, text="Enter the problem/question:", font=("Arial", 12)).pack(pady=5)
question_var = tk.StringVar()
tk.Entry(root, textvariable=question_var, width=60).pack()

tk.Label(root, text="Select category:", font=("Arial", 12)).pack(pady=5)
category_var = tk.StringVar(value="school")
tk.OptionMenu(root, category_var, *excuses.keys()).pack()

tk.Button(root, text="Generate Reply", font=("Arial", 12),
          bg="lightgreen", command=generate_reply).pack(pady=20)

root.mainloop()
