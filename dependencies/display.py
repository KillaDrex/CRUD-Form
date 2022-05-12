from tkinter import END

def displayData(cursor, table): # function used to show all the records in the database
    cursor.execute("SELECT * FROM PACKAGE")
    
    records = cursor.fetchall()
    
    # delete current data in table
    for item in table.get_children():
        table.delete(item)
    
    # show all data
    counter = 1 # alternate between odd and even for row color
    for row in records:
        table.insert("", END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
        counter = counter + 1

# called when clicking the table column headings
def modifiedDisplayData(cursor, headingID, table):
    # get current table rows
    items = table.get_children()
    itemCount = len(table.get_children())
    
    # get last order by setting
    lastSetting = list(table.item(items[0], "tags")).pop(-1)
    
    # delete current data in table
    for item in items:
        table.delete(item)
    
    # show all data
    counter = 1 # alternate between odd and even for row color
    rows = []
    if lastSetting != "ASC":
        for i in range(itemCount):
            # get rows
            match headingID:
                case "#1": # package no
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY pckge_no ASC")
                    rows = cursor.fetchall()
                case "#2": # branch id
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY brnch_id ASC")
                    rows = cursor.fetchall()
                case "#3": # item code
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY item_code ASC")
                    rows = cursor.fetchall()
                case "#4": # batch code
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY batch_code ASC")
                    rows = cursor.fetchall()
                case "#5": # package price
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY pckg_price ASC")
                    rows = cursor.fetchall()
                case "#6": # manufacture date 
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY manufac_date ASC")
                    rows = cursor.fetchall()
                case "#7": # preparation date
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY prep_date ASC")
                    rows = cursor.fetchall()
                case "#8": # expiration date
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY expr_date ASC")
                    rows = cursor.fetchall()  
                
            # set tags
            tagList = ["odd" if counter % 2 != 0 else "even"]
            tagList.append("ASC")

            # insert row
            table.insert("", END, values=rows[i], tags=tuple(tagList))
           
            # increment
            counter = counter + 1        
    else:
        for i in range(itemCount):
            # get rows
            match headingID:
                case "#1": # package no
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY pckge_no DESC")
                    rows = cursor.fetchall()
                case "#2": # branch id
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY brnch_id DESC")
                    rows = cursor.fetchall()
                case "#3": # item code
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY item_code DESC")
                    rows = cursor.fetchall()
                case "#4": # batch code
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY batch_code DESC")
                    rows = cursor.fetchall()
                case "#5": # package price
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY pckg_price DESC")
                    rows = cursor.fetchall()
                case "#6": # manufacture date 
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY manufac_date DESC")
                    rows = cursor.fetchall()
                case "#7": # preparation date
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY prep_date DESC")
                    rows = cursor.fetchall()
                case "#8": # expiration date
                    cursor.execute("SELECT * FROM PACKAGE ORDER BY expr_date DESC")
                    rows = cursor.fetchall() 
                    
            # set tags
            tagList = ["odd" if counter % 2 != 0 else "even"]
            
            # insert row
            table.insert("", END, values=rows[i], tags=tuple(tagList))
           
            # increment
            counter = counter + 1   