from bme68x import BME68X
from guizero import App, Text, PushButton, Box
import json

def update():
    global box
    global NormalAirValue
    global MeatValue
    global CheeseValue

    with open("data.json", "r") as file:
        d = json.load(file)

    NormalAirValue.value = d['NormalAir']
    MeatValue.value = d['Meat']
    CheeseValue.value = d['Cheese']

    box.after(500, update)

def main():
    spacing_top = 20
    bg = "#101015"
    text_color = "#f0f0f0"
    text_size = 114
    text_spacing = 12

    app = App(title="Digital Nose App", layout="grid", bg=bg, visible=True)
    app.tk.attributes("-fullscreen", True)
    SpacingTop = Text(app, grid=[0,0], height=spacing_top)

    global box
    box = Box(app, width="fill", height="fill", grid=[0,1], layout="grid")

    NormalAirLabel = Text(box, text="Normal Air", size=text_size, grid=[0,0], color=text_color, width="fill")
    MeatLabel = Text(box, text="Meat", size=text_size, grid=[2,0], color=text_color, width="fill")
    CheeseLabel = Text(box, text="Cheese", size=text_size, grid=[4,0], color=text_color, width="fill")

    global NormalAirValue
    global MeatValue
    global CheeseValue

    NormalAirValue = Text(box, text="0.0%", size=text_size, grid=[0,1], color=text_color)
    MeatValue = Text(box, text="0.0%", size=text_size, grid=[2,1], color=text_color)
    CheeseValue = Text(box, text="0.0%", size=text_size, grid=[4,1], color=text_color)

    Spacer1 = Text(box, width=text_spacing, grid=[1,0])
    Spacer2 = Text(box, width=text_spacing, grid=[3,0])
    Spacer3 = Text(box, width=text_spacing, grid=[1,1])
    Spacer4 = Text(box, width=text_spacing, grid=[3,1])

    box.after(500, update)

    app.display()

if __name__ == '__main__':
    global box
    global NormalAirValue
    global MeatValue
    global CheeseValue
    main()

