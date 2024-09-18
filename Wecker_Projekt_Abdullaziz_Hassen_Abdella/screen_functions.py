







def weatherscreen_create(gruppe, bild, temperatur, beschreibung, stadt, knopf, knopf2, knopf3):
    while len(gruppe) > 0:
        gruppe.pop()
    gruppe.append(bild)
    gruppe.append(temperatur)
    gruppe.append(beschreibung)
    gruppe.append(stadt)
    gruppe.append(knopf)
    gruppe.append(knopf2)
    gruppe.append(knopf3)


def mainscreen_create(gruppe, bild, titel, knopf, knopf2, uhr):
    while len(gruppe) > 0:
        gruppe.pop()
    gruppe.append(bild)
    gruppe.append(titel)
    gruppe.append(knopf)
    gruppe.append(knopf2)
    gruppe.append(uhr)



def alarmscreen_create(gruppe, bild, knopf, alarmknopf, alarmtext):
    while len(gruppe) > 0:
        gruppe.pop()
    gruppe.append(bild)
    gruppe.append(knopf)
    gruppe.append(alarmknopf)
    gruppe.append(alarmtext)


def notificationscreen_create(gruppe, bild, knopf):
    while len(gruppe) > 0:
        gruppe.pop()
    gruppe.append(bild)
    gruppe.append(knopf)


def numpadscreen_create(gruppe, bild, knopf, rect, text):
    while len(gruppe) > 0:
        gruppe.pop()
    gruppe.append(bild)
    gruppe.append(knopf)
    gruppe.append(rect)
    gruppe.append(text)



def numpad_create(gruppe, eins, zwei, drei, vier, fuenf, sechs, sieben, acht, neun, null, enter, delete):
    gruppe.append(eins)
    gruppe.append(zwei)
    gruppe.append(drei)
    gruppe.append(vier)
    gruppe.append(fuenf)
    gruppe.append(sechs)
    gruppe.append(sieben)
    gruppe.append(acht)
    gruppe.append(neun)
    gruppe.append(null)
    gruppe.append(enter)
    gruppe.append(delete)


