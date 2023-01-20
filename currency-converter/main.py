import tkinter as tk
import requests as req
from datetime import datetime


def currency_converter(from_curr, to_curr, amount) -> float:
    res = req.get(f'https://v6.exchangerate-api.com/v6/09d0f82d23ac956b094672cb/latest/{from_curr}').json()['conversion_rates']
    result = amount * res[to_curr]
    return result


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        res = req.get('https://v6.exchangerate-api.com/v6/09d0f82d23ac956b094672cb/latest/USD').json()['conversion_rates']

        # Setting up Initial Things
        self.title = 'Currency Converter'
        self.geometry('400x300')
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file='img/logo.png'))
        self.currency_converter = currency_converter

        # Creating a container
        container = tk.Frame(self, bg='gray50')
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Creating Title
        title = tk.Label(
            container, text='Welcome to Real Time Currency Converter',
            font=('Arial', 15), bg='#1F7EB5', fg='white', width='800'
        )
        title.pack(pady=0, padx=0)

        # Creating Intro Lable
        intro_label = tk.Label(
            container, text=f'1 USD = {res["UAH"]} UAH \n Date: {datetime.today().date()}',
            font=('Arial', 13), fg='black', bg='gray50',
        )
        intro_label.pack(pady=10)

        # Creating Converter
        converter_frame = tk.Frame(container, bg='gray50')

        lst = res.keys()
        self.first_dropdown = tk.StringVar(converter_frame)
        self.first_dropdown.set(list(lst)[0])
        self.input = tk.Entry(converter_frame, width=15, justify=tk.CENTER)

        om1 = tk.OptionMenu(converter_frame, self.first_dropdown, *lst)
        om1.grid(row=0, column=2, padx=5, pady=5)
        self.input.grid(row=1, column=2, padx=5, pady=5)

        self.second_dropdown = tk.StringVar(converter_frame)
        self.second_dropdown.set(list(lst)[1])
        self.output = tk.Label(converter_frame, width=15, justify=tk.CENTER, text='')

        om2 = tk.OptionMenu(converter_frame, self.second_dropdown, *lst)
        om2.grid(row=0, column=4, padx=5, pady=5)
        self.output.grid(row=1, column=4, padx=5, pady=5)

        convert_btn = tk.Button(
            converter_frame, font=('Arial', 13, 'bold'), text="Convert", fg="white", bg='#3EA9D0', command=self.convert
        )
        convert_btn.grid(row=2, column=3, padx=5, pady=5)

        converter_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def convert(self):
        amount = float(self.input.get())
        from_curr = self.first_dropdown.get()
        to_curr = self.second_dropdown.get()

        converted_amount = self.currency_converter(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.output.config(text=str(converted_amount))


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
