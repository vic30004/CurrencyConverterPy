# Import modules
from tkinter import *


# create initial class

class CurrencyConveret:
    def __init__(self):
      # create the application window using Tk()
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="#333")

  # Add a widget label to the app window
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Amount to Convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Conversion Amount").grid(row=3, column=1, sticky=W)

# style the app
