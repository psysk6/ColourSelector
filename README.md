# ColourSelector (maybe I'll actually give it a proper name idk yet)

## About

A simple colour testing application which I didn't really need but kinda wanted.

Tired of having to screenshot and open in photoshop to test a colour? this is the app for you!

A very simple colour testing widget you can have open on your desktop to test the colour of a pixel on the screen.

It features <a href = "https://www.thecolorapi.com/">colourAPI</a> to fetch the closest named colour to your colour selection and outputs in rgb and hex.

Yes, I know it's super simple. But I wanted it for actual work so I set aside an evening to do it. I even learned a bit or two about tkinter i.e. how to avoid using it in favour of a graphical editor (see <a href = "https://github.com/alejandroautalan/pygubu">pygubu</a>)

Hope you find it as useful as I do I have integrated it into my web development workflows and it works solidly!

---

## Installation

Compiled version is availible <a href = "">here</a>

I might actually set up a proper workflow for it later if I have time but I'm lazy so it might be a while!

## Running your own

Make sure you have the following libraries installed:

- pynput
- tkinter
- Pillow

Application should run from pycolour.py

```
python pyColour.py
```

## Compiling your own.

Should you wish to compile your own version of this app (god only knows why) you can use pyInstaller

```
pip install pyinstaller
pyinstaller pyColour.py
```

this will create a /dist directory which will contain an executable version of the application. inside the dist folder will be pyColour.exe

## Known issues

- Bug with Pillow (currently handled with an exception) unfortunately it will only grab the primary monitor therefore clicking on other monitors would cause a crash.

## the future of this

Must:

- Icons (making it less tkinter)
- Buttons to add straight to clipboard
- Substute for pillow as it has an issue with grabbing multiple screens (this could be a project within itself)

Should:

- Some kind of automatic build process (again if I can be asked)

Could:

- Colour Pallets using an api (find appropriate colour palletes)
- Saved colours pallette (does not have to be remote could just be local)
