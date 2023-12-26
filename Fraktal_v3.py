import random
import turtle as t
from turtle import *
from PIL import Image, ImageGrab
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import colorchooser
import webbrowser



#Глобальные переменные 

global g 
global x1
global y1
global x2
global y2
global x3
global y3
global x4
global y4
global x5
global y5
global x6
global y6
global x7
global y7
global x8
global y8
global x9
global y9



pointx1 = 0
pointy1 = 0

pointx2 = 0
pointy2 = 0

pointx3 = 0
pointy3 = 0

pointx4 = 0
pointy4 = 0

pointx5 = 0
pointy5 = 0

pointx6 = 0
pointy6 = 0

pointx7 = 0
pointy7 = 0

pointx8 = 0
pointy8 = 0

pointx9 = 0
pointy9 = 0


#Tkinter окно
window = Tk()
window.title("Fraktal python")
window.geometry('1400x1024') 



#Создание меню и его второстипенных функций
def Window_width_and_length():
    pass

main_menu = Menu()
help_menu = Menu()
Info_menu = Menu()
option_menu = Menu()
option_WinSet_menu = Menu()


def GitHub():
    webbrowser.open_new('https://github.com/EgorSad06/Sierpinski-triangle')
    pass

def learn():
    webbrowser.open_new('https://ru.wikipedia.org/wiki/%D0%A4%D1%80%D0%B0%D0%BA%D1%82%D0%B0%D0%BB')




main_menu.add_checkbutton(label="Git hub", command=GitHub)
main_menu.add_cascade(label="Info", menu= Info_menu)
Info_menu.add_checkbutton(label="Learn about fracnal", command=learn)




#Правое меню настройки и создание фрактала
def peremen():
    global g
    g = Kol_vo_point.get()
    

text_right1 = Label(window, text="Настройка фрактала", font=("Arial Bold", 15)).grid(row=1, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)

text_right2 = Label(window, text="Количество стартовых точек", font=("Arial Bold", 10)).grid(row=2, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)
Kol_vo_point = StringVar()
Kol_vo_point_value = ("3", "4", "5" , "6")
KolVoPoint_combox = ttk.Combobox(textvariable=Kol_vo_point, values=Kol_vo_point_value, state="readonly").grid(row=7, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)




text_right4 = Label(window, text="Количество точек", font=("Arial Bold", 10)).grid(row=11, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)


point = IntVar(value=0)
points = IntVar()

def points_call_back():
    global points
    points = point.get() 
    print(points)
    
point = ttk.Spinbox(window, from_=1, to=2000000, command= points_call_back).grid(row=12, column=1)

text_point = Label(window, textvariable=point).grid(row=11, column=0)


def select_color_bg():
    result_bg = colorchooser.askcolor(initialcolor="black")
    canvas["bg"] = result_bg[1]
    text_color1["foreground"] = result_bg[1]
    text_color1["background"] = result_bg[1]
    
RGB_button = Button(window, text="Настройка фона поля", font=("Arial Bold", 10), command=select_color_bg).grid(row=13, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)
text_color1 = ttk.Label(window, text="----color----",
                        padding=8,
                    foreground= "#FFFFFF", 
                    background= "#FFFFFF")
text_color1.grid(row=14, column=1)


def select_color_point():
    result_poi = colorchooser.askcolor(initialcolor="black")
    Df_color = result_poi
    text_color2["foreground"] =  result_poi[1]
    text_color2["background"] =  result_poi[1]
    TurColor = result_poi[1]
    t.color(TurColor)
    
RGB_button = Button(window, text="Настройка цвета фрактала", font=("Arial Bold", 10), command=select_color_point).grid(row=15, column=1, ipadx=6, ipady=6, padx=[15, 4], pady=4)
text_color2 = ttk.Label(window, text="----color----",
                        padding=8,
                    foreground= "#FFFFFF", 
                    background= "#FFFFFF")
text_color2.grid(row=16, column=1)
    
  
  
#костыль
kolxoz = Label(window, text=" -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", font=("Arial Bold", 10))
kolxoz.grid(row=2, column=2, ipadx=6, ipady=6, padx=[15, 4], pady=4, sticky= NS)



#Левое меню настройки и создание фрактала и КОНЧЕНОЕ решение  
    
text_left1 = Label(window, text="Настройка стартовых точек", font=("Arial Bold", 15)).grid(row=1, column=3, ipadx=6, ipady=6, padx=[15, 4], pady=4, sticky=E)



# создание стартовых точек в новом окне

def save_cord_start_point():
    click_en1x = StringVar()
    print(click_en1x.get())
    h = click_en1x.get()
    print(h)

pass



def click():
    root = Tk()
    root.title("настройка стартовых точек")
    root.geometry("800x800")
    peremen()
    close_button = ttk.Button(root, text="сохранить и выйти", command=lambda: root.destroy()).grid(row=0, column=0,ipadx=6, ipady=6, padx=[15, 4], pady=4)
    


    if g == "3":
        global pointx1
        global pointy1

        global pointx2
        global pointy2
        
        global pointx3
        global pointy3

        
        click_en1_text1 = Label(root, text = "координаты 1 точки").grid(row=1, column = 1, columnspan = 2)


        def change_x1(newVal):
            global int_value_x1
            float_value = float(newVal)     
            int_value_x1 = round(float_value)  

        x1 = IntVar(value=0)
        click_x1_text = Label(root, textvariable=x1).grid(row=2, column=0)
        click_x1_sca = StringVar()
        click_x1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x1, command= change_x1).grid(row=2, column=1)
        
        
        def change_y1(newVal):
            global int_value_y1
            float_value = float(newVal)     
            int_value_y1 = round(float_value)  
    
        y1 = IntVar()
        click_y1_text = Label(root, textvariable=y1).grid(row=3, column=0)
        click_y1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y1, command= change_y1).grid(row=3, column=1)
     
        
        def change_x2(newVal):
            global int_value_x2
            float_value = float(newVal)     
            int_value_x2 = round(float_value)  

        click_en2_text = Label(root, text = "координаты 2 точки").grid(row=4, column = 1, columnspan = 2)
        x2 = IntVar(value=0)
        click_x2_text = Label(root, textvariable=x2).grid(row=5, column=0)
        click_x2_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x2, command= change_x2).grid(row=5, column=1)

       
        def change_y2(newVal):
            global int_value_y2
            float_value = float(newVal)     
            int_value_y2 = round(float_value)  

        y2 = IntVar()
        click_y2_text = Label(root, textvariable=y2).grid(row=6, column=0)
        click_y2_sca = ttk.Scale(root,orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y2, command= change_y2).grid(row=6, column=1)

      

        def change_x3(newVal):
            global int_value_x3
            float_value = float(newVal)     
            int_value_x3 = round(float_value)  

        click_en3_text3 = Label(root, text = "координаты 3 точки").grid(row=7, column = 1, columnspan = 2)
        x3 = IntVar(value=0)
        click_x3_text = Label(root, textvariable=x3).grid(row=8, column=0)
        click_x3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x3, command= change_x3).grid(row=8, column=1)


        def change_y3(newVal):
            global int_value_y3
            float_value = float(newVal)     
            int_value_y3 = round(float_value)  

        y3 = IntVar(value=0)
        click_y3_text = Label(root, textvariable=y3).grid(row=9, column=0)
        click_y3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y3, command= change_y3).grid(row=9, column=1)

        
        root.mainloop()
        pass
    if g == "4":
        
        global pointx1
        global pointy1

        global pointx2
        global pointy2
        
        global pointx3
        global pointy3

        global pointx4
        global pointy4

        click_en1_text1 = Label(root, text = "координаты 1 точки").grid(row=1, column = 1, columnspan = 2)


        def change_x1(newVal):
            global int_value_x1
            float_value = float(newVal)     
            int_value_x1 = round(float_value)  

        x1 = IntVar(value=0)
        click_x1_text = Label(root, textvariable=x1).grid(row=2, column=0)
        click_x1_sca = StringVar()
        click_x1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x1, command= change_x1).grid(row=2, column=1)
        
        
        def change_y1(newVal):
            global int_value_y1
            float_value = float(newVal)     
            int_value_y1 = round(float_value)  
    
        y1 = IntVar()
        click_y1_text = Label(root, textvariable=y1).grid(row=3, column=0)
        click_y1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y1, command= change_y1).grid(row=3, column=1)
     
        
        def change_x2(newVal):
            global int_value_x2
            float_value = float(newVal)     
            int_value_x2 = round(float_value)  

        click_en2_text = Label(root, text = "координаты 2 точки").grid(row=4, column = 1, columnspan = 2)
        x2 = IntVar(value=0)
        click_x2_text = Label(root, textvariable=x2).grid(row=5, column=0)
        click_x2_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x2, command= change_x2).grid(row=5, column=1)

       
        def change_y2(newVal):
            global int_value_y2
            float_value = float(newVal)     
            int_value_y2 = round(float_value)  

        y2 = IntVar()
        click_y2_text = Label(root, textvariable=y2).grid(row=6, column=0)
        click_y2_sca = ttk.Scale(root,orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y2, command= change_y2).grid(row=6, column=1)

      

        def change_x3(newVal):
            global int_value_x3
            float_value = float(newVal)     
            int_value_x3 = round(float_value)  

        click_en3_text3 = Label(root, text = "координаты 3 точки").grid(row=7, column = 1, columnspan = 2)
        x3 = IntVar(value=0)
        click_x3_text = Label(root, textvariable=x3).grid(row=8, column=0)
        click_x3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x3, command= change_x3).grid(row=8, column=1)


        def change_y3(newVal):
            global int_value_y3
            float_value = float(newVal)     
            int_value_y3 = round(float_value)  

        y3 = IntVar(value=0)
        click_y3_text = Label(root, textvariable=y3).grid(row=9, column=0)
        click_y3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y3, command= change_y3).grid(row=9, column=1)


        def change_x4(newVal):
            global int_value_x4
            float_value = float(newVal)     
            int_value_x4 = round(float_value)  


        click_en4_text4 = Label(root, text = "координаты 4 точки").grid(row=10, column = 1, columnspan = 2)
        x4 = IntVar(value=0)
        click_x4_text = Label(root, textvariable=x4).grid(row=11, column=0)
        click_x4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x4, command=change_x4).grid(row=11, column=1)


        def change_y4(newVal):
            global int_value_y4
            float_value = float(newVal)     
            int_value_y4 = round(float_value)  

        y4 = IntVar(value=0)
        click_y4_text = Label(root, textvariable=y4).grid(row=12, column=0)
        click_y4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y4, command= change_y4).grid(row=12, column=1)
        root.mainloop()
        pass
    if g == "5":
        
        global pointx1
        global pointy1

        global pointx2
        global pointy2
        
        global pointx3
        global pointy3

        global pointx4
        global pointy4

        global pointx5
        global pointy5

        click_en1_text1 = Label(root, text = "координаты 1 точки").grid(row=1, column = 1, columnspan = 2)


        def change_x1(newVal):
            global int_value_x1
            float_value = float(newVal)     
            int_value_x1 = round(float_value)  

        x1 = IntVar(value=0)
        click_x1_text = Label(root, textvariable=x1).grid(row=2, column=0)
        click_x1_sca = StringVar()
        click_x1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x1, command= change_x1).grid(row=2, column=1)
        
        
        def change_y1(newVal):
            global int_value_y1
            float_value = float(newVal)     
            int_value_y1 = round(float_value)  
    
        y1 = IntVar()
        click_y1_text = Label(root, textvariable=y1).grid(row=3, column=0)
        click_y1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y1, command= change_y1).grid(row=3, column=1)
     
        
        def change_x2(newVal):
            global int_value_x2
            float_value = float(newVal)     
            int_value_x2 = round(float_value)  

        click_en2_text = Label(root, text = "координаты 2 точки").grid(row=4, column = 1, columnspan = 2)
        x2 = IntVar(value=0)
        click_x2_text = Label(root, textvariable=x2).grid(row=5, column=0)
        click_x2_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x2, command= change_x2).grid(row=5, column=1)

       
        def change_y2(newVal):
            global int_value_y2
            float_value = float(newVal)     
            int_value_y2 = round(float_value)  

        y2 = IntVar()
        click_y2_text = Label(root, textvariable=y2).grid(row=6, column=0)
        click_y2_sca = ttk.Scale(root,orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y2, command= change_y2).grid(row=6, column=1)

      

        def change_x3(newVal):
            global int_value_x3
            float_value = float(newVal)     
            int_value_x3 = round(float_value)  

        click_en3_text3 = Label(root, text = "координаты 3 точки").grid(row=7, column = 1, columnspan = 2)
        x3 = IntVar(value=0)
        click_x3_text = Label(root, textvariable=x3).grid(row=8, column=0)
        click_x3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x3, command= change_x3).grid(row=8, column=1)


        def change_y3(newVal):
            global int_value_y3
            float_value = float(newVal)     
            int_value_y3 = round(float_value)  

        y3 = IntVar(value=0)
        click_y3_text = Label(root, textvariable=y3).grid(row=9, column=0)
        click_y3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y3, command= change_y3).grid(row=9, column=1)


        def change_x4(newVal):
            global int_value_x4
            float_value = float(newVal)     
            int_value_x4 = round(float_value)  


        click_en4_text4 = Label(root, text = "координаты 4 точки").grid(row=10, column = 1, columnspan = 2)
        x4 = IntVar(value=0)
        click_x4_text = Label(root, textvariable=x4).grid(row=11, column=0)
        click_x4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x4, command=change_x4).grid(row=11, column=1)


        def change_y4(newVal):
            global int_value_y4
            float_value = float(newVal)     
            int_value_y4 = round(float_value)  

        y4 = IntVar(value=0)
        click_y4_text = Label(root, textvariable=y4).grid(row=12, column=0)
        click_y4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y4, command= change_y4).grid(row=12, column=1)


        def change_x5(newVal):
            global int_value_x5
            float_value = float(newVal)     
            int_value_x5 = round(float_value) 

        click_en4_text4 = Label(root, text = "координаты 5 точки").grid(row=13, column = 1, columnspan = 2)
        x5 = IntVar(value=0)
        click_x5_text = Label(root, textvariable=x5).grid(row=14, column=0)
        click_x5_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x5, command=change_x5).grid(row=14, column=1)



        def change_y5(newVal):
            global int_value_y5
            float_value = float(newVal)     
            int_value_y5 = round(float_value) 

        y5 = IntVar(value=0)
        click_y5_text = Label(root, textvariable=y5).grid(row=15, column=0)
        click_y5_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y5, command=change_y5).grid(row=15, column=1)
        root.mainloop()
        pass
    if g == "6":
        
        global pointx1
        global pointy1

        global pointx2
        global pointy2
        
        global pointx3
        global pointy3

        global pointx4
        global pointy4

        global pointx5
        global pointy5

        global pointx6
        global pointy6

        click_en1_text1 = Label(root, text = "координаты 1 точки").grid(row=1, column = 1, columnspan = 2)


        def change_x1(newVal):
            global int_value_x1
            float_value = float(newVal)     
            int_value_x1 = round(float_value)  

        x1 = IntVar(value=0)
        click_x1_text = Label(root, textvariable=x1).grid(row=2, column=0)
        click_x1_sca = StringVar()
        click_x1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x1, command= change_x1).grid(row=2, column=1)
        
        
        def change_y1(newVal):
            global int_value_y1
            float_value = float(newVal)     
            int_value_y1 = round(float_value)  
    
        y1 = IntVar()
        click_y1_text = Label(root, textvariable=y1).grid(row=3, column=0)
        click_y1_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y1, command= change_y1).grid(row=3, column=1)
     
        
        def change_x2(newVal):
            global int_value_x2
            float_value = float(newVal)     
            int_value_x2 = round(float_value)  

        click_en2_text = Label(root, text = "координаты 2 точки").grid(row=4, column = 1, columnspan = 2)
        x2 = IntVar(value=0)
        click_x2_text = Label(root, textvariable=x2).grid(row=5, column=0)
        click_x2_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable= x2, command= change_x2).grid(row=5, column=1)

       
        def change_y2(newVal):
            global int_value_y2
            float_value = float(newVal)     
            int_value_y2 = round(float_value)  

        y2 = IntVar()
        click_y2_text = Label(root, textvariable=y2).grid(row=6, column=0)
        click_y2_sca = ttk.Scale(root,orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y2, command= change_y2).grid(row=6, column=1)

      

        def change_x3(newVal):
            global int_value_x3
            float_value = float(newVal)     
            int_value_x3 = round(float_value)  

        click_en3_text3 = Label(root, text = "координаты 3 точки").grid(row=7, column = 1, columnspan = 2)
        x3 = IntVar(value=0)
        click_x3_text = Label(root, textvariable=x3).grid(row=8, column=0)
        click_x3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x3, command= change_x3).grid(row=8, column=1)


        def change_y3(newVal):
            global int_value_y3
            float_value = float(newVal)     
            int_value_y3 = round(float_value)  

        y3 = IntVar(value=0)
        click_y3_text = Label(root, textvariable=y3).grid(row=9, column=0)
        click_y3_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y3, command= change_y3).grid(row=9, column=1)


        def change_x4(newVal):
            global int_value_x4
            float_value = float(newVal)     
            int_value_x4 = round(float_value)  


        click_en4_text4 = Label(root, text = "координаты 4 точки").grid(row=10, column = 1, columnspan = 2)
        x4 = IntVar(value=0)
        click_x4_text = Label(root, textvariable=x4).grid(row=11, column=0)
        click_x4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x4, command=change_x4).grid(row=11, column=1)


        def change_y4(newVal):
            global int_value_y4
            float_value = float(newVal)     
            int_value_y4 = round(float_value)  

        y4 = IntVar(value=0)
        click_y4_text = Label(root, textvariable=y4).grid(row=12, column=0)
        click_y4_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y4, command= change_y4).grid(row=12, column=1)


        def change_x5(newVal):
            global int_value_x5
            float_value = float(newVal)     
            int_value_x5 = round(float_value) 

        click_en4_text4 = Label(root, text = "координаты 5 точки").grid(row=13, column = 1, columnspan = 2)
        x5 = IntVar(value=0)
        click_x5_text = Label(root, textvariable=x5).grid(row=14, column=0)
        click_x5_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x5, command=change_x5).grid(row=14, column=1)



        def change_y5(newVal):
            global int_value_y5
            float_value = float(newVal)     
            int_value_y5 = round(float_value) 

        y5 = IntVar(value=0)
        click_y5_text = Label(root, textvariable=y5).grid(row=15, column=0)
        click_y5_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y5, command=change_y5).grid(row=15, column=1)
    
        click_en6_text6 = Label(root, text = "координаты 6 точки").grid(row=16, column = 1, columnspan = 2)


        def change_x6(newVal):
            global int_value_x6
            float_value = float(newVal)     
            int_value_x6 = round(float_value) 
        
        x6 = IntVar(value=0)
        click_x6_text = Label(root, textvariable=x6).grid(row=17, column=0)
        click_x6_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=x6, command= change_x6).grid(row=17, column=1)

        def change_y6(newVal):
            global int_value_y6
            float_value = float(newVal)     
            int_value_y6 = round(float_value) 

        y6 = IntVar(value=0)
        click_y6_text = Label(root, textvariable=y6).grid(row=18, column=0)
        click_y6_sca = ttk.Scale(root, orient=HORIZONTAL, length=200, from_=-200.0, to=200.0, value=30, variable=y6, command=change_y6).grid(row=18, column=1)
        root.mainloop()
        pass


    global pointx1
    global pointy1

    global pointx2
    global pointy2
    
    global pointx3
    global pointy3
    
    global pointx4
    global pointy4
    
    global pointx5
    global pointy5
    
    global pointx6
    global pointy6
    
    global pointx7
    global pointy7
    
    global pointx8
    global pointy8
    
    global pointx9
    global pointy9
    


left_button1 = Button(window, text="Настройка координат точек", font=("Arial Bold", 10), command=click).grid(row=2, column=3, ipadx=6, ipady=6, padx=[15, 4], pady=4)


    
#canvas


canvas = Canvas(bg="white", width=800, height=800)
canvas.place(x=640, y=256, anchor="center")
t = RawTurtle(canvas)
t.pensize(5)
Df_color = "black"
t.color(Df_color)



def start():
    if g == "3":
        g3()
    if g == "4":
        g4()
    if g == "5":
        g5()
    if g == "6":
        g6()
#ускорить работу точек


def g3():

    t.speed(10)
    x = 0
    t.penup()
    t.goto(int_value_x1, int_value_x1)
    t.dot()

    t.goto(int_value_x2, int_value_y2)
    t.dot()

    t.goto(int_value_x3, int_value_y3)
    t.dot()
    t.goto(0,0)

    while x != points:
        r1 = 1
        r6 = 5
        kosta = random.randint(r1, r6)
        if kosta == 1:
            corX = t.xcor()
            corY = t.ycor()
            x12 = (int_value_x1 + corX)/2
            y12 = (int_value_y1 + corY)/2
            t.setx(x12)
            t.sety(y12)
            t.dot()
            x += 1
        if kosta == 3:
            corX = t.xcor()
            corY = t.ycor()
            x34 = (int_value_x2 + corX)/2
            y34 = (int_value_y2 + corY)/2
            t.setx(x34)
            t.sety(y34)
            t.dot()
            x += 1
        if kosta == 5:
            corX = t.xcor()
            corY = t.ycor()
            x56 = (int_value_x3 + corX)/2
            y56 = (int_value_y3 + corY)/2
            t.setx(x56)
            t.sety(y56)
            t.dot()
            x += 1
        if x == points:
            t.goto(0,0)
            int=input()
	     
    pass

def g4():
    t.speed(10)
    x = 0
    t.penup()
    t.goto(int_value_x1, int_value_x1)
    t.dot()

    t.goto(int_value_x2, int_value_y2)
    t.dot()

    t.goto(int_value_x3, int_value_y3)
    t.dot()
        
    t.goto(int_value_x4, int_value_y4)
    t.dot()
    t.goto(0,0)

    r1 = 1
    r6 = 5
    while x != points:
        kosta = random.randint(r1, r6)
        if kosta == 1:
            corX = t.xcor()
            corY = t.ycor()
            x1 = (int_value_x1 + corX)/3
            y1 = (int_value_y1 + corY)/3
            t.setx(x1)
            t.sety(y1)
            t.dot()
            x += 1
        if kosta == 2:
            corX = t.xcor()
            corY = t.ycor()
            x2 = (int_value_x2 + corX)/3
            y2 = (int_value_y2 + corY)/3
            t.setx(x2)
            t.sety(y2)
            t.dot()
            x += 1
        if kosta == 3:
            corX = t.xcor()
            corY = t.ycor()
            x3 = (int_value_x3 + corX)/3
            y3 = (int_value_y3 + corY)/3
            t.setx(x3)
            t.sety(y3)
            t.dot()
            x += 1
        if kosta == 4:
            corX = t.xcor()
            corY = t.ycor()
            x4 = (int_value_x4 + corX)/3
            y4 = (int_value_y4 + corY)/3
            t.setx(x4)
            t.sety(y4)
            t.dot()
            x += 1
        if x == points:
            t.goto(0,0)
            int=input()

    pass

def g5():
    t.speed(10)
    x = 0
    t.penup()
    t.goto(int_value_x1, int_value_x1)
    t.dot()

    t.goto(int_value_x2, int_value_y2)
    t.dot()

    t.goto(int_value_x3, int_value_y3)
    t.dot()
        
    t.goto(int_value_x4, int_value_y4)
    t.dot()

    t.goto(int_value_x5, int_value_y5)
    t.dot()

    t.goto(0,0)

    r1 = 1
    r6 = 5
    while x != points:
        kosta = random.randint(r1, r6)
        if kosta == 1:
            corX = t.xcor()
            corY = t.ycor()
            x1 = (int_value_x1 + corX)/4
            y1 = (int_value_y1 + corY)/4
            t.setx(x1)
            t.sety(y1)
            t.dot()
            x += 1
        if kosta == 2:
            corX = t.xcor()
            corY = t.ycor()
            x2 = (int_value_x2 + corX)/4
            y2 = (int_value_y2 + corY)/4
            t.setx(x2)
            t.sety(y2)
            t.dot()
            x += 1
        if kosta == 3:
            corX = t.xcor()
            corY = t.ycor()
            x3 = (int_value_x3 + corX)/4
            y3 = (int_value_y3 + corY)/4
            t.setx(x3)
            t.sety(y3)
            t.dot()
            x += 1
        if kosta == 4:
            corX = t.xcor()
            corY = t.ycor()
            x4 = (int_value_x4 + corX)/4
            y4 = (int_value_y4 + corY)/4
            t.setx(x4)
            t.sety(y4)
            t.dot()
            x += 1
        if kosta == 5:
            corX = t.xcor()
            corY = t.ycor()
            x5 = (int_value_x5 + corX)/4
            y5 = (int_value_y5 + corY)/4
            t.setx(x5)
            t.sety(y5)
            t.dot()
            x += 1

        if x == points:
            t.goto(0,0)
            int=input()    


def g6():
    t.speed(10)
    x = 0
    t.penup()
    t.goto(int_value_x1, int_value_x1)
    t.dot()

    t.goto(int_value_x2, int_value_y2)
    t.dot()

    t.goto(int_value_x3, int_value_y3)
    t.dot()
        
    t.goto(int_value_x4, int_value_y4)
    t.dot()

    t.goto(int_value_x5, int_value_y5)
    t.dot()

    t.goto(int_value_x6, int_value_y6)
    t.dot()

    t.goto(0,0)

    r1 = 1
    r6 = 5
    while x != points:
        kosta = random.randint(r1, r6)
        if kosta == 1:
            corX = t.xcor()
            corY = t.ycor()
            x1 = (int_value_x1 + corX)/5
            y1 = (int_value_y1 + corY)/5
            t.setx(x1)
            t.sety(y1)
            t.dot()
            x += 1
        if kosta == 2:
            corX = t.xcor()
            corY = t.ycor()
            x2 = (int_value_x2 + corX)/5
            y2 = (int_value_y2 + corY)/5
            t.setx(x2)
            t.sety(y2)
            t.dot()
            x += 1
        if kosta == 3:
            corX = t.xcor()
            corY = t.ycor()
            x3 = (int_value_x3 + corX)/5
            y3 = (int_value_y3 + corY)/5
            t.setx(x3)
            t.sety(y3)
            t.dot()
            x += 1
        if kosta == 4:
            corX = t.xcor()
            corY = t.ycor()
            x4 = (int_value_x4 + corX)/5
            y4 = (int_value_y4 + corY)/5
            t.setx(x4)
            t.sety(y4)
            t.dot()
            x += 1
        if kosta == 5:
            corX = t.xcor()
            corY = t.ycor()
            x5 = (int_value_x5 + corX)/5
            y5 = (int_value_y5 + corY)/5
            t.setx(x5)
            t.sety(y5)
            t.dot()
            x += 1

        if x == points:
            t.goto(0,0)
            int=input()        

main_menu.add_checkbutton(label="Start", command=start)

 
window.config(menu=main_menu)
window.mainloop()
