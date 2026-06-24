import tkinter as tk
import json
from datetime import datetime

BG = "#313244"
DARK_BG = "#1e1e2e"
NAV_BG = "#181825"
TEXT_BG = "#45475a"
TEXT = "#cdd6f4"
SUBTEXT = "#a6adc8"
RED = "#f38ba8"
GREEN = "#a6e3a1"

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

def current_budget():
    with open("budget.txt", "r") as file:
        budget = file.read()

    if budget != "":
        budget = float(budget)
        return f"${budget:.2f}"
    
    else:
        return
    
#def current_spent():
    

# summary label
summary_label = tk.Label(
    root, text=f"Spent:  |  Budget:  {current_budget()}  |  Remaining: ", font=("Segoe UI", 12), bg=BG, fg=SUBTEXT
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

#--------------------------------------------------------------------- SAVE EXPENSE BUTTON
invalid_expense_entry = tk.Label(log_expense_frame, text=f"Invalid Entry", font=("Segoe UI", 9, "bold"), bg=DARK_BG, fg=RED)
valid_expense_entry = tk.Label(log_expense_frame, text=f"Successful", font=("Segoe UI", 9, "bold"), bg=DARK_BG, fg=GREEN)

# save expense function
def save_expense(amount, category, desc):

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        
    if amount != "" and category != "":
        try:
            amount = float(amount)
        except ValueError:
            if valid_expense_entry.winfo_ismapped() == True:
                valid_expense_entry.pack_forget()

            invalid_expense_entry.pack(pady=(5,0))    # show error msg
            return
        
        data.append(
            {
            "year": year,
            "month": month,
            "amount": amount,
            "category": category,
            "description": desc
            }
            )

        with open("data.json", "w") as file:
            json.dump(data, file)          # the file stores list of dict of expense info
        
        if invalid_expense_entry.winfo_ismapped() == True:
            invalid_expense_entry.pack_forget()
        
        valid_expense_entry.pack(pady=(5,0))  # show success msg
    
    else:
        # show error msg
        if valid_expense_entry.winfo_ismapped() == True:
            valid_expense_entry.pack_forget()

        invalid_expense_entry.pack(pady=(5,0))

# save expense button
SAVE_EXPENSE_BUTTON_BG = "#89b4fa"
SAVE_EXPENSE_BUTTON_TEXT = "#1e1e2e"
save_expense_button = tk.Button(
    log_expense_frame,
    font=("Segoe UI", 10, "bold"),
    text="Save Expense",
    bg=SAVE_EXPENSE_BUTTON_BG,
    fg=SAVE_EXPENSE_BUTTON_TEXT,
    activebackground=SAVE_EXPENSE_BUTTON_BG,
    activeforeground=SAVE_EXPENSE_BUTTON_TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: save_expense(amount_input.get(), category_input.get().title(), desc_input.get())    # use inputted button entries
    )
save_expense_button.pack()

#------------------------------------------------------------------------------------------------------ BREAKDOWN FRAME
# breakdown_frame
breakdown_frame = tk.Frame(root, bg=DARK_BG)

# breakdown phrase
breakdown_phrase = tk.Label(
    breakdown_frame, text=f"{month} {year} Breakdown", font=("Segoe UI", 15, "bold"), bg=DARK_BG, fg=TEXT
    )
breakdown_phrase.pack()

#--------------------------------------------------------------------- SCROLLABLE BREAKDOWN FRAME
# frame --> canvas (picture frame) --> inner frame (picture) --> widgets

# canvas
breakdown_canvas = tk.Canvas(breakdown_frame, bg=DARK_BG, highlightthickness=0)
breakdown_canvas.pack(fill="both", expand=True)

# inner
breakdown_inner_frame = tk.Frame(breakdown_canvas, bg=DARK_BG)
breakdown_inner_frame_id = breakdown_canvas.create_window((0, 0), window=breakdown_inner_frame, anchor="nw")

# make inner frame match canvas width on window open/resize
breakdown_canvas.bind("<Configure>", lambda e: breakdown_canvas.itemconfig(breakdown_inner_frame_id, width=e.width))





# figure out how to make it so that the scrollbar will only show when the height of the inner is greater than the cavnas height



# vertical scrollbar to maneuver canvas to capture/see different areas of inner frame
breakdown_scrollbar = tk.Scrollbar(breakdown_frame, orient="vertical", command=breakdown_canvas.yview)
breakdown_scrollbar.pack(side="right", fill="y")
breakdown_canvas.configure(yscrollcommand=breakdown_scrollbar.set)

# create bar graph
def bar_graph():
    with open("data.json", "r") as file:
        expenses = json.load(file)
    
    category_totals = {}        # stores total amount per category
    for expense in expenses:
        if expense["year"] == year and expense["month"] == month:       # only display current month
            cat = expense["category"]
            category_totals[cat] = category_totals.get(cat, 0) + expense["amount"]

    breakdown_canvas.update_idletasks()                      # force calculation of canvas size (w/o this, size is not yet calculated)
    
    max_amount = max(category_totals.values())
    max_bar_width = breakdown_canvas.winfo_width() * 5 // 8    # determine max bar width proportional to canvas width

    for category, amount in category_totals.items():
        row = tk.Frame(breakdown_inner_frame, bg=DARK_BG)       # create inner frame per each row
        row.pack(fill="x", pady=breakdown_canvas.winfo_width() // 100)

        # category label
        tk.Label(row, text=category, bg=DARK_BG, fg=TEXT, width=breakdown_canvas.winfo_width() // 38, anchor="e").pack(side="left")

        bar_width = int((amount / max_amount) * max_bar_width)      # determine bar widths proportional to their amounts

        # create bar
        bar = tk.Frame(row, bg=GREEN, width=bar_width, height=20)
        bar.pack(side="left")

        # amount label
        tk.Label(row, text=f"${amount:.2f}", bg=DARK_BG, fg=SUBTEXT).pack(side="left", padx=breakdown_canvas.winfo_width() // 160)

# fix scroll bar
# resize everything on resize
# for current_budget function, try and except for filenotfound and make the file
# for log expense, max 14 char long


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
    set_budget_frame, text=f"Current Budget: {current_budget()}", font=("Segoe UI", 12), bg=DARK_BG, fg=TEXT
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

#--------------------------------------------------------------------- SAVE BUDGET BUTTON
invalid_budget_entry = tk.Label(set_budget_frame, text=f"Invalid Entry", font=("Segoe UI", 9, "bold"), bg=DARK_BG, fg=RED)
valid_budget_entry = tk.Label(set_budget_frame, text=f"Successful", font=("Segoe UI", 9, "bold"), bg=DARK_BG, fg=GREEN)

# save budget function
def save_budget(new_budget):
    if new_budget != "":
        try:
            float(new_budget)
        except ValueError:
            if valid_budget_entry.winfo_ismapped():
                valid_budget_entry.pack_forget()

            invalid_budget_entry.pack(pady=(5,0))
            return

        if "." in new_budget and len(new_budget.split(".")[1]) > 2:
            if valid_budget_entry.winfo_ismapped():
                valid_budget_entry.pack_forget()

            invalid_budget_entry.pack(pady=(5,0))
            return
    
        current_budget_phrase.config(text=f"Current Budget: ${float(new_budget):.2f}")  # config to update text, colour, or font only
        summary_label.config(text=f"Spent:  |  Budget:  ${float(new_budget):.2f}  |  Remaining: ")

        if invalid_budget_entry.winfo_ismapped():
            invalid_budget_entry.pack_forget()

        valid_budget_entry.pack(pady=(5,0))

    else:
        current_budget_phrase.config(text=f"Current Budget: None")  # config to update text, colour, or font only
        summary_label.config(text=f"Spent:  |  Budget:  None  |  Remaining: ")

        if invalid_budget_entry.winfo_ismapped():
            invalid_budget_entry.pack_forget()

        valid_budget_entry.pack(pady=(5,0))

    with open("budget.txt", "w") as file:
        file.write(new_budget)

# save budget button
SAVE_BUDGET_BUTTON_BG = "#89b4fa"
SAVE_BUDGET_BUTTON_TEXT = "#1e1e2e"
save_budget_button = tk.Button(
    set_budget_frame,
    font=("Segoe UI", 10, "bold"),
    text="Save Budget",
    bg=SAVE_BUDGET_BUTTON_BG,
    fg=SAVE_BUDGET_BUTTON_TEXT,
    activebackground=SAVE_BUDGET_BUTTON_BG,
    activeforeground=SAVE_BUDGET_BUTTON_TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: save_budget(new_budget_input.get())
    )
save_budget_button.pack()

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


#------------------------------------------------------------------------------------------------------ NAVIGATION BUTTONS
# log expense button
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

# breakdown button
breakdown_button = tk.Button(
    nav_inner,
    text="Breakdown",
    bg=TEXT_BG,
    fg=TEXT,
    activebackground=TEXT_BG,
    activeforeground=TEXT,
    relief=tk.FLAT,
    padx=14, pady=7,
    command=lambda: (show_frame(breakdown_frame), bar_graph())  # show frame and show graph on button event
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
# if padding, must be function-based in order to use the updated height
# only pad always-showing objects, no error msgs here; pack_configure will pack them
object_padding = [
    (title_label, None, lambda height: (height//50, height//125)),
    (summary_label, None, lambda height: (0, height//100)),
    (warning_label, None, lambda height: (0, height//100)),

    (log_expense_phrase, None, lambda height: (height//50, 0)),
    (amount_phrase, lambda height: (int(height//2.5), 0), lambda height: (height//50, 0)),
    (amount_input, lambda height: (0, int(height//2.5)), lambda height: (height//50, 0)),
    (category_phrase, lambda height: (int(height//2.5), 0), lambda height: (height//50, 0)),
    (category_input, lambda height: (0, int(height//2.5)), lambda height: (height//50, 0)),
    (desc_phrase, lambda height: (int(height//2.5), 0), lambda height: (height//50, 0)),
    (desc_input, lambda height: (0, int(height//2.5)), lambda height: (height//50, 0)),
    (save_expense_button, None, lambda height: (height//25, 0)),

    (breakdown_phrase, None, lambda height: (height//50, height//50)),

    (set_budget_phrase, None, lambda height: (height//50, 0)),
    (current_budget_phrase, None, lambda height: (height//50, 0)),
    (new_budget_phrase, lambda height: (height//1.8, 0), lambda height: (height//20, 0)),
    (new_budget_input, lambda height: (0, height//1.8), lambda height: (height//20, 0)),
    (save_budget_button, None, lambda height: (height//25, 0)),

    (history_phrase, None, lambda height: (height//50, height//125)),
    
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


# optimization: loops instead of repetition