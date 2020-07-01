import tkinter as tk
import tkinter.ttk as ttk


class NewprojectWidget(tk.Frame):
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
        frame_3 = tk.Frame(self)
        frame_3.config(background='#8680ff', height='70', width='70')
        frame_3.place(anchor='nw', x='70', y='5')


def task():
    print("hello")
    root.after(2000,task)

if __name__ == '__main__':
    root = tk.Tk()
    widget = NewprojectWidget(root)
    widget.pack(expand=True, fill='both')
    root.after(2000,task)
    root.mainloop()
