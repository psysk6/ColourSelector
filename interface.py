import tkinter as tk
import tkinter.ttk as ttk
from clickHandler import *
from colourEval import *
from pynput import *
from apiuse import *

debugging = False

#handle clicks
def on_click(x,y,button,pressed):
    if debugging:
        output = ("click at {0},{1},{2},{3}").format(x,y,button,pressed)
        print(get_pixel_colour(x,y))
        print(output)
    hexColour = convert_to_hex(get_pixel_colour(x,y),debugging)
    widget.setColour(hexColour,get_pixel_colour(x,y))


#setup the project
class Interface(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)
        ViewOnline = tk.Button(self)
        ViewOnline.config(justify='left', takefocus=True,command = self.fun(), text='Select Colour')
        ViewOnline.place(anchor='nw', x='60', y='170')
        self.rgbText = tk.Text(self)
        self.rgbText.config(height='1', insertunfocussed='none', setgrid='false', width='15')
        _text_ = '''hex'''
        self.rgbText.insert('0.0', _text_)
        self.rgbText.place(anchor='nw', x='50', y='140')

        
        self.nameText = tk.Text(self)
        self.nameText.config(height='1', insertunfocussed='none', setgrid='false', width='15')
        _text_ = '''hex'''
        self.nameText.insert('0.0', _text_)
        self.nameText.place(anchor='nw', x='50', y='80')


        
        nameLabel = tk.Label(self)
        nameLabel.config(text='Name:')
        nameLabel.place(anchor='nw', x='10', y='80')



        rgbLabel = tk.Label(self)
        rgbLabel.config(text='RGB:')
        rgbLabel.place(anchor='nw', x='10', y='140')

       


        hexLabel = tk.Label(self)
        hexLabel.config(text='Hex:')
        hexLabel.place(anchor='nw', x='10', y='110')
        self.hexText = tk.Text(self)
        self.hexText.config(height='1', setgrid='false', width='15')
        _text_ = '''rgb
'''
        self.hexText.insert('0.0', _text_)
        self.hexText.place(anchor='nw', x='50', y='110')
        self.frame_3 = tk.Frame(self)
        self.frame_3.config(background='#8680ff', height='70', width='70')
        self.frame_3.place(anchor='nw', x='70', y='5')
       
    def fun(self):  
        print("doing a thing")

    def setColour(self,hex,rgb):
        self.frame_3.config(bg = hex) 

        self.hexText.delete(1.0,"end")
        self.hexText.insert(1.0,hex)
        
        self.rgbText.delete(1.0,"end")
        self.rgbText.insert(1.0,rgb)
        self.isSelecting = False
        
        self.nameText.delete(1.0,"end")
        self.nameText.insert(1.0,getNearestName(hex)) 


if __name__ == '__main__':
    root = tk.Tk()
    widget = Interface(root)
    root.geometry("200x200")
    root.resizable(0,0)
    widget.pack(expand=True, fill='both')
    listener = mouse.Listener(on_click=on_click)
    listener.start() # start thread
    root.mainloop()
