import tkinter as tk




class CalculatorApp:
    def __init__(self) -> None:
        
        self.root = tk.Tk()
        self.root.geometry("300x280")
        self.root.bind("<Return>", lambda event: self.evaluate_calculation())
        self.root.title('Calculator')
        self.text_result = tk.Text( self.root, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=5)

        btns = [
        ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("4", 3, 0), ("5", 3, 1),
        ("6", 3, 2), ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("0", 5, 1)
        ]

        for btn_text, row, col in btns:
            btn = tk.Button( self.root, text=btn_text, command=lambda text=btn_text:  self.add_to_calculation(text), width=5, font=("Arial", 13))
            btn.grid(row=row, column=col)

        btn_clear = tk.Button( self.root, text="C", command= self.clear_calculation, width=5, font=("Arial", 13))
        btn_clear.grid(row=5, column=0)

        btn_equal = tk.Button( self.root, text="=", command= self.evaluate_calculation, width=5, font=("Arial", 13))
        btn_equal.grid(row=5, column=2)

        btn_plus = tk.Button( self.root, text="+", command=lambda:  self.add_to_calculation("+"), width=5, font=("Arial", 13))
        btn_plus.grid(row=2, column=3)

        btn_minus = tk.Button( self.root, text="-", command=lambda: self. add_to_calculation("-"), width=5, font=("Arial", 13))
        btn_minus.grid(row=3, column=3)

        btn_multiply = tk.Button( self.root, text="*", command=lambda:  self.add_to_calculation("*"), width=5, font=("Arial", 13))
        btn_multiply.grid(row=4, column=3)

        btn_divide = tk.Button( self.root, text="/", command=lambda:  self.add_to_calculation("/"), width=5, font=("Arial", 13))
        btn_divide.grid(row=5, column=3)





    def add_to_calculation(value,self):
        self.current_text = self.text_result.get("1.0", "end-1c")
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, self.current_text + str(value))

    def clear_calculation(self):
        self.text_result.delete("1.0", tk.END)

    def evaluate_calculation(self):
        try:
            self.result = eval(self.text_result.get("1.0", "end-1c"))
            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, self.result)
        except Exception as e:
            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, "Error")
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app=CalculatorApp()
    app.run()
