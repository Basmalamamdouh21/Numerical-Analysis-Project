from tkinter import *

window = Tk()
window.config(bg='#050100')
window.geometry('700x750')
window.title("Gauss-Jordan Elimination")

def getmatrix():
    matrix = []
    for row in rows:
        a = []
        for col in row:
            val = col.get()
            a.append(float(val))
        matrix.append(a)
    return matrix

def Get_GJ():
    r = getmatrix()
    Steps.delete('1.0', END)
    
    rows_num = len(r)
    cols_num = len(r[0])
    
    for i in range(rows_num):
        # Make the pivot 1
        pivot = r[i][i]
        if pivot == 0:
            for k in range(i+1, rows_num):
                if r[k][i] != 0:
                    r[i], r[k] = r[k], r[i]
                    Steps.insert(END, f"Swapped row {i+1} with row {k+1}:\n{r}\n\n")
                    pivot = r[i][i]
                    break
        if pivot == 0:
            Steps.insert(END, f"Cannot solve due to zero pivot in row {i+1}\n")
            return

        for j in range(cols_num):
            r[i][j] /= pivot
        Steps.insert(END, f"Make pivot in row {i+1} = 1:\n{r}\n\n")

        # Make all other elements in the column zero
        for k in range(rows_num):
            if k != i:
                factor = r[k][i]
                for j in range(cols_num):
                    r[k][j] -= factor * r[i][j]
                Steps.insert(END, f"Make column {i+1} element in row {k+1} = 0:\n{r}\n\n")

    x1, x2, x3 = r[0][3], r[1][3], r[2][3]
    Result['text'] = f"Solution: X1 = {x1:.3f}, X2 = {x2:.3f}, X3 = {x3:.3f}"

rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx='10', pady='10')
        cols.append(e)
    rows.append(cols)

ButtonGetX = Button(window, text="Solve System (Gauss-Jordan)", bg='white', fg='red', command=Get_GJ)
ButtonGetX.grid(row=9, column=1, columnspan=2, padx='20', pady='20')

Result = Label(window, text="   ", fg='red', bg='#050100')
Result.grid(row=10, column=1, columnspan=2, padx='20', pady='20')

Steps = Text(window, height=25, width=90, bg="white")
Steps.grid(row=11, column=0, columnspan=4)

window.mainloop()