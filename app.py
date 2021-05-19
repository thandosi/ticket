# Likho Kapesi

# Importing the tkinter module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox   # importing the messagebox from tkinter


class ClsTicketSales:
    def __init__(self, master):
        self.root = root      # creating a window
        self.root.title("Easy Ticket: Likho Kapesi PTY(LTD)")     # naming the window
        self.root.geometry("900x600")        # setting the window size

        # Cell number widgets
        self.cell_lbl = Label(master, text="Enter Cell Number:")     # creating the cell_lbl Label widget instructing a customer to input his/her cellphone number
        self.cell_lbl.place(x=10, y=30)     # positioning the cell_lbl Label widget utilizing the place() geometry manager
        self.cell_entry = Entry(master)      # creating the cell_entry Entry widget where the customer will input his/her cellphone number
        self.cell_entry.place(x=200, y=30)     # positioning the cell_entry Entry widget using the place() geometry manager

        # Category widgets
        self.category_lbl = Label(master, text="Select Ticket Category:")    # creating
        self.category_lbl.place(x=10, y=80)
        self.var = StringVar()
        self.category_list = ttk.Combobox(master, textvariable=self.var, width=18, value=["Soccer", "Movie", "Theater"])
        self.category_list.place(x=200, y=74)

        # Number of tickets bought
        self.tickets_bought = Label(master, text="Number Of Tickets Bought:")
        self.tickets_bought.place(x=10, y=130)
        self.bought_entry = Spinbox(master, from_=1, to=100, width=17)
        self.bought_entry.place(x=200, y=130)

        # My buttons
        self.calculate_button = Button(master, text="Calculate Ticket", bg="green", fg="white", command=self.calc)   #
        self.calculate_button.place(x=10, y=180)
        self.clear_button = Button(master, text="Clear Entries", bg="blue", fg="white", command=self.clear)
        self.clear_button.place(x=200, y=180)

        # Output section
        self.lb1 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lb1.place(x=10, y=230)

        self.payable = Label(master, text="Amount Payable: ")
        self.payable.place(x=10, y=260)
        self.payable_output = Label(master, text="", fg="green")
        self.payable_output.place(x=180, y=260)

        self.reservation = Label(master, text="Reservation: ")
        self.reservation.place(x=10, y=290)
        self.reservation_output = Label(master, text="", fg="green")
        self.reservation_output.place(x=180, y=290)

        self.num_of_tics = Label(master, text="No of Tickets: ")
        self.num_of_tics.place(x=10, y=320)
        self.num_of_tics_out = Label(master, text="", fg="green")
        self.num_of_tics_out.place(x=180, y=320)

        self.number = Label(master, text="Cell Number: ")
        self.number.place(x=10, y=350)
        self.number_out = Label(master, text="", fg="green")
        self.number_out.place(x=180, y=350)

        self.lb2 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lb2.place(x=10, y=380)

        # Exit Button
        self.exit_btn = Button(master, text="Exit", bg="red", fg="white", width=15, command=self.exit)
        self.exit_btn.place(x=120, y=410)

    # defining a method to validate the inputs from the customer and make calculations
    def calc(self):
        # Check if all the input fiels are filled, if not ==> display error messagebox
        if self.category_list.get() == "" or self.bought_entry.get() == "" or self.cell_entry.get() == "":
            self.message_box = messagebox.showerror('Input Error', 'Please make sure all the input fields are filled')

        # If all inputs are filled run this code
        else:

            # Soccer
            if self.category_list.get() == "Soccer":

                # Calculating the vat and adding it to the total
                vat = (40 * int(self.bought_entry.get())) * 0.14
                total = (40 * int(self.bought_entry.get())) + vat

                # Printing the outputs to the interface
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

             # Movie
            elif self.category_list.get() == "Movie":
                # Calculating the vat and adding it to the total
                vat = (75 * int(self.bought_entry.get())) * 0.14
                total = (75 * int(self.bought_entry.get())) + vat

                # Printing the outputs to the interface
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

             # Theater
            elif self.category_list.get() == "Theater":
                # Calculating the vat and adding it to the total
                vat = (100 * int(self.bought_entry.get())) * 0.14
                total = (100 * int(self.bought_entry.get())) + vat

                # Printing the outputs to the interface
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

    # Method to clear the inputs fields and output labels
    def clear(self):
        self.cell_entry.delete(0, END)
        self.category_list.delete(0, END)
        self.bought_entry.delete(0, END)
        self.payable_output.config(text="")
        self.num_of_tics_out.config(text="")
        self.reservation_output.config(text="")
        self.number_out.config(text="")

    # Method for the exit Button
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.root.destroy()
        else:
            pass


root = Tk()
app = ClsTicketSales(root)
root.mainloop()
