#!/usr/bin/python
# coding=utf-8

import serial

# This is where I read the RFID tag

def read_rfid():
    ser = serial.Serial("/dev/ttyS0")
    ser.baudrate = 9600
    daten = ser.read(14)
    ser.close()
    daten = daten.replace("\x02", "" )
    daten = daten.replace("\x03", "" )
    return daten

id = read_rfid()
print id