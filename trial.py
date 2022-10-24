
# importing all the libraries we are making use of (tkinter and custom MyMath module
#PES2UG21CS088
#ARCHIT ANAND
#COLORING

# importing all the libraries we are making use of (tkfloater and custom MyMath module


from tkinter import *

from turtle import onclick
from turtle import color

from MyMath import *
from tkinter import ttk
from tkinter import messagebox

# creating basic root window
root = Tk()
root.title('MyMath')
root.geometry("500x500")

# defining area function


def destroyforcircle():
    height.forget()
    height_entry.forget()

def area():

    SelectedShape = shapes.get()

    if SelectedShape == "Rectangle":
        l = float(radius_entry.get())
        b = float(height_entry.get())
        area_rectangle = myArea(SelectedShape.lower(), l, b, 0, 0)
        messagebox.showinfo("Area Rectangle", area_rectangle)

    elif SelectedShape == "Square":
        r = float(radius_entry.get())
        area_square = myArea(SelectedShape.lower(), r, 0, 0, 0)
        messagebox.showinfo("Area Square", area_square)

    elif SelectedShape == "Triangle":
        b = float(radius_entry.get())
        h = float(height_entry.get())
        area_triangle = myArea(SelectedShape.lower(), 0, b, h, 0)
        messagebox.showinfo("Area Triangle", area_triangle)

    elif SelectedShape == "Circle":
        destroyforcircle()
        r = float(radius_entry.get())
        area_circle = myArea(SelectedShape.lower(), 0, 0, 0, r)
        messagebox.showinfo("Area Circle", area_circle)
        
    else:
        messagebox.showwarning("Invalid Input", "shape is not available")

# defining volume function


def volume():
    selected_solid_shape = solidshape.get()
    if selected_solid_shape == "Sphere":
        r = float(radius_entry2.get())
        vol_sphere = myvolume(selected_solid_shape.lower(), 0, 0, 0, r)
        messagebox.showinfo("Volume Sphere", vol_sphere)
    elif selected_solid_shape == "Cone":
        r = float(radius_entry2.get())
        h = float(height2.get())
        vol_cone = myvolume(selected_solid_shape.lower(), 0, 0, h, r)
        messagebox.showinfo("Volume Cone", vol_cone)

    elif selected_solid_shape == "Cube":
        l = float(radius_entry2.get())
        vol_cube = myvolume(selected_solid_shape.lower(), l, 0, 0, 0)
        messagebox.showinfo("Volume Cube", vol_cube)
    elif selected_solid_shape == "Cylinder":
        r = float(radius_entry2.get())
        h = float(height2.get())
        vol_cylinder = myvolume(selected_solid_shape.lower(), 0, 0, h, r)
        messagebox.showinfo("Volume Cylinder", vol_cylinder)

    elif selected_solid_shape == "Cuboid":
        l = float(radius_entry2.get())
        b = float(width_entry.get())
        h = float(height2.get())
        vol_cuboid = myvolume(selected_solid_shape.lower(), l, b, h, 0)
        messagebox.showinfo("Volume Cuboid", vol_cuboid)

    else:
        messagebox.showwarning("Invalid input", "shape is not available")


# defining condition_check function

def condition_check():
    tocheck = conditions.get()
    if tocheck == "Pythagorean Triplet Checker":
        a = float(side1_entry.get())
        b = float(side2_entry.get())
        c = float(side3_entry.get())
        py_check = mycondition(tocheck, a, b, c, 0)
        if py_check == 1:
            messagebox.showinfo("Check", "This is a Pythagorean Triplet.")
        else:
            messagebox.showinfo("Check", "This is not a Pythagorean Triplet.")

    elif tocheck == "Complimentary&Supplementary Angles":
        angle = float(angle_entry.get())
        comsup = mycondition(tocheck, 0, 0, 0, angle)


def power1():
    p = float(power_entry.get())
    b = float(base_entry.get())
    power_of= mypower(p,b)
    messagebox.showinfo("power", power_of)

def log():
    v = float(value_entry.get())
    b = float(base_entry.get())
    log_of= mylog(v,b)
    messagebox.showinfo("log", log_of)

def fac():
    v = int(number_entry.get())
    fac_of= myfact(v)
    messagebox.showinfo("factorial", fac_of)


def surarea():

    SelectedShape1 = surface.get()

    if SelectedShape1 == "cuboid":
        r = float(radius_entry1.get())
        l = float(height_entry1.get())
        b = float(height_entry2.get())
        h = float(height_entry3.get())
        area_rectangle1 = mysurArea(SelectedShape1.lower(), l, b, h,0)
        messagebox.showinfo("surface Area of a Rectangle", area_rectangle1)

    elif SelectedShape1 == "cube":
        l = float(height_entry1.get())
        area_square1 = mysurArea(SelectedShape1.lower(), l, 0, 0, 0)
        messagebox.showinfo("surface Area of a Square", area_square1)

    elif SelectedShape1 == "sphere":
        r = float(radius_entry1.get())
        area_circle1 = mysurArea(SelectedShape1.lower(), 0, 0, 0, r)
        messagebox.showinfo("surface Area of a Circle", area_circle1)
    


# creating tabs
note1 = ttk.Notebook(root)
note1.pack(pady=5)

# creating 3 frames
area_frame = Frame(note1, width=300, height=300 , )
volume_frame = Frame(note1, width=300, height=300)
condition_frame = Frame(note1, width=300, height=300)
power_frame = Frame(note1, width=300, height=300)
sur_frame = Frame(note1, width=300, height=300)
log_frame = Frame(note1, width=300, height=300)
fac_frame = Frame(note1, width=300, height=300)


area_frame.pack(fill="both", expand=1)
volume_frame.pack(fill="both", expand=1)
condition_frame.pack(fill="both", expand=1)
power_frame.pack(fill="both", expand=1)
sur_frame.pack(fill="both", expand=1)
log_frame.pack(fill="both", expand=1)
fac_frame.pack(fill="both", expand=1)

# adding tabs
note1.add(area_frame, text="Area Calculator")
note1.add(volume_frame, text="Volume Calculator")
note1.add(condition_frame, text="Condition Checker")
note1.add(power_frame, text="Power")
note1.add(sur_frame, text="Surface area 3-D")
note1.add(log_frame, text="logarithm")
note1.add(fac_frame, text="factorial")

# defining shapes and show
shapes = StringVar()
shapes.set("Select")
solidshape = StringVar()
solidshape.set("Select")
conditions = StringVar()
conditions.set("Select")
surface = StringVar()
surface.set("Select")



def show1():
    mylabel = Label(area_frame, text=shapes.get()).pack()


def show2():
    mylabel2 = Label(volume_frame, text=solidshape.get()).pack()


def show3():
    mylabel3 = Label(condition_frame, text=conditions.get()).pack()

def show4():
    mylabel4 = Label(sur_frame, text=surface.get()).pack()




# area frame option
power_side = Label(area_frame, text="Select Shape").pack()
shape_options = OptionMenu(
    area_frame, shapes, "Circle", "Square", "Triangle", "Rectangle").pack()


mybutton1 = Button(area_frame, text="Select shape", command=area)
mybutton1.pack()


mybutton1 = Button(area_frame, text="Select shape", command=show1,bg="orange").pack()







radius_side = Label(area_frame, text="Enter radius or side in m")
radius_side.pack()

radius_entry = Entry(area_frame, font=("Helvetica", 20),bg="grey")
radius_entry.pack()


height = Label(area_frame, text="Enter height or width in m if applicable else enter 0")
height.pack()
height_entry = Entry(area_frame, font=("Helvetica", 20))

height_entry.pack()


height_entry.pack()


# volume frame option
power_side = Label(volume_frame, text="Select Shape").pack()
volume_options = OptionMenu(
    volume_frame, solidshape, "Cone", "Sphere", "Cylinder", "Cube", "Cuboid").pack()

radius_side2 = Label(volume_frame, text="Enter radius or side in m").pack()
radius_entry2 = Entry(volume_frame, font=("Helvetica", 20),bg="green")
radius_entry2.pack()
height2 = Label(
    volume_frame, text="Enter height in m if applicable else enter 0").pack()
height2 = Entry(volume_frame, font=("Helvetica", 20),bg="red")
height2.pack()
width = Label(
    volume_frame, text="Enter breadth in m if applicable else enter 0").pack()
width_entry = Entry(volume_frame, font=("Helvetica", 20),bg="blue")
width_entry.pack()

# condition frame
power_side = Label(condition_frame, text="Select Condition").pack()
condition_options = OptionMenu(condition_frame, conditions,
                               "Pythagorean Triplet Checker", "Complimentary&Supplementary Angles").pack()

side1_label = Label(condition_frame, text="Enter first number").pack()
side1_entry = Entry(condition_frame, font=("Helvetica", 20),bg="blue")
side1_entry.pack()
side2_label = Label(condition_frame, text="Enter second number").pack()
side2_entry = Entry(condition_frame, font=("Helvetica", 20),bg="green")
side2_entry.pack()
side3_label = Label(condition_frame, text="Enter third number").pack()
side3_entry = Entry(condition_frame, font=("Helvetica", 20),bg="red")
side3_entry.pack()
angle_label = Label(condition_frame, text="Enter angle in degrees").pack()
angle_entry = Entry(condition_frame, font=("Helvetica", 20),bg="blue")
angle_entry.pack()

# power
power_side = Label(power_frame, text="Enter power").pack()
power_entry = Entry(power_frame, font=("Helvetica", 20))
power_entry.pack()

base = Label(
    power_frame, text="base").pack()
base_entry = Entry(power_frame, font=("Helvetica", 20))
base_entry.pack()

# surface area frame option
power_side = Label(sur_frame, text="Select Shape").pack()
shape_options = OptionMenu(
    sur_frame, surface, "sphere", "cuboid", "cube").pack()

radius_side = Label(sur_frame, text="Enter radius").pack()

radius_entry1 = Entry(sur_frame, font=("Helvetica", 20))
radius_entry1.pack()

length = Label(
    sur_frame, text="Enter length").pack()
height_entry1 = Entry(sur_frame, font=("Helvetica", 20))
height_entry1.pack()

breadth = Label(
    sur_frame, text="Enter breadth").pack()
height_entry2 = Entry(sur_frame, font=("Helvetica", 20))
height_entry2.pack()

height = Label(
    sur_frame, text="Enter height").pack()
height_entry3 = Entry(sur_frame, font=("Helvetica", 20))
height_entry3.pack()

#logarithm
power_side1 = Label(log_frame, text="Enter x\n log(x)").pack()
value_entry = Entry(log_frame, font=("Helvetica", 20))
value_entry.pack()

base1 = Label(
    log_frame, text="base").pack()
base_entry = Entry(log_frame, font=("Helvetica", 20))
base_entry.pack()

#factorial
number_side = Label(fac_frame, text="Enter number").pack()
number_entry = Entry(fac_frame, font=("Helvetica", 20))
number_entry.pack()


# button frame
button_frame1 = Frame(area_frame)
button_frame1.pack()
button_frame2 = Frame(volume_frame)
button_frame2.pack()
button_frame3 = Frame(condition_frame)
button_frame3.pack()
button_frame4 = Frame(power_frame)
button_frame4.pack()
button_frame5 = Frame(sur_frame)
button_frame5.pack()
button_frame6 = Frame(log_frame)
button_frame6.pack()
button_frame7 = Frame(fac_frame)
button_frame7.pack()

# creating buttons

button1 = Button(button_frame1, text="Calculate", command=area,bg="grey")
button1.grid(row=0, column=0, padx=10)
button2 = Button(button_frame2, text="Calculate", command=volume,bg="orange")
button2.grid(row=0, column=0, padx=10)
button3 = Button(button_frame3, text="Calculate", command=condition_check,bg="blue")

button3.grid(row=0, column=0, padx=10)
button4 = Button(button_frame4, text="Calculate", command=power1)
button4.grid(row=0, column=0, padx=10)
button5 = Button(button_frame5, text="Calculate", command=surarea)
button5.grid(row=0, column=0, padx=10)
button6 = Button(button_frame6, text="Calculate", command=log)
button6.grid(row=0, column=0, padx=10)
button7 = Button(button_frame7, text="Calculate", command=fac)
button7.grid(row=0, column=0, padx=10)

root.mainloop()