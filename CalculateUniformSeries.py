import tkinter as tk

class CalculateUniformSeries:

    def _init_(self):
        self.total = 0
        self.message = 'u'

    def calculate(self, amount, period, percentage, message, scroll, pct):

        self.total = round(amount * (((pow((1 + percentage), period) - 1))/percentage), 2)

        message += "With " + pct + " interest rate per interest period " + "you will receive " + "$" + str(
            self.total) + " at the end of " + str(period) + " interest period(s)" + " if you invest uniformly at " + "$" + str(
            amount) + "!\n"

        scroll.insert(tk.END, message) # displayed message
