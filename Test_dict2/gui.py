from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Product App')
root.geometry('700x600')

products = {'usb': 120, 'mouse': 130, 'xbox':900}

#Labels and Entries
lbl = Label(root, text='==Choose Option==', background='aqua').pack()
lblc = Label(root, text='--1.ADD \n2.UPDATE \n3.GET PRICE \n4.DELETE-- \n5.DISPLAY\n', background='aqua')
lblc.pack()
lblec = Label(root, text='Enter choice:').pack()
cEnt = Entry(root, background='aqua')
cEnt.pack()

lblp= Label(root, text='Enter product name:')
lblp.pack()

pEnt = Entry(root)
pEnt.pack()

lblpr= Label(root, text='Enter price:')
lblpr.pack()

prEnt = Entry(root)
prEnt.pack()

lblpl= Label(root, text='Enter price limit:')
lblpl.pack()

plEnt = Entry(root, background='yellow')
plEnt.pack()

lblst= Label(root, text='Enter start price range:')
lblst.pack()
stEnt = Entry(root, background='red')
stEnt.pack()

lblsp= Label(root, text='Enter stop price range:')
lblsp.pack()
spEnt = Entry(root, background='red')
spEnt.pack()

def get_price_range():
    start = float(stEnt.get())
    stop = float(spEnt.get())
    lblR = Label(root, text=f"Products in the range R{start} - R{stop}:")
    lblR.pack()
    filtered_products = [(product, price) for product, price in products.items() if start <= price <= stop]
    lblO = Label(root, text=f'{filtered_products}')
    lblO.pack()
    return filtered_products

def get_expensive():
    value = ''
    if not products:
        return None
    value = max(products.items(), key=lambda x: x[1])
    lblx = Label(root, text=f'{value}')
    lblx.pack()
    return value

def get_cheaper():
    value = ''
    if not products:
        return None
    value = min(products.items(), key=lambda x: x[1])
    lblc = Label(root, text=f'{value}')
    lblc.pack()
    return value

def get_products_cheaper_than():
    """Returns a list of products cheaper than the given price."""
    price_limit = int(plEnt.get())
    prod = [product for product, price in products.items() if price < price_limit]
    lblx = Label(root, text=f'{prod}')
    lblx.pack()
    return prod

def menu():
    try:
        #print('==Choose option==')
        choice = int(cEnt.get())
        display = ''
        msg = ''
        if choice == 1:
            p_name = pEnt.get().lower()
            p_price = float(prEnt.get())
            new_entry = {p_name:p_price}
            products.update(new_entry)
            display = products
        elif choice == 2:
            p_name = pEnt.get().lower()
            p_price = float(prEnt.get())
            new_entry = {p_name:p_price}
            products.update(new_entry)
            display = products 
        elif choice == 3:
            p_name = pEnt.get().lower()
            if p_name in products:
                msg = (f'{p_name} price is: R{products.get(p_name):.2f}')
            else:
                msg = (f'{p_name} not in dictionary.')
        elif choice == 4:
            p_name = pEnt.get()
            if p_name in products:
                del products[p_name]
                msg = (f'{p_name} deleted successfully')
                display = (products)
            else:
                msg = (f'{p_name} not in dictionary')
        elif choice == 5:
            display = products
        lbld = Label(root, text=f'{display}')
        lbld.pack()
        lblm = Label(root, text=f'{msg}')
        lblm.pack()
        return display
    
    except ValueError:
        messagebox.showerror('Error', 'Invalid choice')

btn = Button(root, text='Submit', command=menu, background='aqua')
btn.pack()

btne = Button(root, text='Get Expensive', command=get_expensive)
btne.pack()

btnc = Button(root, text='Get Cheaper', command=get_cheaper)
btnc.pack()

btnp = Button(root, text='Get Products', command=get_products_cheaper_than, background='yellow')
btnp.pack()

btnpr = Button(root, text='Get Range', command=get_price_range, background='red')
btnpr.pack()

root.mainloop()
