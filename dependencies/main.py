import MySQLdb
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.simpledialog import askstring

from create import create
from read import read
from update import update, on_click
from delete import delete
from display import displayData

# exit function
def on_closing():
    db.close()
    root.destroy()
    
# clear function
def clear():
    for i in range(4):
        textFields[i].delete(0, END)
    
    # deselect any selected rows
    if len(records.selection()) > 0:
        records.selection_remove(records.selection()[0])
    
    # notify user
    messagebox.showinfo("Form notification", "Form Cleared")
        
# create the main window
rootWidth = 1151
rootHeight = 543

root = Tk()
root.title("Inventory Management")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.withdraw()
root.iconbitmap(default="icon.ico")


# create the frames
mainFrame = Frame(root, bd=10, relief=RIDGE, bg="#129793")
mainFrame.pack()

titleFrame = Frame(mainFrame, bd=10, relief=GROOVE, bg="#9BD7D5")
titleFrame.pack(fill=X)

# title label
title = Label(titleFrame, text="Inventory Registration Form", bg="#9BD7D5")
title.config(font=("Times New Roman", 30))
title.pack()

topFrame = Frame(mainFrame, bd=10, relief=GROOVE, bg="#FFF5C3")
topFrame.pack(expand=True, fill="both")

topFrame.columnconfigure(0, weight=1)
topFrame.columnconfigure(1, weight=3)

dataFrame = Frame(topFrame, bd=10, relief=RIDGE, bg="#9BD7D5")
dataFrame.grid(column=0, row=0, sticky=NS)

tableFrame = Frame(topFrame, bd=10, relief=RIDGE, bg="#9BD7D5")
tableFrame.grid(column=1, row=0, sticky=NS)

tableFrame.columnconfigure(0, weight=1)
tableFrame.columnconfigure(1, weight=2)
tableFrame.columnconfigure(2, weight=1)

dataCount = 7 # amount of data fields

# create data frame labels
labels = [Label(dataFrame, text="Branch ID", bg="#9BD7D5"), Label(dataFrame, text="Item Code",  bg="#9BD7D5"), Label(dataFrame, text="Batch Code",  bg="#9BD7D5"), 
            Label(dataFrame, text="Price", bg="#9BD7D5"), Label(dataFrame, text="Manufacture Date", bg="#9BD7D5"),   
            Label(dataFrame, text="Preparation Date", bg="#9BD7D5"), Label(dataFrame, text="Expiration Date", bg="#9BD7D5")]
for i in range(dataCount):
    labels[i].config(font=("Times New Roman", 15))
for i in range(dataCount):
    labels[i].grid(row=i, sticky=W, pady=5)
    
# create data frame textfields
textFields = [Entry(dataFrame, bd=5, relief=SUNKEN, font=("Helvetica", 15)) for i in range(dataCount - 3)]
for i in range(4):
    textFields[i].grid(column=1, row=i, pady=5, padx=5)

# create data frame date pickers
datePickers = [DateEntry(dataFrame, width=30, state="readonly", font=("Helvetica", 10)) for i in range(3)]
for i in range(3):
    datePickers[i].grid(column=1, row=i+4)

# create button frame
buttonFrame = Frame(dataFrame, bd=10,relief=FLAT, bg="#9BD7D5")
buttonFrame.grid(column=0, row=dataCount, columnspan=4, sticky=W)

# create buttons
addButtonImage = PhotoImage(file="add.png")
addButton = Button(buttonFrame, text="Add", bd=4, width=80, height=80, image=addButtonImage, compound=TOP, font=("Garamond", 15), command=lambda: create(db, cursor, textFields, datePickers, records))
addButton.pack(side="left", padx=(0,7), pady=(5,0))

updateButtonImage = PhotoImage(file="update.png")
updateButton = Button(buttonFrame, text="Update", bd=4, width=80, height=80, image=updateButtonImage, compound=TOP, font=("Garamond", 15), command=lambda: update(db, cursor, textFields, datePickers, records))
updateButton.pack(side="left", padx=(0,7), pady=(5,0))

deleteButtonImage = PhotoImage(file="delete.png")
deleteButton = Button(buttonFrame, text="Delete", bd=4, width=80, height=80, image=deleteButtonImage, compound=TOP, font=("Garamond", 15), command=lambda: delete(db, cursor, records))
deleteButton.pack(side="left", padx=(0,7), pady=(5,0))

clearButtonImage = PhotoImage(file="clear.png")
clearButton = Button(buttonFrame, text="Clear", bd=4, width=80, height=80, image=clearButtonImage, compound=TOP, font=("Garamond", 15), command=clear)
clearButton.pack(side="left", pady=(5,0))

# create search bar & filter combo box
search_bar_lbl = Label(tableFrame, text="Search ", font=("Times New Roman", 20), bg="#9BD7D5")
img = PhotoImage(file="search.png")
search_bar_lbl["compound"]= RIGHT
search_bar_lbl["image"] = img
search_bar_lbl.grid(column=0, row=0, pady=5)

search_bar = Entry(tableFrame, bd=5, relief=SUNKEN, width=33, font=("Helvetica", 15))
search_bar.grid(column=1, row=0, pady=5)
search_bar.bind("<KeyRelease>", lambda event: read(cursor, records, filter_cbox, search_bar))

filter_cbox = ttk.Combobox(tableFrame, font=("Helvetica", 11), state="readonly", width=15)
filter_cbox["values"] = ("", "Branch ID", "Item Code", "Batch Code", "Price", "Manufacture Date", "Preparation Date", "Expiration Date")
filter_cbox.current(0)
filter_cbox.grid(column=2, row=0, columnspan=2)
filter_cbox.bind("<<ComboboxSelected>>", lambda event: read(cursor, records, filter_cbox, search_bar))

# create table
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)
records = ttk.Treeview(tableFrame, height=16, columns=("pckge_no", "brnch_id", "item_code", "batch_code", "pckg_price", "manufac_date", "prep_date", "expr_date",),
                        show="headings", yscrollcommand=scroll_y.set)
scroll_y.configure(command=records.yview)
scroll_y.grid(column=4, sticky=NS, padx=(0,5), pady=(5,0))

# stylize the table
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#ffb469", fieldbackground="#fed8b1")
style.configure("Treeview.Heading", background="#26428b", foreground="white")

# create color tags for the table rows
records.tag_configure("odd", background="#ffb469")
records.tag_configure("even", background="#fed8b1")

records.heading("pckge_no", text="Package No")
records.heading("brnch_id", text="Branch ID")
records.heading("item_code", text="Item Code")
records.heading("batch_code", text="Batch Code")
records.heading("pckg_price", text="Package Price")
records.heading("manufac_date", text="Manufacture Date")
records.heading("prep_date", text="Preparation Date")
records.heading("expr_date", text="Expiration Date")

records.column("pckge_no", width=73)
records.column("brnch_id", width=59)
records.column("item_code", width=63)
records.column("batch_code", width=70)
records.column("pckg_price", width=81)
records.column("manufac_date", width=103)
records.column("prep_date", width=96)
records.column("expr_date", width=88)

# table binds
records.bind('<ButtonRelease-1>', lambda event: on_click(event, db, cursor, records=records, textFields=textFields, datePickers=datePickers, dataCount=dataCount))

# add table to frame
records.grid(column=0, row=1, columnspan=4, padx=(5,0), pady=(5,0))

# disable column width resizing
records.bind("<Motion>", "break")

# center root window

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

root.geometry(f"{rootWidth}x{rootHeight}+{int(sw/2-rootWidth/2)}+{int(sh/2-rootHeight/2)}") # this part allows you to only change the location

# show window
root.deiconify()

# ask for user (root) password
password = ""

while password == "":
    password = askstring("Authenticate", "Enter the root password:", parent=root, show="*")
    
    # user pressed the 'cancel' button: exit program
    if password == None:
        root.destroy()
        break
        
    try:
        db = MySQLdb.connect("localhost", "root", password, "inventory_db") # make connection to database
    except MySQLdb.Error as e:  # wrong password
        password = ""
        messagebox.showerror("Error", "Incorrect root password")
else: # connection complete
    cursor = db.cursor()

    # show data on database
    displayData(cursor, records)

    # loop
    root.mainloop()