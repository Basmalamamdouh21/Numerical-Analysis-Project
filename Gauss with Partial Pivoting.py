from tkinter import *

window = Tk()
window.config(bg='#050100')
window.geometry('700x750')
window.title("Gauss Elimination with Partial Pivoting")

# واجهة الإدخال
rows = []
for i in range(3):
    cols = []
    for j in range(4):   
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx=10, pady=10)
        cols.append(e)
    rows.append(cols)


def get_matrix():
    matrix = []
    for row in rows:
        matrix.append([float(cell.get()) for cell in row])
    return matrix


def gauss_elimination_partial(matrix):
    n = 3
    steps_output = ""

   
    for i in range(n):
    
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        steps_output += f"\nPivot on row {i}, matrix:\n{format_matrix(matrix)}\n"

        # تصفير العناصر تحت العنصر الرئيسي
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n+1):
                matrix[j][k] -= factor * matrix[i][k]
            steps_output += f"Eliminating row {j} using row {i}, factor={factor:.2f}\n"
            steps_output += format_matrix(matrix) + "\n"

    # الحل العكسي
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        sum_ax = sum(matrix[i][j] * x[j] for j in range(i+1, n))
        x[i] = (matrix[i][n] - sum_ax) / matrix[i][i]
        steps_output += f"x[{i}] = {x[i]:.4f}\n"

    return x, steps_output


def format_matrix(matrix):
    return "\n".join(["\t".join([f"{val:.2f}" for val in row]) for row in matrix])
def solve_system():
    Steps.delete("1.0", END)
    try:
        matrix = get_matrix()
        solution, log = gauss_elimination_partial(matrix)
        Result['text'] = f"Solution: X1={solution[0]:.2f}, X2={solution[1]:.2f}, X3={solution[2]:.2f}"
        Steps.insert(END, log)
    except Exception as e:
        Result['text'] = f"Error: {e}"
        
        
ButtonGetX = Button(window, text="Solve System", bg='white', fg='red', command=solve_system)
ButtonGetX.grid(row=9, column=2, padx=20, pady=20)

Result = Label(window, text="   ", fg='red', bg='#050100')
Result.grid(row=10, column=2, padx=20, pady=20)

Steps = Text(window, height=25, width=90, bg="white")
Steps.grid(row=11, column=0, columnspan=5, padx=10)

window.mainloop()
