import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Tag1 = str('1800387799CE')
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
# GPIO.output(23,False)
# GPIO.output(24,False)

GPIO.output(23,True)
GPIO.output(24,True)
PortRF = serial.Serial('/dev/ttyS0',9600,timeout=1)
# PortRF = serial.Serial('/dev/serial1',9600)
# print 1
# while True:
#     ID = ""
#     read_byte = PortRF.read(1)
#     print read_byte
#     if read_byte=="\x02":
#         for Counter in range(12):
#             read_byte=PortRF.read(1)
#             ID = ID + str(read_byte)
#             print hex(ord( read_byte))
#         print ID
#         if ID == Tag1:
#             print "matched"
#             GPIO.output(23,True)
#             GPIO.output(24,False)
#             time.sleep(5)
#             GPIO.output(23,False)
#         else:
#             GPIO.output(23,False)
#             print "Access Denied"
#             GPIO.output(24,True)
#             time.sleep(5)
#             GPIO.output(24,False)

while True:
    ID = ""
    line = PortRF.readline()
    read_byte = line.rstrip().split()
    # print read_byte
    if read_byte=="\x02":
        for Counter in range(12):
            read_byte=PortRF.read(1)
            ID = ID + str(read_byte)
            print hex(ord( read_byte))
        print ID
# while True:
#     daten = PortRF.read(14)
#     # PortRF.close()
#     daten = daten.replace("\x02", "" )
#     daten = daten.replace("\x03", "" )
#     GPIO.output(23,True)
#     GPIO.output(24,False)
#     print daten