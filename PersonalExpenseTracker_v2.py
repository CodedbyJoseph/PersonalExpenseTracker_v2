import tkinter as tk
from datetime import datetime

year = datetime.now().year
month = datetime.now().strftime("%B")

#------------------------------------------------------------------------------------------------------
# window
root = tk.Tk()

# window title
root.title("Personal Expense Tracker")

# window size
root.geometry("800x500")

# window background
root.configure(bg="#313244")

#------------------------------------------------------------------------------------------------------
# title label
title_label = tk.Label(root, text=f"{month} {year}", font=("Segoe UI", 15, "bold"), bg="#313244", fg="#cdd6f4")
title_label.pack()     # pack to place, centres by default

# summary label
summary_label = tk.Label(
    root, text=f"Spent:   |   Budget:   |   Remaining: ", font=("Segoe UI", 12), bg="#313244", fg="#a6adc8"
    )
summary_label.pack()

# warning label
warning_label = tk.Label(root, text="", font=("Segoe UI", 11), bg="#313244", fg="#f38ba8")
warning_label.pack()

#------------------------------------------------------------------------------------------------------
# navigation frame
nav_frame = tk.Frame(root, bg="#181825")
nav_frame.pack(fill="x")

# create nav inner, pack for centering, any object introduced within nav_inner will be centred automatically
nav_inner = tk.Frame(nav_frame, bg="#181825")
nav_inner.pack()

#------------------------------------------------------------------------------------------------------
# log expense frame
log_expense_frame = tk.Frame(root, bg="#1e1e2e")

# log_expense_phrase
log_expense_phrase = tk.Label(
    log_expense_frame, text=f"Log Expense", font=("Segoe UI", 15, "bold"), bg="#1e1e2e", fg="#cdd6f4"
    )
log_expense_phrase.pack()

# amount_phrase
amount_phrase = tk.Label(
    log_expense_frame, text=f"Amount ($)", font=("Segoe UI", 12), bg="#1e1e2e", fg="#cdd6f4"
    )
amount_phrase.pack(anchor="w")

# category_phrase
category_phrase = tk.Label(
    log_expense_frame, text=f"Category", font=("Segoe UI", 12), bg="#1e1e2e", fg="#cdd6f4"
    )
category_phrase.pack(anchor="w")

# desc_phrase
desc_phrase = tk.Label(
    log_expense_frame, text=f"Amount ($)", font=("Segoe UI", 12), bg="#1e1e2e", fg="#cdd6f4"
    )
desc_phrase.pack(anchor="w")

#------------------------------------------------------------------------------------------------------
# log expense button within nav
log_expense_button = tk.Button(
    nav_inner,
    text="Log Expense",
    bg="#45475a",
    fg="#cdd6f4",
    activebackground="#45475a",
    activeforeground="#cdd6f4",
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: log_expense_frame.pack(fill="both", expand=True)        # pack/place the log_expense frame
    )
log_expense_button.pack(side="left")

# breakdown button within nav
breakdown_button = tk.Button(
    nav_inner,
    text="Breakdown",
    bg="#45475a",
    fg="#cdd6f4",
    activebackground="#45475a",
    activeforeground="#cdd6f4",
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: log_expense_frame.pack(fill="both", expand=True)
    )
breakdown_button.pack(side="left")

# set_budget button
set_budget_button = tk.Button(
    nav_inner,
    text="Set Budget",
    bg="#45475a",
    fg="#cdd6f4",
    activebackground="#45475a",
    activeforeground="#cdd6f4",
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: log_expense_frame.pack(fill="both", expand=True)
    )
set_budget_button.pack(side="left")

# history button
history_button = tk.Button(
    nav_inner,
    text="History",
    bg="#45475a",
    fg="#cdd6f4",
    activebackground="#45475a",
    activeforeground="#cdd6f4",
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: log_expense_frame.pack(fill="both", expand=True)
    )
history_button.pack(side="left")

#------------------------------------------------------------------------------------------------------
WIN_H = 500

# tuple for chosen padding of objects: (object, x_padding, y_padding)
# if padding, must be function based in order to use the updated height
object_padding = [
    (title_label, None, lambda height: (height//50, height//125)),
    (summary_label, None, lambda height: (0, height//100)),
    (warning_label, None, lambda height: (0, height//100)),
    (log_expense_phrase, None, lambda height: (height/50, height//125)),
    (amount_phrase, lambda height: (int(height//2.5), 0), lambda height: (0, height//50)),
    (category_phrase, lambda height: (int(height//2.5), 0), lambda height: (0, height//50)),
    (desc_phrase, lambda height: (int(height//2.5), 0), lambda height: (0, height//50)),
    (log_expense_button, lambda height: height//100, lambda height: height//50),
    (breakdown_button, lambda height: height//100, lambda height: height//50),
    (set_budget_button, lambda height: height//100, lambda height: height//50),
    (history_button, lambda height: height//100, lambda height: height//50)
]

# add/update padding
def initiate_padding(event):
    global WIN_H
    if root is event.widget:    # if root is the widget changed
        WIN_H = event.height
        for (widget, x_padding, y_padding) in object_padding:
            widget.pack_configure(padx=x_padding(WIN_H) if x_padding else None, pady=y_padding(WIN_H))   # pack_configure updates/adds to initial pack()

# event listener
# root.bind(event_name, function) --> "for root or object within, when event happens, call function with the event as parameter"
# configure event occurs when on window initializaion/resize
root.bind("<Configure>", initiate_padding)




#------------------------------------------------------------------------------------------------------
# GUI event loop
root.mainloop()

# figure out how to hide frame on event of new button pressed
# pack corresponding frame of new button on event of press