from tkinter import *
root = Tk()
# MY tittle
root.title("TicketSales")

root.geometry("600x800")

# Giving a background color
root.config(bg="light blue")


# Below is my labels,Entry,btn.

my_lab1 = Label(text="Enter cell number:", bg='white', fg="black")
my_lab1.place(x=50, y=250)
lab1_entry = Entry()
lab1_entry.place(x=300, y=250)
my_lab2 = Label(text="Select TicketCategory:", bg='white', fg="black")
my_lab2.place(y=300, x=50)

# creating a select btn
option = StringVar(root)
option.set("select ticket")

select_btn =OptionMenu(root, option, "Movies", "Soccer", "Theater")
select_btn.place(y=300, x=300)

my_lab3 = Label(text="Number of tickets Bought", bg='white', fg="black")
my_lab3.place(y=350, x=50)

# creating a select btn
options = StringVar(root)
options.set("0")

select_btn =OptionMenu(root, options, "1", "2", "3", "4", "5")
select_btn.place(y=350, x=300)

my_btn1 = Button(text="CalculateTickets", width=20, )
my_btn1.place(y=400, x=50)
my_btn2 = Button(text="Clear entries")
my_btn2.place(y=400, x=300)

class ClsTicketSale(): # Thandokazi Nkohla

    def __init__(self, cell, price, number_tickets):
        self.cell = cell
        self.price = price
        self.number_tickets = number_tickets



root.mainloop()
