import tkinter as tk

class CalculatePresentFuture:

    def __init__(self):
        pass

    def calculate(self, amount, prd, percentage, message, scroll, pct, present):

        if (present == 1):  # if present sum is known then find the future sum of money
            total = round(amount * pow((1 + pct), prd), 2)
        else:
            total = round(amount / pow((1 + pct), prd), 2)

        if (present == 1):
            message += "With " + percentage + " interest rate per interest period " + "you will receive " + "$" + str(
                total) + " at the end of " + str(prd) + " interest period(s)" + " if you invest " + "$" + str(
                amount) + " at this moment!\n"
        else:
            message += "With " + percentage + " interest rate per interest period " + "you will receive " + "$" + str(
                amount) + " at the end of " + str(prd) + " interest period(s)" + " if you invest " + "$" + str(
                total) + " at this moment!\n"

        scroll.insert(tk.END, message) # show message