from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Demographic GUI')
root.geometry('500x300')

#Entries with #Labels
lbl1 = Label(root, text='Enter Age:').pack()
eA = Entry(root)
eA.pack()

lbl2 = Label(root, text='Enter Gender:').pack()
eG = Entry(root)
eG.pack()

lbl3 = Label(root, text='Enter Marital Status:').pack()
eMs = Entry(root)
eMs.pack()

def check_demographic():
    try:
        age = int(eA.get())
        gender = eG.get().lower()
        marital_status = eMs.get().lower()
        demo = ''
        if gender == 'male' and age < 30:
            demo = 'You are a bachelor!'
        elif gender == 'male' and age >= 30 and age <65:
            if marital_status == 'married':
                demo = 'You are a settled man!'
            else:
                demo = 'You are a bachelor looking for love!'
        elif gender == 'female' and age < 30 and age <65:
            demo = 'You are a young lady!'
        elif gender == 'female' and age >= 30 and age <65:
            if marital_status == 'married':
                demo = 'You are a happy homemaker!'
            else:
                demo = 'You are a single lady looking for love!'
        elif age >= 65:
            demo = "You are a golden ager!"
        else:
            messagebox.showerror('Bad Input', 'Enter required fields')
        lbl4 = Label(root, text=f'{demo}')
        lbl4.pack()
        return demo
    except ValueError:
        messagebox.showerror('Error!', 'Invalid Input')

btn = Button(root, text='Submit', command=check_demographic)
btn.pack()

root.mainloop()