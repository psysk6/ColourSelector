from PIL import ImageGrab
from PIL import ImageColor

def get_pixel_colour(i_x, i_y):
    try:
        out = ImageGrab.grab().load()[i_x, i_y]
    except IndexError:
        print("error wow that's a big number!")
    else:
        return out


def convert_to_hex(colour,debugging):
    try:
        output = '#{:02x}{:02x}{:02x}'.format(colour[0],colour[1],colour[2])
        if(debugging):
            print(output)
    except TypeError:
        return "#373d7b"
    else:
        return output