import tkinter

class Calculator_GUI:
    def __init__(self):
        
        #Create main window
        self.mw = tkinter.Tk()
        #Set the main title of GUI
        self.mw.title("My Calculator")
        
        #Defining the String variables
        self.lab_var = tkinter.StringVar()
        
        #Defining the String for the User Interface
        self.lab_label = tkinter.Label(self.mw, textvariable = self.lab_var )        
        
        #Setting the label variable with the display and input reset to 0
        self.lab_var.set("Total :           0")
        
        
        #Creating the buttons: Entry, Addition, Substraction and Reset
        self.entry = tkinter.Entry(self.mw, width = 15)
        self.Addition_label = tkinter.Button(self.mw, text = "+", command = self.calc_add)
        self.Substraction_label = tkinter.Button(self.mw, text = "-", command = self.calc_sub)
        self.Reset = tkinter.Button(self.mw, text = "Reset", command = self.calc_reset)
        
        #Equating the calculation to 0 for reset
        self.calc_total = 0
       
        #Packing all the Attributes
        self.lab_label.pack(side = "top")
        self.entry.pack(side = "top")
        self.Addition_label.pack(side = "left")
        self.Substraction_label.pack(side = "left")
        self.Reset.pack(side = "left")
        
        #Creating a standard tkinter function for operation
        tkinter.mainloop()
    
    #Defining the addition function for command referencing
    def calc_add(self):
         self.calc_total = self.calc_total + int(self.entry.get())
         self.lab_var.set("Total :           %d" %self.calc_total)

    #Defining the substraction function for command referencing
    def calc_sub(self):
         self.calc_total = self.calc_total - int(self.entry.get())
         self.lab_var.set("Total :           %d" %self.calc_total)

    #Defining the reset function for command referencing
    def calc_reset(self):
        reset = 0
        self.calc_total = 0
        self.lab_var.set("Total :           %d" %reset)
        
    
#Calling the Calculator class
Calculator_GUI()