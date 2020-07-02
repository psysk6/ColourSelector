import json
import requests

def getNearestName(hex):
    code = hex.replace('#', '')
    url = ("http://www.thecolorapi.com/id?format=json&hex={0}").format(code)

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    jsonRes = response.json()

    nameBlock = jsonRes['name']

    name = nameBlock['value']

    return name