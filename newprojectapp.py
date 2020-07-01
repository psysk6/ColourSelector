import tkinter as tk
import tkinter.ttk as ttk
from clickHandler import *

from pynput import *
from PIL import ImageGrab
from PIL import ImageColor

debugging = True


def get_pixel_colour(i_x, i_y):
    try:
        out = ImageGrab.grab().load()[i_x, i_y]
    except IndexError:
        print("error wow that's a big number!")
    else:
        return out


def convert_to_hex(colour):
    try:
        output = '#{:02x}{:02x}{:02x}'.format(colour[0],colour[1],colour[2])
        if(debugging):
            print(output)
    except TypeError:
        return "#373d7b"
    else:
        return output

def on_click(x,y,button,pressed):
    if debugging:
        output = ("click at {0},{1},{2},{3}").format(x,y,button,pressed)
        print(get_pixel_colour(x,y))
        print(output)
    hexColour = convert_to_hex(get_pixel_colour(x,y))
    widget.setColour(hexColour)

    


#setup the project
class Interface(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)
        ViewOnline = tk.Button(self)
        ViewOnline.config(justify='left', takefocus=True, text='View Online')
        ViewOnline.place(anchor='nw', x='60', y='160')
        rgbText = tk.Text(self)
        rgbText.config(height='1', insertunfocussed='none', setgrid='false', width='15')
        _text_ = '''hex'''
        rgbText.insert('0.0', _text_)
        rgbText.place(anchor='nw', x='50', y='120')
        rgbLabel = tk.Label(self)
        rgbLabel.config(text='RGB:')
        rgbLabel.place(anchor='nw', x='10', y='120')
        hexLabel = tk.Label(self)
        hexLabel.config(text='Hex:')
        hexLabel.place(anchor='nw', x='10', y='90')
        hexText = tk.Text(self)
        hexText.config(height='1', setgrid='false', width='15')
        _text_ = '''rgb
'''
        hexText.insert('0.0', _text_)
        hexText.place(anchor='nw', x='50', y='90')
        self.frame_3 = tk.Frame(self)
        self.frame_3.config(background='#8680ff', height='70', width='70')
        self.frame_3.place(anchor='nw', x='70', y='5')
       
        

    def setColour(self,hex):
        self.frame_3.config(bg = hex)  


if __name__ == '__main__':
    root = tk.Tk()
    widget = Interface(root)
    widget.pack(expand=True, fill='both')
    listener = mouse.Listener(on_click=on_click)
    listener.start() # start thread
    root.mainloop()
