import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)

        self.symbols = [["C", "(", ")", "<"],
                        ["7", "8", "9", "÷"],
                        ["4", "5", "6", "×"],
                        ["1", "2", "3", "-"],
                        [".", "0", "=", "+"]]

        self.create_gui()

    def create_gui(self):
        self.main_frame = ttk.Frame(self.master, padding=3)
        self.main_frame.grid(row=0, column=0)

        self.display = tk.Label(self.main_frame, bg="white", font=("arial", 30),
                                width=13, height=2, relief=tk.GROOVE, anchor="e")
        self.display.grid(row=0, column=0)

        self.buttons_frame = ttk.Frame(self.main_frame, padding=3)
        self.buttons_frame.grid(row=1, column=0)

        # creates all the buttons
        for row in range(len(self.symbols)):
            for col in range(len(self.symbols[0])):

                symbol = self.symbols[row][col]

                button = ttk.Button(self.buttons_frame, text=symbol, takefocus=False)
                button.grid(row=row, column=col, padx=1, ipady=20)

                # assigns the commands to the buttons
                if symbol == "C":
                    button["command"] = self.clear
                elif symbol == "<":
                    button["command"] = self.undo
                elif symbol == "=":
                    button["command"] = self.solve
                else:
                    button["command"] = lambda x=symbol: self.add_symbol(x)

                button.bind("<ButtonRelease-1>", self.check_error)

    def clear(self):
        self.display["text"] = ""

    def check_error(self, event):
        if self.display["text"] == "error":
            self.clear()

    def add_symbol(self, symbol):
        self.display["text"] = self.display["text"] + symbol

    def undo(self):
        self.display["text"] = self.display["text"][:-1]

    def solve(self):
        try:
            self.display["text"] = self.display["text"].replace("×", "*")
            self.display["text"] = self.display["text"].replace("÷", "/")
            # a bit yucky since we're using eval, but gets the job done
            self.display["text"] = str(eval(self.display["text"]))
        except Exception:
            self.display["text"] = "error"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
