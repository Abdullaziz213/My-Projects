import board

display = board.DISPLAY

ziffer = 1


def button_eins(alarm_time, alarmtext):
    global ziffer
    if ziffer == 1:
        alarm_time[0]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 2
    elif ziffer == 2:
        alarm_time[1]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 1
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext






def button_zwei(alarm_time, alarmtext):
    global ziffer
    if ziffer == 1:
        alarm_time[0]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 2
        display.refresh()
    elif ziffer == 2:
        alarm_time[1]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 2
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext




def button_drei(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 3
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 3
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 3
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 3
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 3
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext



def button_vier(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 4
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 4
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 4
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 4
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 4
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext




def button_fuenf(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 5
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 5
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 5
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 5
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 5
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext



def button_sechs(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 6
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 6
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 6
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext

def button_sieben(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 7
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 7
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 7
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext


def button_acht(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 8
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 8
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 8
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext



def button_neun(alarm_time, alarmtext):
    global ziffer
    if ziffer == 2:
        alarm_time[1]   = 9
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 9
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 9
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext


def button_null(alarm_time, alarmtext):
    global ziffer
    if ziffer == 1:
        alarm_time[0]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 2
        display.refresh()
    elif ziffer == 2:
        alarm_time[1]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 3
        display.refresh()
    elif ziffer == 3:
        alarm_time[2]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 4
        display.refresh()
    elif ziffer == 4:
        alarm_time[3]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 5
        display.refresh()
    elif ziffer == 5:
        alarm_time[4]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        ziffer          = 6
        display.refresh()
    elif ziffer == 6:
        alarm_time[5]   = 0
        alarmtext       = f"{alarm_time[0]}{alarm_time[1]}:{alarm_time[2]}{alarm_time[3]}:{alarm_time[4]}{alarm_time[5]}"
        display.refresh()
    return alarmtext


def button_del():
    global ziffer
    ziffer = 1
