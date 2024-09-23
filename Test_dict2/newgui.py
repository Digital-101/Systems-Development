from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Product Management App')
root.geometry('500x550')
root.configure(bg='lightblue')

products = {'usb': 120, 'mouse': 130, 'xbox': 900}

# Header
header_label = Label(root, text='== Product Management ==', bg='aqua', font=('Arial', 16))
header_label.grid(row=0, column=0, columnspan=2, pady=10)

# Menu options
menu_label = Label(root, text='Choose an option:\n1. Add Product\n2. Update Product\n3. Get Product Price\n4. Delete Product\n5. Display All Products', bg='aqua')
menu_label.grid(row=1, column=0, columnspan=2, pady=10)

# Choice input
choice_label = Label(root, text='Enter choice (1-5):', bg='lightblue')
choice_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
choice_entry = Entry(root, bg='aqua')
choice_entry.grid(row=2, column=1, padx=5, pady=5)

# Product Name
product_label = Label(root, text='Enter product name:', bg='lightblue')
product_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)
product_entry = Entry(root)
product_entry.grid(row=3, column=1, padx=5, pady=5)

# Price input
price_label = Label(root, text='Enter price:', bg='lightblue')
price_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)
price_entry = Entry(root)
price_entry.grid(row=4, column=1, padx=5, pady=5)

# Price limit for filtering
price_limit_label = Label(root, text='Enter price limit for filtering:', bg='lightblue')
price_limit_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)
price_limit_entry = Entry(root, bg='yellow')
price_limit_entry.grid(row=5, column=1, padx=5, pady=5)

# Price range inputs
start_price_label = Label(root, text='Enter start price range:', bg='lightblue')
start_price_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)
start_price_entry = Entry(root, background='red')
start_price_entry.grid(row=6, column=1, padx=5, pady=5)

stop_price_label = Label(root, text='Enter stop price range:', bg='lightblue')
stop_price_label.grid(row=7, column=0, sticky=W, padx=5, pady=5)
stop_price_entry = Entry(root, bg='red')
stop_price_entry.grid(row=7, column=1, padx=5, pady=5)

def display_message(message):
    messagebox.showinfo("Information", message)

def get_price_range():
    try:
        start = float(start_price_entry.get())
        stop = float(stop_price_entry.get())
        filtered_products = [(product, price) for product, price in products.items() if start <= price <= stop]
        display_message(f"Products in the range R{start} - R{stop}: {filtered_products}")
    except ValueError:
        display_message("Please enter valid numeric values for the price range.")

def get_expensive():
    if not products:
        display_message("No products available.")
        return
    value = max(products.items(), key=lambda x: x[1])
    display_message(f'Most expensive product: {value}')

def get_cheaper():
    if not products:
        display_message("No products available.")
        return
    value = min(products.items(), key=lambda x: x[1])
    display_message(f'Cheapest product: {value}')

def get_products_cheaper_than():
    try:
        price_limit = float(price_limit_entry.get())
        prod = [product for product, price in products.items() if price < price_limit]
        display_message(f'Products cheaper than R{price_limit}: {prod}')
    except ValueError:
        display_message("Please enter a valid numeric value for the price limit.")

def menu():
    try:
        choice = int(choice_entry.get())
        msg = ''
        
        if choice == 1 or choice == 2:
            p_name = product_entry.get().lower()
            p_price = float(price_entry.get())
            products[p_name] = p_price
            msg = f'{p_name.capitalize()} added/updated successfully.'
        
        elif choice == 3:
            p_name = product_entry.get().lower()
            if p_name in products:
                msg = f'{p_name.capitalize()} price is: R{products[p_name]:.2f}'
            else:
                msg = f'{p_name.capitalize()} not found.'
        
        elif choice == 4:
            p_name = product_entry.get().lower()
            if p_name in products:
                del products[p_name]
                msg = f'{p_name.capitalize()} deleted successfully.'
            else:
                msg = f'{p_name.capitalize()} not found.'
        
        elif choice == 5:
            msg = f'All products: {products}'
        
        else:
            msg = "Invalid choice. Please enter a number between 1 and 5."
        
        display_message(msg)
    
    except ValueError:
        display_message("Invalid input. Please enter a number for the choice.")

# Action Buttons
submit_button = Button(root, text='Submit', command=menu, bg='aqua')
submit_button.grid(row=8, column=0, padx=5, pady=10)

expensive_button = Button(root, text='Get Most Expensive Product', command=get_expensive, bg='lightgreen')
expensive_button.grid(row=8, column=1, padx=5, pady=10)

cheaper_button = Button(root, text='Get Cheapest Product', command=get_cheaper, bg='lightgreen')
cheaper_button.grid(row=9, column=0, padx=5, pady=5)

filter_button = Button(root, text='Get Products Cheaper Than', command=get_products_cheaper_than, bg='yellow')
filter_button.grid(row=9, column=1, padx=5, pady=5)

range_button = Button(root, text='Get Products in Price Range', command=get_price_range, bg='red')
range_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)

root.mainloop()
