# This is a python application which used to calculate finance problem
import tkinter as tk
from tkinter import ttk, scrolledtext

win =  tk.Tk()
win.title("ProCal")

total = 0 # present or future sum
pct = 0 # interest rate

def calculateSum():

    global total # present or future sum
    global pct # interest rate
    amout = (amt.get())  # get the amount entered
    prd = (period.get())  # get the period entered
    percentage = per.get()  # get the interest rate per interest period

    # convert interest rate from string to number
    if percentage == "3%":
        pct = 0.03
    elif percentage == "6%":
        pct = 0.06
    elif percentage == "12%":
        pct = 0.12
    else:
        pct = 0.15

    present = chVarName.get() # to find out whether present or future sum is given

    if(present == 1): # if present sum is known then find the future sum of money
        total = round(amout * pow((1 + pct), prd), 2)
    else:
        total = round(amout / pow((1 + pct), prd), 2)

    message = ""
    if (present == 1):
        message += "With " + percentage + " interest rate per interest period " + "you will receive " + "$" + str(
                total) + " at the end of " + str(prd) + " interest period(s)" + " if you invest " + "$" + str(
                amout) + " at this moment!\n"
    else:
        message += "With " + percentage + " interest rate per interest period " + "you will receive " + "$" + str(
                amout) + " at the end of " + str(prd) + " interest period(s)" + " if you invest " + "$" + str(
                total) + " at this moment!\n"

    scroll.insert(tk.END, message)

# create a button
calculate = ttk.Button(win, text="Calculate", command=calculateSum) # calculate button
calculate.grid(column=5, row=1, padx=10)

# label
amount_label = ttk.Label(win, text="Amount")
amount_label.grid(column=0, row=0)
period_label = ttk.Label(win, text="Period")
period_label.grid(column=1, row=0)
percentage_label = ttk.Label(win, text="Percentage")
percentage_label.grid(column=2, row=0)

# create a text box widget for amount and interest period
amt = tk.IntVar() # create the amount string variable object
entry_amt = ttk.Entry(win, width=16, textvariable=amt)
entry_amt.grid(column=0, row=1, padx=3)

period = tk.IntVar() # create the period string variable object
entry_period = ttk.Entry(win, width=16, textvariable=period)
entry_period.grid(column=1, row=1, padx=3)

# combo box
per = tk.StringVar()
percentage = ttk.Combobox(win, width=16, textvariable=per, state='readonly') # readonly will avoid the user from typing value into the combo box
percentage['value'] = ('3%', '6%', '12%', '15%') # compound interest factors
percentage.grid(column=2, row=1)
percentage.current(0)

# create scrolled text widget
scrollWidth = 60
scrollHeight = 10
scroll = scrolledtext.ScrolledText(win, width=scrollWidth, height=scrollHeight, wrap=tk.WORD)
scroll.grid(column=0, row=2, columnspan=6, padx=10, pady=6)

# Create a check button
chVarName = tk.IntVar()
check0 = tk.Checkbutton(win, text="Present Sum", variable=chVarName)
check0.select()
check0.grid(column=3, row=1)

win.mainloop()