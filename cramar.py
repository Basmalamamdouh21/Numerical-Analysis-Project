from tkinter import *

window = Tk()
window.config(bg='#050100')
window.geometry('800x800')
window.title("Cramer's Rule (No NumPy)")

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub)
    return det


def replace_column(matrix, column_index, new_column):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        new_matrix[i][column_index] = new_column[i]
    return new_matrix

def getmatrix():
    matrix = []
    for row in rows:
        a = []
        for col in row:
            m = col.get()
            a.append(int(m))
        matrix.append(a)
    return matrix

def Get_GE():
    Steps.delete("1.0", END)
    r = getmatrix()
    B = [r[i][3] for i in range(3)]
    A = [row[:3] for row in r]

    Steps.insert(END, f"Matrix A: {A}\n")
    Steps.insert(END, f"Vector B: {B}\n")

    D = determinant(A)
    Steps.insert(END, f"det(D) = {D}\n\n")
    if D == 0:
        Result['text'] = "No unique solution: determinant is zero."
        return

    A1 = replace_column(A, 0, B)
    D1 = determinant(A1)
    Steps.insert(END, f"A1 (replace col 0): {A1}\n")
    Steps.insert(END, f"det(D1) = {D1}\n\n")

    A2 = replace_column(A, 1, B)
    D2 = determinant(A2)
    Steps.insert(END, f"A2 (replace col 1): {A2}\n")
    Steps.insert(END, f"det(D2) = {D2}\n\n")

    A3 = replace_column(A, 2, B)
    D3 = determinant(A3)
    Steps.insert(END, f"A3 (replace col 2): {A3}\n")
    Steps.insert(END, f"det(D3) = {D3}\n\n")

    x1 = round(D1 / D, 4)
    x2 = round(D2 / D, 4)
    x3 = round(D3 / D, 4)

    Result['text'] = f"Solution (X1, X2, X3): ({x1}, {x2}, {x3})"
    Steps.insert(END, f"X1 = D1 / D = {x1}\n")
    Steps.insert(END, f"X2 = D2 / D = {x2}\n")
    Steps.insert(END, f"X3 = D3 / D = {x3}\n")


rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx='10', pady='10')
        cols.append(e)
    rows.append(cols)


ButtonGetX = Button(window, text="Solve System", bg='white', fg='red', command=Get_GE)
ButtonGetX.grid(row=9, column=2, padx='20', pady='20')


Result = Label(window, text="   ", fg='red', bg='#050100')
Result.grid(row=10, column=2, padx='20', pady='20')


Steps = Text(window, height=25, width=100, bg="white")
Steps.grid(row=11, column=0, columnspan=4, padx=10)

window.mainloop()

