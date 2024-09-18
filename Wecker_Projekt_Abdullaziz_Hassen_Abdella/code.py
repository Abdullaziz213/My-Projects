import board
import busio
import audioio
import digitalio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_pyportal import PyPortal
import displayio
import adafruit_touchscreen
from adafruit_button import Button
from adafruit_display_shapes.rect import Rect
import time
import json
from digitalio import DigitalInOut, Direction, Pull
import adafruit_requests as requests
from buttons_functions import create_button_designs
from screen_functions import (
    mainscreen_create,
    weatherscreen_create,
    alarmscreen_create,
    notificationscreen_create,
    numpadscreen_create,
    numpad_create,
)
from numpad_functions import (
    button_eins,
    button_zwei,
    button_drei,
    button_vier,
    button_fuenf,
    button_sechs,
    button_sieben,
    button_acht,
    button_neun,
    button_null,
    button_del
)
from bulb_functions import (
    turn_on,
    turn_off,
    brightness_high,
    brightness_low
)
# lade die WLAN Verbindungsdaten

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise


# Allgemeine Variablen definieren
display         = board.DISPLAY
myGroup         = displayio.Group()
wetter_text     = displayio.Group()
numpad          = displayio.Group()
ts              = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(480, 320),
)
haupt         = displayio.OnDiskBitmap(open("/images/background.bmp", "rb"))
wetter        = displayio.OnDiskBitmap(open("/images/redbackground.bmp", "rb"))
alarm         = displayio.OnDiskBitmap(open("/images/bluebackground.bmp", "rb"))
alarm_active  = displayio.OnDiskBitmap(open("/images/alarm.bmp", "rb"))
alarm_choice  = displayio.OnDiskBitmap(open("/images/wecker.bmp", "rb"))
radio_url     = "https://stream.streambase.ch/radiofm1/mp3-192/direct/"
alarmsound    = "/sounds/wecker.wav"
LOCATION      = "Sankt Gallen, CH"
DATA_SOURCE   = "http://api.openweathermap.org/data/2.5/weather?q=" + LOCATION
DATA_SOURCE  += "&appid=" + secrets["openweather_token"]
DATA_LOCATION = []


# PyPortal instanizieren
pyportal = PyPortal(
    url=DATA_SOURCE, json_path=DATA_LOCATION, default_bg=("/images/main.bmp")
)

font = bitmap_font.load_font("/fonts/Helvetica-Bold-36.bdf")


city_text           = None
temp_text           = None
description_text    = None


def display_weather(weather):
    weather         = json.loads(weather)
    city_name       = weather["name"] + ", " + weather["sys"]["country"]
    print(city_name)
    global city_text  # Die globale Variable verwenden
    city_text       = label.Label(font, text=city_name)
    city_text.x     = 10
    city_text.y     = 230
    city_text.color = 0xFFFFFF

    global temp_text
    temp_text       = label.Label(font)
    temp_text.x     = 410
    temp_text.y     = 290
    temp_text.color = 0xFFFFFF
    temperature     = weather["main"]["temp"] - 273.15  # its...in kelvin
    print(temperature)
    temp_text.text  = "%d °C" % temperature

    global description_text
    description_text        = label.Label(font)
    description_text.x      = 10
    description_text.y      = 290
    description_text.color  = 0xFFFFFF
    description             = weather["weather"][0]["description"]
    description             = description[0].upper() + description[1:]
    print(description)
    description_text.text   = description


display_weather(pyportal.fetch())


localtile_refresh = None



with open("alarm.json", "r") as json_file:
    data = json.load(json_file)


print(data["alarms"][0]["time"])

alarm_time      = data["alarms"][0]["time"]
alarm_ausgelost = 1
screennum       = 1
ziffer          = 1
schalter        = 0
hellig          = 0


# Uhr gestallten
clock_color     = 0xFFFFFF
clock_area      = label.Label(font, clock_text="", color=clock_color)
clock_area.x    = 10
clock_area.y    = 40


alarm_text          = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
color               = 0xF00000
alarm_text_area     = label.Label(font, text=alarm_text, color=color)
alarm_text_area.x   = 160
alarm_text_area.y   = 160


# Text, Schriftart und Farbe konfigurieren
text    = "Willkommen!"
color   = 0xF00000

# Text Area konfigurieren
text_area   = label.Label(font, text=text, color=color)
text_area.x = 190
text_area.y = 50


def sounds():
    pyportal.play_file(alarmsound)




refresh_time    = None
weather_refresh = None

# aktualisiere die Wetterdaten
def updateWeatherData():
    value = pyportal.fetch()
    print("Response is", value)
    display_weather(value)


# synchronisiere die Uhrzeit
def updateTimeData():
    time_now = time.localtime()
    print("Getting time from internet!")
    pyportal.get_local_time()


(
    buttonhaupt_design,
    buttonalarm_design,
    buttonalarmchoice_design,
) = create_button_designs()


# Wetterknopf erstellen
button_wetter       =   Button(
    x               =   0,
    y               =   270,
    width           =   buttonhaupt_design.width,
    height          =   buttonhaupt_design.height,
    label           =   "Wetter und Lichtschalter",
    label_font      =   font,
    label_color     =   buttonhaupt_design.label_color,
    fill_color      =   buttonhaupt_design.fill_color,
    outline_color   =   buttonhaupt_design.outline_color,
)

# Weckerknopf erstellen
button_wecker       =   Button(
    x               =   0,
    y               =   140,
    width           =   buttonhaupt_design.width,
    height          =   buttonhaupt_design.height,
    label           =   "Wecker",
    label_font      =   font,
    label_color     =   buttonhaupt_design.label_color,
    fill_color      =   buttonhaupt_design.fill_color,
    outline_color   =   buttonhaupt_design.outline_color,
)

# Hauptmenuknopf erstellen
button_hauptmenu    =   Button(
    x               =   0,
    y               =   30,
    width           =   buttonhaupt_design.width,
    height          =   buttonhaupt_design.height,
    label           =   "Hauptmenu",
    label_font      =   font,
    label_color     =   buttonhaupt_design.label_color,
    fill_color      =   buttonhaupt_design.fill_color,
    outline_color   =   buttonhaupt_design.outline_color,
)


button_lichtschalter = Button(
    x=40,
    y=135,
    width=80,
    height=buttonalarm_design.height,
    label="Lichtschalter",
    label_font=font,
    label_color=buttonalarm_design.label_color,
    fill_color=buttonalarm_design.fill_color,
    outline_color=buttonalarm_design.outline_color,
)

button_helligkeit = Button(
    x=370,
    y=135,
    width=80,
    height=buttonalarm_design.height,
    label="Helligkeit",
    label_font=font,
    label_color=buttonalarm_design.label_color,
    fill_color=buttonalarm_design.fill_color,
    outline_color=buttonalarm_design.outline_color,
)




button_alarm_settings   =   Button(
    x                   =   0,
    y                   =   200,
    width               =   buttonalarm_design.width,
    height              =   buttonalarm_design.height,
    label               =   "Wecker einstellen",
    label_font          =   font,
    label_color         =   buttonalarm_design.label_color,
    fill_color          =   buttonalarm_design.fill_color,
    outline_color       =   buttonalarm_design.outline_color,
)


numpad_eins   =   Button(
    x               =   130,
    y               =   200,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "1",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_zwei   =   Button(
    x               =   210,
    y               =   200,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "2",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_drei   =   Button(
    x               =   290,
    y               =   200,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "3",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_vier   =   Button(
    x               =   130,
    y               =   135,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "4",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_fuenf  =   Button(
    x               =   210,
    y               =   135,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "5",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)

numpad_sechs  =   Button(
    x               =   290,
    y               =   135,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "6",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_sieben =   Button(
    x               =   130,
    y               =   70,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "7",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)

numpad_acht   =   Button(
    x               =   210,
    y               =   70,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "8",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)


numpad_neun   =   Button(
    x               =   290,
    y               =   70,
    width           =   buttonalarmchoice_design.width,
    height          =   buttonalarmchoice_design.height,
    label           =   "9",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)

numpad_null   =   Button(
    x               =   130,
    y               =   265,
    width           =   210,
    height          =   buttonalarmchoice_design.height,
    label           =   "0",
    label_font      =   font,
    label_color     =   buttonalarmchoice_design.label_color,
    fill_color      =   buttonalarmchoice_design.fill_color,
    outline_color   =   buttonalarmchoice_design.outline_color,
)

numpad_enter  =   Button (
    x               =   370,
    y               =   5,
    width           =   80,
    height          =   80,
    label           =   "->",
    label_font      =   font,
    label_color     =   0xFFFFFF,
    fill_color      =   0x008800,
    outline_color   =   0xFFFFFF,
)


numpad_del    =   Button (
    x               =   370,
    y               =   230,
    width           =   80,
    height          =   80,
    label           =   "DEL",
    label_font      =   font,
    label_color     =   0xFFFFFF,
    fill_color      =   0xF00000,
    outline_color   =   0xFFFFFF,
)

numpad_create(
    numpad,
    numpad_eins,
    numpad_zwei,
    numpad_drei,
    numpad_vier,
    numpad_fuenf,
    numpad_sechs,
    numpad_sieben,
    numpad_acht,
    numpad_neun,
    numpad_null,
    numpad_enter,
    numpad_del,
)


rect = Rect(130, 5, 210, 50, fill=0x808080, outline=0x000000, stroke=3)


# Die Gruppen zu den Hauptgruppen hinzufügen
hauptbild = displayio.TileGrid(
    haupt, pixel_shader=getattr(haupt, "pixel_shader", displayio.ColorConverter())
)
wetterbild = displayio.TileGrid(
    wetter, pixel_shader=getattr(wetter, "pixel_shader", displayio.ColorConverter())
)
weckerbild = displayio.TileGrid(
    alarm, pixel_shader=getattr(alarm, "pixel_shader", displayio.ColorConverter())
)
alarm_activebild = displayio.TileGrid(
    alarm_active,
    pixel_shader=getattr(alarm_active, "pixel_shader", displayio.ColorConverter()),
)
alarm_choicebild = displayio.TileGrid(
    alarm_choice,
    pixel_shader=getattr(alarm_choice, "pixel_shader", displayio.ColorConverter()),
)

turn_off()
brightness_low
mainscreen_create(
    myGroup, hauptbild, text_area, button_wecker, button_wetter, clock_area
)
def time_to_struct_time(time_str):
    alarm_hour, alarm_minute, alarm_second = map(int, time_str.split(':'))
    return time.struct_time((0, 0, 0, alarm_hour, alarm_minute, alarm_second, 0, 0, -1))

display.show(myGroup)


darkscreen = time.monotonic()

al = 0

while True:
    touch = ts.touch_point

    if (not weather_refresh) or ((time.monotonic() - weather_refresh) > 600):
        weather_refresh = time.monotonic()
        updateWeatherData()
        print("Wetterdaten aktualisiert")

    if (not refresh_time) or ((time.monotonic() - refresh_time) > 480):
        refresh_time = time.monotonic()
        updateTimeData()
        print("Uhrzeit synchronisiert")

    current_time = time.localtime()
    clock_area.text = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"
    current_time_struct = time.localtime()
    current_time = time_to_struct_time(f"{current_time_struct.tm_hour:02d}:{current_time_struct.tm_min:02d}:{current_time_struct.tm_sec:02d}")
    alarm_time_struct = time_to_struct_time(alarm_text_area.text)

    # überprüfe ob die Alarmzeit erreicht wurde
    if current_time == alarm_time_struct:
        turn_on
        brightness_high
        darkscreen = time.monotonic()
        display.brightness = 1.0
        screennum = 4
        alarm_ausgelost = 2
        notificationscreen_create(myGroup, alarm_activebild, button_hauptmenu)
    if alarm_ausgelost is 2:
        sounds()
        time.sleep(0.2)
        if touch:
            if button_hauptmenu.contains(touch) and screennum is 4:
                screennum = 1
                brightness_low
                mainscreen_create(
                    myGroup,
                    hauptbild,
                    text_area,
                    button_wecker,
                    button_wetter,
                    clock_area,
                )
                print("Hauptmenuknopf gedrückt")
                alarm_ausgelost = 1

    # überprüfe ob der Alarmscreen zurückgesetzt werden kann
    if ((time.monotonic() - darkscreen) > 60) and screennum is not 4 and not touch:
        screennum = 90
        display.brightness = 0

    # überprüfe ob ein Touchevent ausgelöst wurde

    if touch:

        if screennum is 90:
            screennum = 1
            darkscreen = time.monotonic()
            mainscreen_create(
                myGroup, hauptbild, text_area, button_wecker, button_wetter, clock_area
            )
            time.sleep(0.1)
            display.brightness = 1.0

        if button_wetter.contains(touch) and screennum is 1:
            al = 1
            screennum = 2
            weatherscreen_create(
                myGroup,
                wetterbild,
                temp_text,
                description_text,
                city_text,
                button_hauptmenu,
                button_lichtschalter,
                button_helligkeit
            )
            print("Wetterknopf gedrückt")

        if button_wecker.contains(touch) and screennum is 1:
            # turn_off()
            screennum = 3
            alarmscreen_create(
                myGroup,
                weckerbild,
                button_hauptmenu,
                button_alarm_settings,
                alarm_text_area,
            )
            print("Alarmknopf gedrückt ")

        if button_hauptmenu.contains(touch) and screennum is not 5 and screennum is not 1:

            screennum = 1
            mainscreen_create(
                myGroup, hauptbild, text_area, button_wecker, button_wetter, clock_area
            )
            print("Hauptmenuknopf gedrückt")

        if button_lichtschalter.contains(touch) and screennum is 2:
            if schalter is 0:
                turn_on()
                schalter = 1
                print("an")
            else:
                turn_off()
                schalter = 0
                print("aus")
            time.sleep(1)

        if button_helligkeit.contains(touch) and screennum is 2:
            if hellig is 0:
                brightness_high()
                hellig = 1
                print("hell")
            else:
                brightness_low()
                hellig = 0
                print("dunkel")
            time.sleep(1)

        if button_alarm_settings.contains(touch) and screennum is 3:
            numpadscreen_create(myGroup, alarm_choicebild, numpad, rect, alarm_text_area)
            screennum = 5
            alarm_text_area.y   = 27
            print("Wecker einstellen knopf gedrückt")

        if numpad_eins.contains(touch) and screennum is 5:
            alarm_text_area.text = button_eins(alarm_time, alarm_text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_zwei.contains(touch) and screennum is 5:
            alarm_text_area.text = button_zwei(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_drei.contains(touch) and screennum is 5:
            alarm_text_area.text = button_drei(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_vier.contains(touch) and screennum is 5:
            alarm_text_area.text = button_vier(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_fuenf.contains(touch) and screennum is 5:
            alarm_text_area.text = button_fuenf(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_sechs.contains(touch) and screennum is 5:
            alarm_text_area.text = button_sechs(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_sieben.contains(touch) and screennum is 5:
            alarm_text_area.text = button_sieben(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_acht.contains(touch) and screennum is 5:
            alarm_text_area.text = button_acht(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_neun.contains(touch) and screennum is 5:
            alarm_text_area.text = button_neun(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_null.contains(touch) and screennum is 5:
            alarm_text_area.text = button_null(alarm_time, alarm_text_area.text)
            display.refresh()
            print(alarm_text_area.text)
            time.sleep(0.5)



        if numpad_enter.contains(touch) and screennum is 5:
            data["alarms"][0]["time"] = alarm_time
            with open("alarm.json", "w") as json_file:
                json.dump(data, json_file)
            screennum = 3
            alarmscreen_create(
                myGroup,
                weckerbild,
                button_hauptmenu,
                button_alarm_settings,
                alarm_text_area,
            )
            alarm_text_area.y   = 160
        if numpad_del.contains(touch) and screennum is 5:
            button_del()
            alarm_time = [0,0,0,0,0,0]
            alarm_text_area.text = "00:00:00"
            print(alarm_text_area.text)
            display.refresh()

