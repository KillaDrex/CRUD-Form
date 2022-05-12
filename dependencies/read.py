from display import displayData
import tkinter

def read(cursor, records, filter_cbox, search_bar):
    try:
        match filter_cbox.get():
            case "":
                displayData(cursor, records)
            case "Branch ID":
                cursor.execute(f"select * from Package where brnch_id = {search_bar.get()}")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
                    
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1                      
            case "Item Code":
                cursor.execute(f"select * from Package where item_code = {search_bar.get()}")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
            case "Batch Code":
                cursor.execute(f"select * from Package where batch_code = {search_bar.get()}")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
            case "Price":
                cursor.execute(f"select * from Package where pckg_price LIKE {search_bar.get()}")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
            case "Manufacture Date":
                cursor.execute(f"select * from Package where manufac_date = '{search_bar.get()}'")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
            case "Preparation Date":
                cursor.execute(f"select * from Package where prep_date = '{search_bar.get()}''")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
            case "Expiration Date":
                cursor.execute(f"select * from Package where expr_date = '{search_bar.get()}'")
                rows = cursor.fetchall()
                # delete current data in table
                for item in records.get_children():
                    records.delete(item)
        
                # show all data
                counter = 1 # alternate between odd and even for row color
                for row in rows:
                    records.insert("", tkinter.END, values=row, tags=("odd" if counter % 2 != 0 else "even"))
                    counter = counter + 1    
    except: # catch exception
        pass
