import tkinter as tk
from datetime import datetime

BG = "#313244"
DARK_BG = "#1e1e2e"
NAV_BG = "#181825"
TEXT_BG = "#45475a"
TEXT = "#cdd6f4"
SUBTEXT = "#a6adc8"
RED = "#f38ba8"

year = datetime.now().year
month = datetime.now().strftime("%B")

#------------------------------------------------------------------------------------------------------ WINDOW SET UP
# window
root = tk.Tk()

# window title
root.title("Personal Expense Tracker")

# window size
root.geometry("800x500")

# window background
root.configure(bg=BG)

#------------------------------------------------------------------------------------------------------ DEFAULT UPPER FRAME
# title label
title_label = tk.Label(root, text=f"{month} {year}", font=("Segoe UI", 15, "bold"), bg=BG, fg=TEXT)
title_label.pack()     # pack to place, centres by default

# summary label
summary_label = tk.Label(
    root, text=f"Spent:   |   Budget:   |   Remaining: ", font=("Segoe UI", 12), bg=BG, fg=SUBTEXT
    )
summary_label.pack()

# warning label
warning_label = tk.Label(root, text="", font=("Segoe UI", 11), bg=BG, fg=RED)
warning_label.pack()

#------------------------------------------------------------------------------------------------------ NAVIGATION FRAME
# navigation frame
nav_frame = tk.Frame(root, bg=NAV_BG)
nav_frame.pack(fill="x")

# create nav inner, pack for centering, any object introduced within nav_inner will be centred automatically
nav_inner = tk.Frame(nav_frame, bg=NAV_BG)
nav_inner.pack()

#------------------------------------------------------------------------------------------------------ LOG EXPENSE FRAME
# log expense frame
log_expense_frame = tk.Frame(root, bg=DARK_BG)

# log_expense_phrase
log_expense_phrase = tk.Label(
    log_expense_frame, text=f"Log Expense", font=("Segoe UI", 15, "bold"), bg=DARK_BG, fg=TEXT
    )
log_expense_phrase.pack()

#--------------------------------------------------------------------- AMOUNT INNER FRAME
# amount row
amount_row = tk.Frame(log_expense_frame, bg=DARK_BG)
amount_row.pack(fill="x")

# amount_phrase
amount_phrase = tk.Label(amount_row, text="Amount ($)", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT)
amount_phrase.pack(side="left")

# amount input
amount_input = tk.Entry(
    amount_row, font=("Segoe UI", 12), bg=TEXT_BG, fg=TEXT, insertbackground=TEXT, relief=tk.FLAT
    )
amount_input.pack(side="right")

#--------------------------------------------------------------------- CATEGORY INNER FRAME
# category row
category_row = tk.Frame(log_expense_frame, bg=DARK_BG)
category_row.pack(fill="x")

# category_phrase
category_phrase = tk.Label(category_row, text=f"Category", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT)
category_phrase.pack(side="left")

# category input
category_input = tk.Entry(
    category_row, font=("Segoe UI", 12), bg=TEXT_BG, fg=TEXT, insertbackground=TEXT, relief=tk.FLAT
    )
category_input.pack(side="right")

#--------------------------------------------------------------------- DESC INNER FRAME
# desc row
desc_row = tk.Frame(log_expense_frame, bg=DARK_BG)
desc_row.pack(fill="x")

# desc_phrase
desc_phrase = tk.Label(desc_row, text=f"Desc (Optional)", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT)
desc_phrase.pack(side="left")

# desc input
desc_input = tk.Entry(
    desc_row, font=("Segoe UI", 12), bg=TEXT_BG, fg=TEXT, insertbackground=TEXT, relief=tk.FLAT
    )
desc_input.pack(side="right")

#------------------------------------------------------------------------------------------------------ BREAKDOWN FRAME
# breakdown_frame
breakdown_frame = tk.Frame(root, bg=DARK_BG)

# breakdown phrase
breakdown_phrase = tk.Label(
    breakdown_frame, text=f"{month} {year} Breakdown", font=("Segoe UI", 15, "bold"), bg=DARK_BG, fg=TEXT
    )
breakdown_phrase.pack()

#------------------------------------------------------------------------------------------------------ SET BUDGET FRAME
# set_budget_frame
set_budget_frame = tk.Frame(root, bg=DARK_BG)

# set budget phrase
set_budget_phrase = tk.Label(
    set_budget_frame, text=f"Set Monthly Budget", font=("Segoe UI", 15, "bold"), bg=DARK_BG, fg=TEXT
    )
set_budget_phrase.pack()

# current budget phrase
current_budget_phrase = tk.Label(
    set_budget_frame, text=f"Current Budget: ", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT
    )
current_budget_phrase.pack()

#--------------------------------------------------------------------- NEW BUDGET INNER FRAME
# new budget row
new_budget_row = tk.Frame(set_budget_frame, bg=DARK_BG)
new_budget_row.pack(fill="x")

# new budget phrase
new_budget_phrase = tk.Label(
    new_budget_row, text=f"New Budget ($)", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT
    )
new_budget_phrase.pack(side="left")

# new budget input
new_budget_input = tk.Entry(
    new_budget_row, font=("Segoe UI", 12), bg=TEXT_BG, fg=TEXT, insertbackground=TEXT, relief=tk.FLAT, width = 10
    )
new_budget_input.pack(side="right")

#------------------------------------------------------------------------------------------------------ HISTORY FRAME
# history_frame
history_frame = tk.Frame(root, bg=DARK_BG)

# history phrase
history_phrase = tk.Label(
    history_frame, text=f"Expense History", font=("Segoe UI", 15, "bold"), bg=DARK_BG, fg=TEXT
    )
breakdown_phrase.pack()

#------------------------------------------------------------------------------------------------------ TOGGLE FRAME FUNCTION
# hide and show frame function for on event of button
all_frames = [log_expense_frame, breakdown_frame, set_budget_frame, history_frame]

def show_frame(frame):
    for f in all_frames:
        f.pack_forget()
    frame.pack(fill="both", expand=True)


#------------------------------------------------------------------------------------------------------
# log expense button in navigation frame
log_expense_button = tk.Button(
    nav_inner,
    text="Log Expense",
    bg=TEXT_BG,
    fg=TEXT,
    activebackground=TEXT_BG,
    activeforeground=TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: show_frame(log_expense_frame)        # pack/place the log_expense frame
    )
log_expense_button.pack(side="left")

# breakdown button in navigation frame
breakdown_button = tk.Button(
    nav_inner,
    text="Breakdown",
    bg=TEXT_BG,
    fg=TEXT,
    activebackground=TEXT_BG,
    activeforeground=TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: show_frame(breakdown_frame)
    )
breakdown_button.pack(side="left")

# set_budget button
set_budget_button = tk.Button(
    nav_inner,
    text="Set Budget",
    bg=TEXT_BG,
    fg=TEXT,
    activebackground=TEXT_BG,
    activeforeground=TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: show_frame(set_budget_frame)
    )
set_budget_button.pack(side="left")

# history button
history_button = tk.Button(
    nav_inner,
    text="History",
    bg=TEXT_BG,
    fg=TEXT,
    activebackground=TEXT_BG,
    activeforeground=TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: show_frame(history_frame)
    )
history_button.pack(side="left")

#------------------------------------------------------------------------------------------------------ PADDING
WIN_H = 500

# tuple for chosen padding of objects: (object, x_padding, y_padding)
# if padding, must be function based in order to use the updated height
object_padding = [
    (title_label, None, lambda height: (height//50, height//125)),
    (summary_label, None, lambda height: (0, height//100)),
    (warning_label, None, lambda height: (0, height//100)),

    (log_expense_phrase, None, lambda height: (height/50, 0)),
    (amount_phrase, lambda height: (int(height//2.5), 0), lambda height: (height/50, 0)),
    (amount_input, lambda height: (0, int(height//2.5)), lambda height: (height/50, 0)),
    (category_phrase, lambda height: (int(height//2.5), 0), lambda height: (height/50, 0)),
    (category_input, lambda height: (0, int(height//2.5)), lambda height: (height/50, 0)),
    (desc_phrase, lambda height: (int(height//2.5), 0), lambda height: (height/50, 0)),
    (desc_input, lambda height: (0, int(height//2.5)), lambda height: (height/50, 0)),

    (breakdown_phrase, None, lambda height: (height/50, height//125)),

    (set_budget_phrase, None, lambda height: (height/50, 0)),
    (current_budget_phrase, None, lambda height: (height/50, 0)),
    (new_budget_phrase, lambda height: (int(height//1.8), 0), lambda height: (height/20, 0)),
    (new_budget_input, lambda height: (0, int(height//1.8)), lambda height: (height/20, 0)),

    (history_phrase, None, lambda height: (height/50, height//125)),
    
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
            widget.pack_configure(padx=x_padding(WIN_H) if x_padding else None, pady=y_padding(WIN_H))  # pack_configure updates/adds to initial pack()

# event listener
# root.bind(event_name, function) --> "for root or object within, when event happens, call function with the event as parameter"
# configure event occurs when on window initializaion/resize
root.bind("<Configure>", initiate_padding)




#------------------------------------------------------------------------------------------------------
# GUI event loop
root.mainloop()

# work: log expense button to save entry, save budget button to save budget
# optimization: loops instead of repetition