from tkinter import *

window = Tk()
window.config(bg='#050100')
window.geometry('700x750')
window.title("Gauss-Jordan Elimination with Partial Pivoting")

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
        # Partial Pivoting: Find max absolute value in column i from row i to end
        max_row = i
        max_val = abs(r[i][i])
        for k in range(i+1, rows_num):
            if abs(r[k][i]) > max_val:
                max_val = abs(r[k][i])
                max_row = k
        if max_val == 0:
            Steps.insert(END, f"No unique solution; column {i+1} is zero in all rows below.\n")
            return
        if max_row != i:
            r[i], r[max_row] = r[max_row], r[i]
            Steps.insert(END, f"Swapped row {i+1} with row {max_row+1} for partial pivoting:\n{r}\n\n")

        # Normalize pivot row
        pivot = r[i][i]
        for j in range(cols_num):
            r[i][j] /= pivot
        Steps.insert(END, f"Make pivot in row {i+1} = 1:\n{r}\n\n")

        # Eliminate other entries in column i
        for k in range(rows_num):
            if k != i:
                factor = r[k][i]
                for j in range(cols_num):
                    r[k][j] -= factor * r[i][j]
                Steps.insert(END, f"Make column {i+1} zero in row {k+1}:\n{r}\n\n")

    # Display final solution
    solution = [r[i][-1] for i in range(rows_num)]
    result_text = "Solution: " + ", ".join([f"X{i+1} = {val:.3f}" for i, val in enumerate(solution)])
    Result['text'] = result_text

rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx='10', pady='10')
        cols.append(e)
    rows.append(cols)

ButtonGetX = Button(window, text="Solve System (Gauss-Jordan + Pivoting)", bg='white', fg='red', command=Get_GJ)
ButtonGetX.grid(row=9, column=1, columnspan=2, padx='20', pady='20')

Result = Label(window, text="   ", fg='red', bg='#050100')
Result.grid(row=10, column=1, columnspan=2, padx='20', pady='20')

Steps = Text(window, height=25, width=90, bg="white")
Steps.grid(row=11, column=0, columnspan=4)

window.mainloop()