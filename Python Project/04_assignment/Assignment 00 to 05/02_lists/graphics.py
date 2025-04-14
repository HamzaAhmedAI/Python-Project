import tkinter
import time

class Canvas:
    def __init__(self, width, height):
        self.__root = tkinter.Tk()
        self.__width = width
        self.__height = height
        self.__canvas = tkinter.Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__mouse_x = 0
        self.__mouse_y = 0
        self.__last_click_x = 0
        self.__last_click_y = 0
        
        def mouse_moved(event):
            self.__mouse_x = event.x
            self.__mouse_y = event.y
        self.__canvas.bind('<Motion>', mouse_moved)
        
        def mouse_clicked(event):
            self.__last_click_x = event.x
            self.__last_click_y = event.y
        self.__canvas.bind('<Button-1>', mouse_clicked)
        
        self.__root.update()
    
    def create_rectangle(self, left_x, top_y, right_x, bottom_y, color):
        return self.__canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill=color)
    
    def set_color(self, item, color):
        self.__canvas.itemconfig(item, fill=color)
    
    def moveto(self, item, x, y):
        self.__canvas.coords(item, x, y, x + 20, y + 20)
    
    def find_overlapping(self, left_x, top_y, right_x, bottom_y):
        return self.__canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    def get_mouse_x(self):
        return self.__mouse_x
    
    def get_mouse_y(self):
        return self.__mouse_y
    
    def get_last_click(self):
        return (self.__last_click_x, self.__last_click_y)
    
    def wait_for_click(self):
        while self.__last_click_x == 0 and self.__last_click_y == 0:
            self.__root.update()
            time.sleep(0.05)
        
        click = (self.__last_click_x, self.__last_click_y)
        self.__last_click_x = 0
        self.__last_click_y = 0
        return click