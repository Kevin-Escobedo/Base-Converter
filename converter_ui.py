import num_converter
import tkinter

class Converter:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x300")
        self.root_window.resizable(0, 0)
        self.root_window.title("Number Converter")
        self.number = tkinter.Entry(self.root_window)
        self.base = tkinter.Entry(self.root_window)

    def run(self):
        tkinter.Label(self.root_window, text = "Number").grid(row=0)
        tkinter.Label(self.root_window, text = "Base").grid(row=1)
        self.number.grid(row=0, column=1)
        self.base.grid(row=1, column = 1)
        



if __name__ == "__main__":
    Converter().run()
