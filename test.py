from pynput.mouse import Listener
from PIL import ImageGrab

def get_pixel_colour(i_x, i_y):
    try:
        out = ImageGrab.grab().load()[i_x, i_y]
    except IndexError:
        print("error wow that's a big number!")
    else:
        return out

def on_move(x,y):
    pass

def on_click(x,y,button,pressed):
    output = ("click at {0},{1},{2},{3}").format(x,y,button,pressed)
    print(get_pixel_colour(x,y))
    print(output)


with Listener(on_click=on_click) as Listener:
    Listener.join()

