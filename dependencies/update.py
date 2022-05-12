from lib2to3.pytree import convert
from time import strptime
from tkinter import messagebox, END
from MySQLdb import DataError
from MySQLdb import IntegrityError
from MySQLdb import OperationalError
from display import displayData, modifiedDisplayData

from datetime import datetime
from time import mktime

data = []

def on_click(event, db, cursor, records, textFields, datePickers, dataCount):
    if records.identify("region", event.x, event.y) == "heading": # a heading was clicked
        headingID = records.identify_column(event.x)
        modifiedDisplayData(cursor, headingID, records)
        
    else: # a row was clicked
        record = records.focus()

        global data
        data = records.item(record, 'values')
        
        try:    
            for i in range(4):
                textFields[i].delete(0, END)
                textFields[i].insert(0, data[i+1])
            
            for i in range(3):
                convertedDate = datetime.fromtimestamp(mktime(strptime(data[i+5], '%Y-%m-%d')))
                datePickers[i].set_date(convertedDate)

        except:
            pass
    
def update(db, cursor, textFields, datePickers, records):
    # no selected record, return with error message
    try:
        records.item(records.focus(),"values")[0]
    except:
        messagebox.showerror("Error", "There is no selected row")  
        return
        
    branchID = textFields[0].get()
    itemCode = textFields[1].get()
    batchCode = textFields[2].get() if textFields[2].get() != "" else 0
    price = textFields[3].get() if textFields[3].get() != "" else 0.0
    manufacDate = datePickers[0].get_date()
    prepDate = datePickers[1].get_date()
    exprDate = datePickers[2].get_date()
    pkgNum = data[0]

    # no data was modified, return
    rowValues = records.item(records.focus(),"values")
    if branchID == rowValues[1] and itemCode == rowValues[2] and batchCode == rowValues[3] and price == rowValues[4] and str(manufacDate) == rowValues[5] and str(prepDate) == rowValues[6] and str(exprDate) == rowValues[7]:
        return
        
    errorCount = 0

    try:
        cursor.execute(
        """
        UPDATE PACKAGE
            SET 
                brnch_id = %s, 
                item_code = %s, 
                batch_code = %s, 
                pckg_price = %s, 
                manufac_date = %s, 
                prep_date = %s, 
                expr_date = %s 
            WHERE 
                pckge_no = %s;
        """, 
        (branchID, itemCode, batchCode, price, manufacDate, prepDate, exprDate, pkgNum))
            
    # stolen from create.py
    
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

    else:  # try clause did not raise an exception
        # commit changes
        db.commit()
        
        # show data on table
        displayData(cursor, records)

        # notify user
        messagebox.showinfo("Form notification", "Record successfully updated")