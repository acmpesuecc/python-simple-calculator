from tkinter import messagebox
import math

#adding power and returning value
def power(base, exponent):
    return(math.pow(base,exponent))

#returning values of basic trig functions
def trigfunctions(func, value):
     if func == "sin":
        return(math.sin(value))
    elif func == "cos":
        return(math.cos(value))
    elif func == "tan":
        return(math.tan(value))



