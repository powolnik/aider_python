import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("320x400")

    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 18), bd=5)
    entry.grid(row=0, column=0, columnspan=4, ipadx=80)

    def click(char):
        current = entry_var.get()
        if char == '.' and '.' in current:
            return
        entry_var.set(current + char)

    def evaluate():
        try:
            result = eval(entry_var.get())
            entry_var.set(str(result))
        except Exception as e:
            entry_var.set("Error")

    def clear():
        entry_var.set("")

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
        ('0', 4, 0), ('.', 4, 1) # Added '.' button at row 4 column 1
    ]

    for (text, row, col) in buttons:
        btn = tk.Button(root, text=text, font=('Arial', 16),
                        command=lambda t=text: click(t))
        btn.grid(row=row, column=col, sticky='nsew')

    operators = [
        ('+', 1, 3), ('-', 2, 3),
        ('*', 3, 3), ('/', 4, 3)
    ]

    for (text, row, col) in operators:
        btn = tk.Button(root, text=text, font=('Arial', 16),
                        command=lambda t=text: click(t))
        btn.grid(row=row, column=col, sticky='nsew')

    eq_btn = tk.Button(root, text='=', font=('Arial', 16), 
                      command=evaluate)
    eq_btn.grid(row=4, column=2, rowspan=2, sticky='nsew')

    clear_btn = tk.Button(root, text='C', font=('Arial', 16),
                         command=clear)
    clear_btn.grid(row=4, column=0, sticky='nsew')

    for i in range(6): # Now includes row 5 for the equals button's rowspan
        root.grid_rowconfigure(i, weight=1)

    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
