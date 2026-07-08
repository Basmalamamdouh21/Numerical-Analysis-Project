from os import remove  # remove elements from matrix
from tkinter import *
window = Tk()
window.config(bg='#050100')
window.geometry('600x700')
window.title("LU Decomposition with Partial Pivoting and Dynamic Recording")

def getmatrix():
    matrix = []
    for row in rows:
        a = []
        for col in row:
            m = col.get()
            a.append(int(m))
        matrix.append(a)
    print(matrix)
    return matrix

rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx='10', pady='10')
        cols.append(e)
    rows.append(cols)

def record_step(text):
    """ Function to record a step into the Text widget """
    Steps.insert(END, text + '\n')
    Steps.yview(END)  # Scroll to the end to see the latest addition

def Get_GE():
    r = getmatrix()
    b1 = r[0][3]
    b2 = r[1][3]
    b3 = r[2][3]
    
    # Perform LU Decomposition with Partial Pivoting
    n = 3  # For 3x3 system
    for k in range(n):
        # Partial Pivoting: Find the row with the largest absolute value in column k
        max_row = max(range(k, n), key=lambda i: abs(r[i][k]))
        if max_row != k:
            # Swap rows
            r[k], r[max_row] = r[max_row], r[k]
            record_step(f"Swapped rows {k} and {max_row}: {r}")

        for i in range(k+1, n):
            if r[k][k] == 0:
                record_step("Matrix is singular, cannot proceed with LU decomposition")
                return
            factor = r[i][k] / r[k][k]
            # Update the matrix
            for j in range(k, n+1):
                r[i][j] -= factor * r[k][j]
            record_step(f"Updated row {i}: {r[i]}")

    # After the loop, r contains the LU decomposition
    record_step("LU Decomposition (Matrix after Gaussian elimination):")
    record_step(str(r))

    # Extract U matrix (upper triangular part)
    u = [[r[i][j] if i <= j else 0 for j in range(n)] for i in range(n)]
    record_step(f"U Matrix (Upper Triangular): {u}")

    # Extract L matrix (lower triangular part)
    l = [[1 if i == j else r[i][j] if i > j else 0 for j in range(n)] for i in range(n)]
    record_step(f"L Matrix (Lower Triangular): {l}")

    # Forward substitution (L * C = B)
    c1 = b1 / l[0][0]
    c2 = (b2 - l[1][0] * c1) / l[1][1]
    c3 = (b3 - l[2][0] * c1 - l[2][1] * c2) / l[2][2]
    record_step(f"Forward substitution: c1={c1}, c2={c2}, c3={c3}")

    CResult['text'] = f"(C1, C2, C3): {c1}, {c2}, {c3}"

    # Back substitution (U * X = C)
    x3 = c3 / u[2][2]
    x2 = (c2 - u[1][2] * x3) / u[1][1]
    x1 = (c1 - u[0][1] * x2 - u[0][2] * x3) / u[0][0]
    
    record_step(f"Back substitution: x1={x1}, x2={x2}, x3={x3}")
    Result['text'] = f"After Solving The System, (X1, X2, X3): {x1}, {x2}, {x3}"

    # Display steps
    record_step("LU Decomposition with Partial Pivoting")
    record_step(f"U Matrix:\n{u}")
    record_step(f"L Matrix:\n{l}")
    record_step(f"Forward substitution results: c1={c1}, c2={c2}, c3={c3}")
    record_step(f"Back substitution results: x1={x1}, x2={x2}, x3={x3}")

ButtonGetX = Button(window, text="Solve System", bg='white', fg='red', command=Get_GE).grid(row=9, column=2, padx='20', pady='20')
Result = Label(window, text="   ", fg='red', bg='#050100')
Result.grid(row=10, column=2, padx='20', pady='20')
CResult = Label(window, text="   ", fg='red', bg='#050100')
CResult.grid(row=9, column=1, padx='20', pady='20')
Steps = Text(window, height=25, width=100, bg="white")
Steps.grid(row=11, column=2)

window.mainloop()