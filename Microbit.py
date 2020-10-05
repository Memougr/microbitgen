from microbit import *
import radio
radio.config(channel=9)
radio.on()
radio.send("Il fait très froid aujourd'hui :( ")
