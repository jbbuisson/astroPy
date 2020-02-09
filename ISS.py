from sense_hat import SenseHat
import time

def casque():
    sense = SenseHat()

    sense.clear()
    ##sense.show_message("Hello Albin!")

    #1ere ligne
    ##sense.set_pixel(0, 0, 255, 255, 255)
    ##sense.set_pixel(1, 0, 255, 255, 255)
    sense.set_pixel(2, 0, 0, 0, 0)
    sense.set_pixel(3, 0, 0, 0, 0)
    sense.set_pixel(4, 0, 0, 0, 0)
    sense.set_pixel(5, 0, 0, 0, 0)
    ##sense.set_pixel(6, 0, 255, 255, 255)
    ##sense.set_pixel(7, 0, 255, 255, 255)

    #2eme ligne
    ##sense.set_pixel(0, 1, 255, 255, 255)
    sense.set_pixel(1, 1, 0, 0, 0)
    sense.set_pixel(2, 1, 0, 0, 255)
    sense.set_pixel(3, 1, 0, 0, 255)
    sense.set_pixel(4, 1, 0, 0, 255)
    sense.set_pixel(5, 1, 0, 0, 255)
    sense.set_pixel(6, 1, 0, 0, 0)
    ##sense.set_pixel(7, 1, 255, 255, 255)

    #3eme ligne
    sense.set_pixel(0, 2, 0, 0, 0)
    sense.set_pixel(7, 2, 0, 0, 0)
    for i in range(1, 7):
        sense.set_pixel(i, 2, 0, 0, 255)

    #4eme ligne
    sense.set_pixel(0, 3, 0, 0, 0)
    sense.set_pixel(7, 3, 0, 0, 0)
    for i in range(1, 7):
        sense.set_pixel(i, 3, 0, 0, 255)

    #5eme ligne
    sense.set_pixel(0, 4, 0, 0, 0)
    sense.set_pixel(1, 4, 0, 0, 255)
    sense.set_pixel(2, 4, 0, 0, 255)
    sense.set_pixel(5, 4, 0, 0, 255)
    sense.set_pixel(6, 4, 0, 0, 255)
    sense.set_pixel(7, 4, 0, 0, 0)

    for i in range(3, 5):
        sense.set_pixel(i, 4, 0, 0, 0)

    #6eme ligne
    sense.set_pixel(0, 5, 0, 0, 0)
    sense.set_pixel(1, 5, 0, 0, 255)
    sense.set_pixel(6, 5, 0, 0, 255)
    sense.set_pixel(7, 5, 0, 0, 0)

    for i in range(2, 6):
        sense.set_pixel(i, 5, 0, 0, 0)

    #7eme ligne
    sense.set_pixel(0, 6, 0, 0, 0)
    sense.set_pixel(1, 6, 0, 0, 255)
    sense.set_pixel(6, 6, 0, 0, 255)
    sense.set_pixel(7, 6, 0, 0, 0)

    for i in range(2, 6):
        sense.set_pixel(i, 6, 0, 0, 0)

    #7eme ligne
    sense.set_pixel(0, 7, 0, 0, 0)
    sense.set_pixel(1, 7, 0, 0, 255)
    sense.set_pixel(6, 7, 0, 0, 255)
    sense.set_pixel(7, 7, 0, 0, 0)

    for i in range(2, 6):
        sense.set_pixel(i, 7, 0, 0, 0)

def creeper():
    sense = SenseHat()
    O = (0, 255, 0)
    X = (0, 0, 0)

    sense.clear()

    creeper_pixels = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, X, X, O, O, X, X, O,
        O, X, X, O, O, X, X, O,
        O, O, O, X, X, O, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, X, X, X, O, O,
        O, O, X, O, O, X, O, O,
    ]

    sense.set_pixels(creeper_pixels)

creeper()
time.sleep(2)
casque()

time.sleep(2)
sense = SenseHat()
sense.show_message("Victoire Albin! :-)")
