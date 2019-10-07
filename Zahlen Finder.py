""" Eine zufaellige Zahl wird gesucht
    Autor: Mohamad Shaftar
    Datum: 28.09.2019
    """

import random   # Zufaellige Zahlen importieren

# Zur Hilfe beim Zahlen finden
def hinweis():
    global counter
    if counter == 5:
        print('Hinweis:')
        print('Die Zahl ist größer als ', x - counter, ' und kleiner als', x + counter)
        abfrage()
    elif counter == 10:
        print('Du hast ', counter, ' Male falsche Zahlen eingegeben.')
        print('Hinweis:')
        print('Die Zahl ist zwischen', x - y, ' und ', x + y)
        abfrage()
    elif counter == 20:
        print('Du hast keine Chance die richtige Zahl zutreffen. Aufwiedersehen!!')
        exit()


# Falls Der Benutzer nicht weiter machen will
def abfrage():
    print('Willst du weiter machen? ')
    eingabe = input('Yes=y  No=n: ')
    if eingabe == 'n':
        print('Aufwiedersehen!')
        exit()
    elif eingabe == 'y':
        pass


def findzalh():
    global counter
    zahl = int(input('Geben Sie eine Zahl ein: '))
    while True:    # Solange laufen bis die richtige Zahl gefunden wird
        if zahl < x:    # Wenn Zahl kleiner als x
            print('....................Die Zahl ist zu klein')  # Ausgabe wenn Zahl Kleiner als x
            hinweis()
        elif zahl > x:
            print('.....................Die Zahl ist zu groß')
            hinweis()
        elif zahl == x:
            print('Jaaaaaa, Zahl gefunden,', str(zahl), ' ist richtig')
            break
        zahl = int(input('Geben Sie eine Zahl ein: '))
        counter += 1


print('Willkommen beim Zahlen-finder Spiel')    # Zusaetzlich zur Hilfe beim Raten
x = random.randint(1, 100)  # Zwischen 50 und 100, werden Zahlen zufaellig erstellt
y = random.randint(1, 20)  # Zahlen zur Hilfe
counter = 1
findzalh()
