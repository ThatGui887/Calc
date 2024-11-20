import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Create the entry widget for displaying input and results
        self.entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        # Create buttons dynamically
        for text, row, col in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(
            self.root, text=text, font=("Arial", 16), width=5, height=2,
            command=lambda t=text: self.on_button_click(t)
        )
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, symbol):
        if symbol == "=":
            try:
                result = eval(self.entry.get())  # Calculate the result
                self.entry.delete(0, tk.END)  # Clear the entry field
                self.entry.insert(0, str(result))  # Display the result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif symbol == "C":
            self.entry.delete(0, tk.END)  # Clear the entry field
        else:
            self.entry.insert(tk.END, symbol)  # Add symbol to the entry field

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

