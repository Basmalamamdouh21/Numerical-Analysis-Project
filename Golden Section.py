from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math

Window = Tk()
Window.title("Golden Section Search Method")
Window.geometry('1000x700')
Window.config(bg='#050100')
f = ("Helvetica", 9, 'bold')

# Function to get the input values
def get_XLower():
    Xlo = float(XLowerEntry.get())
    return Xlo

def get_Xupper():
    Xu = float(XUpperEntry.get())
    return Xu

def get_Function(x):
    Func = str(eval(entry.get()))
    return Func

def golden_section_search():
    xl = get_XLower()
    xu = get_Xupper()

    phi = 0.618  # Golden Ratio
    d = phi * (xu - xl)  # Initial interval width

    x1 = xl + d
    x2 = xu - d

    fx1 = float(get_Function(x1))
    fx2 = float(get_Function(x2))
    fxl = float(get_Function(xl))  # f(Xl)
    fxu = float(get_Function(xu))  # f(Xu)
    
    iter_count = 0
    results = []

    while (xu - xl) > 1e-5:  # Stop when the interval is sufficiently small
        iter_count += 1
        
        # Insert values into the table for each iteration
        iter.insert(parent='', index='end', iid=iter_count, text='', values=(iter_count, xl, xu, x1, x2, fxl, fxu, fx1, fx2, d))
        
        # Update the interval
        if fx1 > fx2:
            xl = x2
            x2 = x1
            fx2 = fx1
            d = phi * (xu - xl)
            x1 = xl + d
            fx1 = float(get_Function(x1))
        else:
            xu = x1
            x1 = x2
            fx1 = fx2
            d = phi * (xu - xl)
            x2 = xu - d
            fx2 = float(get_Function(x2))

        # Recalculate f(Xl) and f(Xu)
        fxl = float(get_Function(xl))
        fxu = float(get_Function(xu))

    # Display the result
    ResultRoot['text'] = f"The Root is: { (xl + xu) / 2 }"
    return (xl + xu) / 2


######################################################
################## GUI ##############################
Frame1 = Frame(Window, bg='#EEEDEC', width='300', height='200')
Frame1.pack(side=TOP, padx='20', pady='20')

LabelTitle = Label(Frame1, bg='#EEEDEC', text='Golden Section Search Method', fg='red', width='300', font=('Helvetica', 16, 'bold'))
LabelTitle.pack(padx='5', pady='5')

XlowerLabel = Label(Window, text=' X lower', bg='#050100', fg='red', font=('Helvetica', 11, 'bold')).pack(padx='10')
XLowerEntry = Entry(Window, borderwidth=5, width='30', justify=CENTER)
XLowerEntry.pack(padx='5', pady='5')

XupperLabel = Label(Window, text=' X Upper', bg='#050100', fg='red', font=('Helvetica', 11, 'bold')).pack(padx='10')
XUpperEntry = Entry(Window, borderwidth=5, width='30', justify=CENTER)
XUpperEntry.pack(padx='5', pady='5')

f = Label(Window, text="f(x)", bg='#050100', fg='red', font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window, borderwidth=5, width='30', justify=CENTER)
entry.pack(padx='10', pady='10')

##### Table ##################

iter = ttk.Treeview(Window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show='headings', height=9)
iter.pack()
iter.column("1", anchor=CENTER, stretch=NO, width=100)
iter.heading(1, text='i')
iter.column("2", anchor=CENTER, stretch=NO, width=100)
iter.heading(2, text='Xl')
iter.column("3", anchor=CENTER, stretch=NO, width=100)
iter.heading(3, text='Xu')
iter.column("4", anchor=CENTER, stretch=NO, width=100)
iter.heading(4, text='X1')
iter.column("5", anchor=CENTER, stretch=NO, width=100)
iter.heading(5, text='X2')
iter.column("6", anchor=CENTER, stretch=NO, width=100)
iter.heading(6, text='f(Xl)')
iter.column("7", anchor=CENTER, stretch=NO, width=100)
iter.heading(7, text='f(Xu)')
iter.column("8", anchor=CENTER, stretch=NO, width=100)
iter.heading(8, text='f(X1)')
iter.column("9", anchor=CENTER, stretch=NO, width=100)
iter.heading(9, text='f(X2)')
iter.column("10", anchor=CENTER, stretch=NO, width=100)
iter.heading(10, text='D')

ButtonRes = Button(Window, text='Determine Root', fg='red', font=('Helvetica', 11, 'bold'), command=golden_section_search).pack(padx='5', pady='5')

ResultRoot = Label(Window, text=" ", fg='#e8e8e8', font=('Helvetica', 14, 'bold'), bg='#050100')
ResultRoot.pack()

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='red')
style.configure('Treeview.Heading', background="red3")
style.map("Treeview", background=[('selected', 'red')])

###################################################################################

Window.mainloop()