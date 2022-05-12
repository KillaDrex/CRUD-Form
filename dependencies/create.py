from tkinter import messagebox
from MySQLdb import DataError
from MySQLdb import IntegrityError
from MySQLdb import OperationalError
from display import displayData

def create(db, cursor, textFields, datePickers, records):
    # get necessary data from form
    branchID = textFields[0].get()
    itemCode = textFields[1].get()
    batchCode = textFields[2].get() if textFields[2].get() != "" else 0
    price = textFields[3].get() if textFields[3].get() != "" else 0.0
    manufacDate = datePickers[0].get_date()
    prepDate = datePickers[1].get_date()
    exprDate = datePickers[2].get_date()
    
    # error message flag - makes sure that an error message only appears once
    errorCount = 0
    
    try:
        # disallow batch codes in decimal values
        if "." in str(batchCode):
            raise OperationalError("batch_code")
            
        cursor.execute("INSERT INTO PACKAGE(brnch_id, item_code, batch_code, pckg_price, manufac_date, prep_date, expr_date) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                            (branchID, itemCode, batchCode, price, manufacDate, prepDate, exprDate))
        
    except OperationalError as e:
        errorMessage = str(e)
        
        # throw error messages
        if errorCount == 0:
            if "brnch_id" in errorMessage: # foreign key is missing/empty value on branch id/wrong data format
                messagebox.showerror("Error", "Incorrect Branch ID")
            elif "batch_code" in errorMessage: # wrong data for batch code
                messagebox.showerror("Error", "Incorrect batch code")           
            errorCount = errorCount + 1
    except IntegrityError as e:
        errorMessage = str(e)
        
        if errorCount == 0:
            if "brnch_id" in errorMessage: # foreign key does not exist, throw error message
                messagebox.showerror("Error", "Incorrect Branch ID")
            elif "item_code" in errorMessage: # unique constraint is violated
                messagebox.showerror("Error", "Incorrect item code")
    except DataError:
        if errorCount == 0: # wrong data for price
            messagebox.showerror("Error", "Incorrect price")  
            errorCount = errorCount + 1
    else:  
        # commit changes
        db.commit()
        
        # show data on table
        displayData(cursor, records)
        
        # notify user
        messagebox.showinfo("Form notification", "Record successfully added")