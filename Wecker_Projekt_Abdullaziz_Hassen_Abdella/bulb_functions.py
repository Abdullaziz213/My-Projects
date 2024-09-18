import adafruit_requests as requests


turn_on_endpoint            = "http://172.16.230.248/light/0?turn=on"
turn_off_endpoint           = "http://172.16.230.248/color/0?turn=off"
brightness_low_endpoint     = "http://172.16.230.248/light/0?brightness=10"
brightness_high_endpoint    = "http://172.16.230.248/light/0?brightness=100"



def turn_on():
    response = requests.get(turn_on_endpoint)
    if response.status_code == 200:
        print("Bulb turned on.")
    else:
        print("Failed to turn on the bulb.")


def brightness_low():
    response = requests.get(brightness_low_endpoint)
    if response.status_code == 200:
        print("Bulb got dimmer.")
    else:
        print("Failed to turn on the bulb.")


def brightness_high():
    response = requests.get(brightness_high_endpoint)
    if response.status_code == 200:
        print("Bulb got lighter.")
    else:
        print("Failed to turn on the bulb.")


def turn_off():
    response = requests.get(turn_off_endpoint)
    if response.status_code == 200:
        print("Bulb turned off.")
    else:
        print("Failed to turn off the bulb.")
