import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd


# Function for replacing symbols
def replace_symbols():
    main_text = text.get('1.0', tk.END)
    old_symbol, new_symbol = symbol2.get(), symbol3.get()
    # Checking for correct input
    if len(old_symbol) == 0:
        messagebox.showerror(title='Attention', message='You did not enter any symbol!!!')
    else:
        # The result of replacing symbols
        text.delete(1.0, tk.END)
        text.insert(1.0, main_text.replace(old_symbol, new_symbol))


# Function for counting symbols
def count_symbols():
    main_text = text.get('1.0', tk.END)
    symbol = symbol1.get()
    # Checking for correct input
    if len(symbol) == 0:
        messagebox.showerror(title='Attention', message='You did not enter any symbol!!!')
    else:
        # Field for output result of counting
        result = tk.Label(win, text=f'{main_text.count(symbol)}', font=('Arial', 15), width=10)
        result.grid(row=1, column=2, stick='wens', padx=5)


# Open the file
def open_file():
    fname = fd.askopenfilename(
        title='Select file',
        filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
    )
    with open(fname) as f:
        ftext = f.read()
        text.delete(1.0, tk.END)
        text.insert(1.0, ftext)


# Save the file
def save_file():
    fname = fd.asksaveasfile(filetypes=(("txt files", "*.txt"), ("all files", "*.*"))).name
    with open(fname, 'w') as f:
        ftext = text.get(1.0, tk.END)
        f.write(ftext)


# Main window
win = tk.Tk()
win.geometry('500x500')
win['bg'] = 'gray22'
win.title('Текст')

# Field for input main text
text_frame = tk.Frame(win)

scrollbar_y = tk.Scrollbar(text_frame, orient=tk.VERTICAL)
scrollbar_y.pack(side="right", fill="y")

scrollbar_x = tk.Scrollbar(text_frame, orient=tk.HORIZONTAL)
scrollbar_x.pack(side="bottom", fill="x")

text = tk.Text(text_frame, font=('Arial', 15), height=10, width=40, wrap='none',
               xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
text.pack(side="top", fill="both")

scrollbar_y.config(command=text.yview)
scrollbar_x.config(command=text.xview)

text_frame.grid(row=0, column=0, columnspan=3, stick='wens', padx=5, pady=5)

# Button which counts symbol in the text
count_btn = tk.Button(text='Count', font=('Arial', 13), command=lambda: count_symbols())
count_btn.grid(row=1, column=0, stick='wens', padx=5, pady=5)

# Field for input symbol
symbol1 = tk.Entry(win, font=('Arial', 15), width=10)
symbol1.grid(row=1, column=1, stick='wens', padx=5)

count_input = tk.Label(win, text='', font=('Arial', 15), width=10)
count_input.grid(row=1, column=2, stick='wens', padx=5)

# Button which replace the entered symbol for a new one
replace_btn = tk.Button(text='Replace', font=('Arial', 13), command=lambda: replace_symbols())
replace_btn.grid(row=2, column=0, stick='wens', padx=5, pady=5)

# Field for input symbols which must be replaced for a new one
symbol2 = tk.Entry(win, font=('Arial', 15), width=10)
symbol2.grid(row=2, column=1, stick='wens', padx=5)

# Field for input new symbols
symbol3 = tk.Entry(win, font=('Arial', 15), width=10)
symbol3.grid(row=2, column=2, stick='wens', padx=5)

# Menu
menu = tk.Menu(win)
filemenu = tk.Menu(menu, tearoff=0)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Open", command=open_file)
menu.add_cascade(label="File", menu=filemenu)

win.config(menu=menu)

win.mainloop()
