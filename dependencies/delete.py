from tkinter import messagebox
from display import displayData

def delete(db, cursor, records):
    # get primary key value of selected row
    try:
        data = records.item(records.focus(),"values")[0]
    except: # no selected row
        messagebox.showerror("Error", "There is no selected row")  
        return
    
    # delete row
    cursor.execute(f"DELETE FROM PACKAGE WHERE pckge_no = {data}")
        
    # commit changes
    db.commit() 

    # show data on table
    displayData(cursor, records)
    
    # notify user
    messagebox.showinfo("Form notification", "Record successfully deleted")