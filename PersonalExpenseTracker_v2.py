import tkinter as tk
from datetime import datetime

year = datetime.now().year
month = datetime.now().strftime("%B")

# window
root = tk.Tk()

# window title
root.title("Personal Expense Tracker")

# window size
root.geometry("800x500")

# window background
root.configure(bg="#313244")

# title label
title = tk.Label(root, text=f"{month} {year}", font=("Segoe UI", 15, "bold"), bg="#313244", fg="#cdd6f4")
title.pack(pady=(10,4))

# summary label
summary = tk.Label(root, text=f"Spent:   |   Budget:   |   Remaining: ", font=("Segoe UI", 12), bg="#313244", fg="#a6adc8")
summary.pack(pady=(0,10))

# warning label
warning = tk.Label(root, text="", font=("Segoe UI", 11), bg="#313244", fg="#f38ba8")
warning.pack(pady=(0,10))

# navigation frame
nav = tk.Frame(root, bg="#181825")
nav.pack(fill="x")

# nav inner sits within nav, only as wide as its contents
nav_inner = tk.Frame(nav, bg="#181825")
nav_inner.pack()  # centre nav inner

# navigation buttons, they are centred as one unit since they live within nav inner (is centred)
log_expense = tk.Button(nav_inner, text="Log Expense", bg="#45475a", fg="#cdd6f4", relief=tk.FLAT, padx=14, pady=7)
log_expense.pack(side="left", padx=5, pady=10)

breakdown = tk.Button(nav_inner, text="Breakdown",   bg="#45475a", fg="#cdd6f4", relief=tk.FLAT, padx=14, pady=7)
breakdown.pack(side="left", padx=5, pady=10)

set_budget = tk.Button(nav_inner, text="Set Budget",   bg="#45475a", fg="#cdd6f4", relief=tk.FLAT, padx=14, pady=7)
set_budget.pack(side="left", padx=5, pady=10)

history = tk.Button(nav_inner, text="History",   bg="#45475a", fg="#cdd6f4", relief=tk.FLAT, padx=14, pady=7)
history.pack(side="left", padx=5, pady=10)

# GUI event loop
root.mainloop()


# notice that the first parameter of a tk method is always the parent