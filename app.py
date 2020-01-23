# Import modules
from tkinter import *


# create initial class

class CurrencyConveret:
    def __init__(self):
      # create the application window using Tk()
        window = Tk()
        window.title("Currency Converter")
        # style the app
        window.configure(bg="#333")

  # Add a widget label to the app window
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Amount to Convert").grid(row=1, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="#333",
              text="Conversion Amount").grid(row=3, column=1, sticky=W)

   # create an object and use Entry() to take user input

        self.amounttoConvert = StringVar()  # moitors changes
        Entry(window, textvariable=self.amounttoConvert, justify=RIGHT).grid(
            row=1, column=2)  # will take user input

        self.conversionRateVar = StringVar()
        Entry(window, textvariable=self.conversionRateVar, justify=RIGHT).grid(
            row=2, column=2)  # will take user input

        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font="Helvetica 12 bold", bg="#333",
                                   textvariable=self.convertedAmountVar).grid(row=3, column=2, sticky=E)

    # Create the conver and clear button
        btnConvertedAmount = Button(window, text="Convert", font="Helvetica 12 bold", bg="ivory",
                                    fg="black", command=self.convertedAmount).grid(row=4, column=2, sticky=E)

        btndelete_all = Button(window, text="Delete", font="Helvetica 12 bold", bg="ivory",
                               fg="black", command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)

        window.mainloop()

    # Create a function to convert the values
    # This will convert the amount
    def convertedAmount(self):
        amt = float(self.conversionRateVar.get())
        conversionRateVar = float(self.amounttoConvert.get()) * amt
        self.convertedAmountVar.set(format(conversionRateVar, '10.2f'))
    # This will reset all the values to blank

    def delete_all(self):
        self.amounttoConvert.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")


CurrencyConveret()
