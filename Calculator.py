import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # Create display
        self.display = ttk.Entry(root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        ttk.Button(root, text="C", command=self.clear).grid(row=5, column=0, columnspan=4, padx=2, pady=2, sticky="nsew")
        
        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        self.equation = ""
    
    def click(self, button):
        if button == "=":
            try:
                self.equation = str(eval(self.equation))
                self.display.delete(0, tk.END)
                self.display.insert(0, self.equation)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.equation = ""
        else:
            self.equation += button
            self.display.delete(0, tk.END)
            self.display.insert(0, self.equation)
    
    def clear(self):
        self.equation = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
