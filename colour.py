from PIL import ImageGrab
from PIL import ImageColor
import json
import requests


class colour():
    def __init__(self,iX,iY):
        self.rgb = self.get_pixel_colour(iX,iY)
        self.hex = self.convert_to_hex(self.rgb,True)
        self.name = self.getNearestName(self.hex) 

    def getHex(self):
            return self.rgb
        
    def getRgb(self):
        return self.hex
    
    def getName(self):
        return self.name


    def get_pixel_colour(self,i_x, i_y):
        try:
            out = ImageGrab.grab().load()[i_x, i_y]
        except IndexError:
            print("error wow that's a big number!")
            return (0,0,0)
        else:
            return out

    
    def convert_to_hex(self,colour,debugging):
        try:
            output = '#{:02x}{:02x}{:02x}'.format(colour[0],colour[1],colour[2])
            if(debugging):
                print(output)
        except TypeError:
            return "#373d7b"
        else:
            return output
    
    def getNearestName(self,hex):
        code = hex.replace('#', '')
        url = ("http://www.thecolorapi.com/id?format=json&hex={0}").format(code)
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        jsonRes = response.json()
        nameBlock = jsonRes['name']
        name = nameBlock['value']
        return name

