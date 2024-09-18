from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_button import Button
font = bitmap_font.load_font("/fonts/Helvetica-Bold-36.bdf")

def create_button_designs():
    buttonhaupt_design = Button(
    x=0,
    y=0,
    width=480,
    height=40,
    label="",
    label_font=font,
    label_color=0x000000,
    fill_color=0x03345F,
    outline_color=0x000000,
    )
    buttonalarm_design = Button(
    x=0,
    y=230,
    width=480,
    height=40,
    label="Aufstehen",
    label_font=font,
    label_color=0x000000,
    fill_color=0xF00000,
    outline_color=0x000000,
    )
    buttonalarmchoice_design = Button(
    x=0,
    y=0,
    width=50,
    height=50,
    label="",
    label_font=font,
    label_color=0x000000,
    fill_color=0x808080,
    outline_color=0x000000,
    )
    return buttonhaupt_design, buttonalarm_design, buttonalarmchoice_design







