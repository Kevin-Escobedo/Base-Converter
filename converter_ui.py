import num_converter
import tkinter

class Converter:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x150")
        self.root_window.resizable(0, 0)
        self.root_window.title("Number Converter")
        self.number = tkinter.Entry(self.root_window)
        self.base = tkinter.Entry(self.root_window)
        self.new_base = tkinter.Entry(self.root_window)
        self.result = tkinter.StringVar()
        self.converted_result = ""

    def get_first_number(self):
        try:
            return int(self.number.get())
        except:
            self.result.set("Invalid Input for Number")

    def get_first_base(self):
        try:
            return int(self.base.get())
        except:
            self.result.set("Invalid Input for Base")

    def get_second_base(self):
        try:
            return int(self.new_base.get())
        except:
            self.result.set("Invalid Input for New Base")
        

    def convert(self):
        original_number = self.get_first_number()
        original_base = self.get_first_base()
        other_base = self.get_second_base()
        self.converted_result = num_converter.convert_to_base(num_converter.convert_to_decimal(original_number, original_base), other_base)
        self.result.set("Result: {}".format(self.converted_result))

    def run(self):
        tkinter.Label(self.root_window, text = "Number").grid(row=0, column = 1, sticky = tkinter.NSEW)
        tkinter.Label(self.root_window, text = "Base").grid(row=1, column = 1, sticky = tkinter.NSEW)
        tkinter.Label(self.root_window, text = "New Base").grid(row=2, column = 1, sticky = tkinter.NSEW)
        tkinter.Label(self.root_window, textvariable = self.result).grid(row=4, column = 2, columnspan = 4)

        self.result.set("{}".format(self.converted_result))
        
        self.number.grid(row=0, column=2, sticky = tkinter.NSEW)
        self.base.grid(row=1, column = 2, sticky = tkinter.NSEW)
        self.new_base.grid(row=2, column = 2, sticky = tkinter.NSEW)

        button = tkinter.Button(self.root_window, text = "Convert", command = self.convert)
        button.grid(row = 3, column = 2, sticky = tkinter.NSEW)

        self.root_window.mainloop()

        



if __name__ == "__main__":
    Converter().run()
