from PIL import ImageGrab
from PIL import ImageColor
import json
import requests

# class for instances of colour


class colour():
    # Takes parameters iX and iY corresponding to the pixel the user has clicked
    def __init__(self, iX, iY):
        # use the constructor parameters as parameters to the method to return the rgb pixel colours.
        self.rgb = self.get_pixel_colour(iX, iY)
        # call to function to convert to hex
        self.hex = self.convert_to_hex(self.rgb)
        # use api callw with the hex value retrieved from the function call
        self.name = self.getNearestName(self.hex)

    # Function which returns the colour of the clicked pixel using it's x and y coordinates

    def get_pixel_colour(self, i_x, i_y):
        try:
            # try to get a 'screen grab (from pillow library) of the pixel at i_x , i_y..
            out = ImageGrab.grab().load()[i_x, i_y]
        except IndexError:
            # ..except if the index is out of bounds..
            print("error wow that's a big number!")
            # ..return default colour (rgb 0,0,0)
            return (0, 0, 0)
        else:
            # ..else return the rgb value
            return out

    def convert_to_hex(self, colour):
        """[summary]

        Args:
            colour ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            output = '#{:02x}{:02x}{:02x}'.format(
                colour[0], colour[1], colour[2])
        except TypeError:
            return "#373d7b"
        else:
            return output

    def getNearestName(self, hex):
        code = hex.replace('#', '')
        url = (
            "http://www.thecolorapi.com/id?format=json&hex={0}").format(code)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        jsonRes = response.json()
        nameBlock = jsonRes['name']
        name = nameBlock['value']
        return name

    # just a lovely little bunch of getter methods :)

    def getHex(self):
        return self.rgb

    def getRgb(self):
        return self.hex

    def getName(self):
        return self.name
