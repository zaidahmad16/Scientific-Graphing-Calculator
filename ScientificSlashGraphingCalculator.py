#importing all important libraries
import tkinter as tk
import random
import tkinter.messagebox
import math
import matplotlib.pyplot as plt
import numpy as np


#Setting up base design
window = tk.Tk()
window. geometry("1185x568+0+0")
window.resizable(width=False, height=False)
window.title('Scientific Calculator')
window.configure(background = 'black')

calc = tk.Frame(window)
calc.grid()

graphCal = tk.Tk()
graphCal. geometry("500x568+0+0")
graphCal.title("Graphing Calculator")
graphCal.configure(background = 'grey10')

entry = tk.Entry(graphCal)
entry.pack()

error_label = tk.Label(graphCal, text="")
error_label.pack()

default_color = 'blue'

#global default_color,error_label,entry

def switch_to_graphing():
  window.withdraw()
  graphCal.deiconify()
  
def switch_to_scientific():
  graphCal.withdraw()
  window.deiconify()


def plot_graph():
    function = entry.get()
    x = np.linspace(-10, 10, 400)
    try:
        y = eval(function)
        plt.plot(x, y, color=color_var)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of ' + function)
        plt.grid(True)
        plt.show()
        error_label.config(text="")
    except Exception as e:
        error_label.config(text="Error: " + str(e))


color_var = default_color

    
def add_to_expression(char):
    if char == 'x':
        entry.insert(tk.END, char)  # Add 'x' as a variable
    elif char == 'sin':
        entry.insert(tk.END, 'np.sin(')
    elif char == 'cos':
        entry.insert(tk.END, 'np.cos(')
    else:
        entry.insert(tk.END, char)

def clear_expression():
    # Clear the expression in the entry box
    entry.delete(0, tk.END)


class Calc():
  def __init__(self):
    self.total = 0
    self.current = ''
    self.user_input = True
    self.check_sum = False
    self.option = ''
    self.result = False

  #Function to handle number button press
  def NumberPressed(self, num):
    self.result = False
    firstNumber = txtDisplay.get()
    secondNumber = str(num)
    if self.user_input:
      self.current = secondNumber
      self.user_input = False
    else:
      if secondNumber == '.':
        if firstNumber == secondNumber:
          return
      self.current = firstNumber + secondNumber
    self.display(self.current)

  #Function to calculate the total sum
  def sum_total(self):
    self.result = True
    self.current = float(self.current)
    if self.check_sum == True:
      self.basic_functions()
    else:
      self.total = float(txtDisplay.get())
  
  #Function to display the value on the calculator screen
  def display(self,value):
    txtDisplay.delete(0, tk.END)
    txtDisplay.insert(0, value)
    
  #Function to clear the current input
  def clear_function(self):
    self.result = False
    self.current = '0'
    self.display(0)
    self.user_input = True
    
  #Function to clear the entire calculator
  def clear_all(self):
    self.clear_function()
    self.total = '0'
    
  #Function to perform basic arithmetic operations
  def basic_functions(self):
    if self.option ==  'add':
      self.total += self.current
    if self.option == 'sub':
      self.total -= self.current
    if self.option == 'multi':
      self.total *= self.current
    if self.option == 'divide':
      self.total /= self.current
    if self.option == 'mod':
      self.total %= self.current
    self.user_input = True
    self.check_sum = False
    self.display(self.total)
  
  #Function to handle arithmetic operation button presses
  def operation(self, op):
    self.current = float(self.current)
    if self.check_sum:
      self.basic_functions()
    elif  not self.result:
      self.total = self.current
      self.user_input = True
    self.check_sum = True
    self.option = op
    self.result = False

  #Function to calculate square root
  def squared(self):
    try:
      self.result = False
      self.current = math.sqrt(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

  def PM_Pressed(self):
    try:
      self.result = False
      self.current = -(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  #Function to handle sin button press
  def sinPressed(self):
    try:
      self.result = False
      self.current = math.sin(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

  #Function to handle cos button press
  def cosinePressed(self):
    try:
      self.result = False
      self.current = math.cos(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  #Function to handle tan button press
  def tangentPressed(self):
    try:
      self.result = False
      self.current = math.tan(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
  
  #Function to handle Arcsin button press
  def inverseSinPressed(self):
    try:
      self.result = False
      self.current = math.asinh(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  #Function to handle Arccos button press
  def inverseCosinePressed(self):
    try:
      self.result = False
      self.current = math.acosh(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  #Function to get exponents
  def exponents(self):
    try:
      self.result = False
      self.current = math.exp(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
  #Function for logarithms
  def logarithm(self):
    try:
      self.result = False
      self.current = math.log(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  #Function to handle rounding
  def round(self):
    try:
      self.result = False
      self.current = round(self.current,1)
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  #Function to insert the π value
  def pi(self):
    try:
      self.result = False
      self.current = math.pi(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

  #
  def SineH(self):
    try:
      self.result = False
      self.current = math.sinh(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

      
  def CosineH(self):
    try:
      self.result = False
      self.current = math.cosh(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def TangentH(self):
    try:
      self.result = False
      self.current = math.tanh(math.radians(float(txtDisplay.get())))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def degrees(self):
    try:
      self.result = False
      self.current = math.degrees(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def E(self):
    try:
      self.result = False
      self.current = math.e
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def Pi_2(self):
    try:
      self.result = False
      self.current = math.tau
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def log_2(self):
    try:
      self.result = False
      self.current = math.log2(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def log_10(self):
    try:
      self.result = False
      self.current = math.log10(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      
  def log1p(self):
    try:
      self.result = False
      self.current = math.log1p(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")

  def expm1(self):
    try:
      self.result = False
      self.current = math.expm1(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
    
  def gamma(self):
    try:
      self.result = False
      self.current = math.lgamma(float(txtDisplay.get()))
      self.display(self.current)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Check your values and operators")
      

cal_app = Calc()

txtDisplay = tk.Entry(calc,font = ('Lato',20,'bold'),bg='black',fg='white',justify=tk.RIGHT, bd=30,width=28)
txtDisplay.grid(row = 0, column = 0,columnspan = 4, pady = 1)
txtDisplay.insert(0,"0")

#Order for the numberpad
numberpad = "7894561230"

#Default Value
i = 0

cal_button = []

#Number buttons won't work without this
for j in range(2,5):
  for k in range(3):
    cal_button.append(tk.Button(calc,width = 6,height = 2,font = ('Lato',20,'bold'),bg='#505050',fg='white',bd = 4, text = numberpad[i]))
    cal_button[i].grid(row = j, column= k, pady = 1)
    cal_button[i]["command"] = lambda x = numberpad[i]: cal_app.NumberPressed(x)
    i+=1

# Just the visuals for multiple buttons
add_button = tk.Button(calc,text="+",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#FF9500",command=lambda:cal_app.operation("add")).grid(row=1, column= 3, pady = 1)

sub_button = tk.Button(calc,text="-",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#FF9500",command=lambda:cal_app.operation("sub")).grid(row=2, column= 3, pady = 1)

multi_button = tk.Button(calc,text="x",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white",bg="#FF9500",command=lambda:cal_app.operation("multi")).grid(row=3, column= 3, pady = 1)

divde_button = tk.Button(calc,text="÷",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#FF9500",command=lambda:cal_app.operation("divide")).grid(row=4, column= 3, pady = 1)

mod_button = tk.Button(calc,text="%",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=lambda:cal_app.operation("mod")).grid(row=3, column= 6, pady = 1)

clear_button = tk.Button(calc,text="C",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.clear_function).grid(row=1, column=0, pady = 1)

all_clear_button = tk.Button(calc,text="CE",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.clear_all).grid(row=1, column= 1, pady = 1)

dot_button = tk.Button(calc,text=".",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#505050",command=lambda:cal_app.NumberPressed(".")).grid(row=5, column= 1, pady = 1)

zero_button = tk.Button(calc,text="0",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#505050",command=lambda:cal_app.NumberPressed(0)).grid(row=5, column= 0, pady = 1)

equal_button =  tk.Button(calc,text="=",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#FF9500",command=cal_app.sum_total).grid(row=5, column= 3, pady = 1)

PM_button = tk.Button(calc,text=chr(177),width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="white", bg="#505050",command=cal_app.PM_Pressed).grid(row=5, column=2, pady = 1)

root_button = tk.Button(calc,text="\u221A",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.squared).grid(row=1, column= 2, pady = 1)

sin_button =  tk.Button(calc,text="Sin",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.sinPressed).grid(row=1, column= 7, pady = 1)

cos_button =  tk.Button(calc,text="Cos",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.cosinePressed).grid(row=1, column= 5, pady = 1)

tan_button =  tk.Button(calc,text="Tan",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.tangentPressed).grid(row=1, column= 6, pady = 1)

asinh_button =  tk.Button(calc,text="asinh",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.inverseSinPressed).grid(row=5, column= 7, pady = 1)

acosh_button = tk.Button(calc,text="acosh",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.inverseCosinePressed).grid(row=5, column= 6, pady = 1)

exponents_button = tk.Button(calc,text="exp",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.exponents).grid(row=3, column= 5, pady = 1)

logarithm_button = tk.Button(calc,text="Log",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.logarithm).grid(row=3, column= 4, pady = 1)

pi_button = tk.Button(calc,text="π",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.pi).grid(row=1, column= 4, pady = 1)

SineH_button = tk.Button(calc,text="SineH",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.SineH).grid(row=2, column= 7, pady = 1)

CosineH_button = tk.Button(calc,text="cosH",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.CosineH).grid(row=2, column= 5, pady = 1)

TanH_button = tk.Button(calc,text="TanH",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.TangentH).grid(row=2, column= 6, pady = 1)

degree_button = tk.Button(calc,text="Deg",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.degrees).grid(row=5, column=5, pady = 1)

E_button = tk.Button(calc,text="E",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.E).grid(row=3, column= 7, pady = 1)

Pi2_button = tk.Button(calc,text="pi2",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.Pi_2).grid(row=2, column= 4, pady = 1)

log2_button = tk.Button(calc,text="log2",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.log_2).grid(row=5, column= 4, pady = 1)

log10_button = tk.Button(calc,text="Log10",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.log_10).grid(row=4, column= 4, pady = 1)

log1p_button = tk.Button(calc,text="Log1p",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.log1p).grid(row=4, column= 5, pady = 1)

expm1_button = tk.Button(calc,text="Expm1",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.expm1).grid(row=4, column= 6, pady = 1)

gamma_button = tk.Button(calc,text="Gamma",width=6,height= 2,font=("Lato",20,'bold'), bd=4, fg="black", bg="#D4D4D2",command=cal_app.gamma).grid(row=4, column= 7, pady = 1)



lblDisplay = tk.Label(calc, text = "Scientific Calculator",font=('Lato',30,'bold'),bg='black',fg='white',justify=tk.CENTER)
lblDisplay.grid(row=0, column= 4,columnspan=4)


# Graphing Calculator

#-----------------------------------------------------------------------------------------------------



menu_bar2 = tk.Menu(graphCal)
graphCal.config(menu=menu_bar2)

file_menu2 = tk.Menu(menu_bar2, tearoff=0)
menu_bar2.add_cascade(label="Mode", menu=file_menu2)
file_menu2.add_command(label = "Scientific Calculator", command =switch_to_scientific)

file_menu2.add_command(label="Exit", command=graphCal.quit)

# Create an "Options" menu
options_menu = tk.Menu(menu_bar2, tearoff=0)
menu_bar2.add_cascade(label="Options", menu=options_menu)

# Create a label for the instructions
instructions_label = tk.Label(graphCal, text="Enter a mathematical expression (e.g., x**2 + 3*x - 2)")
instructions_label.pack()

# Create an entry box for the function expression

# Create a keypad
keypad_frame = tk.Frame(graphCal)
keypad_frame.pack()

# Define the buttons for the keypad
graph_buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', 'Clear',
    'sin', 'cos',')'  # Add 'sin' and 'cos' buttons
]


for i, char in enumerate(graph_buttons):
    button = tk.Button(keypad_frame, text=char, width=5, command=lambda c=char: add_to_expression(c),font=('Helvetica', 14))
    button.grid(row=i // 4, column=i % 4)

    # Add padding to the Clear button
    if char == 'Clear':
        button.config(width=11)
        button.config(command=clear_expression)

# Create the 'X' button
x_button = tk.Button(keypad_frame, text='X', width=5, command=lambda: add_to_expression('x'))
x_button.grid(row=4, column=1)


# Create a button to plot the graph
plot_button = tk.Button(graphCal, text="Plot", command=plot_graph,font=('Helvetica', 14))
plot_button.pack()

#-------------------------------------------------------------------------------------------------------

def iExit():
  exit =  tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
  if exit>0:
    window.destroy()

menuBar  = tk.Menu(calc)

fileMenu = tk.Menu(menuBar,tearoff = 0)
menuBar.add_cascade(label = 'Mode', menu = fileMenu)
fileMenu.add_command(label = "Exit", command = iExit)
fileMenu.add_separator()
fileMenu.add_command(label = "Graphing Calculator", command =switch_to_graphing)


editMenu = tk.Menu(menuBar,tearoff = 0)
menuBar.add_cascade(label = 'Edit', menu = editMenu)
editMenu.add_command(label = "Cut")
editMenu.add_command(label = "Copy")
editMenu.add_separator()
editMenu.add_command(label = "Paste")

window.config(menu=menuBar)

graphCal.mainloop()
window.mainloop()