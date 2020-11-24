
# !/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

# Festlegen der Motorsensoren
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outD')
motor_medium =ev3.MediumMotor('outB')
# Festlegen der Sensoren
gy = ev3.GyroSensor()     #Gyrosensor
gy.mode = 'GYRO-ANG'
cl = ev3.ColorSensor()    #Farbsensor
cl.mode = 'COL-COLOR'
ts1 = ev3.TouchSensor('in2')     #sensor Links
ts2 = ev3.TouchSensor('in3')     #sensor Rechts
#variablen und Listen Festlegen
squares = []
# Funktionen werden definiert
def leftturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=-105)
    motor_right.run_timed(time_sp=2000, speed_sp=106)
    return


def rightturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=125)
    motor_right.run_timed(time_sp=2000, speed_sp=-105)
    return

def halfturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=-105)
    motor_right.run_timed(time_sp=4000, speed_sp=105)
    return

def drive15squares():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=397)
    motor_right.run_timed(time_sp=2000, speed_sp=397)
    return


def drive1square():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=1000, speed_sp=260)
    motor_right.run_timed(time_sp=1000, speed_sp=260)
    return


def pickingupblocks():  # in eine funktion noch und mit einem stopp feature
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=105)        #Brick turns right
    motor_right.run_timed(time_sp=2000, speed_sp=-105)
    sleep(3)
    x1 = motor_right.position                #messures right motor position in degrees
    y1 = motor_left.position                 #messures let motor position in degrees
    while cl.value() != 3:                      #run until the colour green is detected
        motor_left.run_forever(speed_sp=100)
        motor_right.run_forever(speed_sp=100)
    sleep(1)                        #continues to run for 1 mor second
    motor_left.stop()               #motor stops
    motor_right.stop()
    sleep(0.5)
    motor_medium.run_forever(speed_sp=-190)     #Hold block
    sleep(1)
    x2 = motor_right.position  #New position
    y2 = motor_left.position
    x3 = x2-x1                  #difference between first and second position
    y3 = y2-y1
    motor_left.run_timed(time_sp=1000, speed_sp=-int(y3))      #moves back to first position
    motor_right.run_timed(time_sp=1000, speed_sp=-int(x3))
    print(x1,x2,x3,y1,y2,y3)
    leftturn()                          #turns back to beginning position
    return


def dropoffblocks():
    motor_medium.stop()
    motor_medium.run_timed(time_sp=2000, speed_sp=150)
    return

def navigatesquare():
    if x == 1 or x == 2 or x == 3:
        a1 = motor_right.position                #messures right motor position in degrees
        b1 = motor_left.position                 #messures left motor position in degrees
        drive15squares()
        for i in range(2):
            drive1square()
        if x == 1:
            drive1square()
            a2 = motor_right.position                #messures right motor position in degrees
            b2 = motor_left.position
            leftturn()
            sleep(3)
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=180)
            motor_right.run_timed(time_sp=1000, speed_sp=180)
            sleep(1.5)
            dropoffblocks()
            sleep(0.1)
            motor_left.run_timed(time_sp=1000, speed_sp=-180)
            motor_right.run_timed(time_sp=1000, speed_sp=-180)
            rightturn()
            sleep(3)
            a3 = a2-a1+191
            b3 = b2-b1+191
            motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))      #moves back to first position
            motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
            return

        elif x == 2:
            a2 = motor_right.position  # messures right motor position in degrees
            b2 = motor_left.position
            sleep(1.5)
            dropoffblocks()
            sleep(3)
            a3 = a2 - a1 + 191
            b3 = b2 - b1 + 191
            motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))  # moves back to first position
            motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
            return

        else:
            drive1square()
            a2 = motor_right.position  # messures right motor position in degrees
            b2 = motor_left.position
            rightturn()
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=180)
            motor_right.run_timed(time_sp=1000, speed_sp=180)
            sleep(1.5)
            dropoffblocks()
            sleep(0.1)
            motor_left.run_timed(time_sp=1000, speed_sp=-180)
            motor_right.run_timed(time_sp=1000, speed_sp=-180)
            leftturn()
            sleep(3)
            a3 = a2 - a1 + 191
            b3 = b2 - b1 + 191
            motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))  # moves back to first position
            motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
            return

    elif x == 4 or x == 5 or x == 6:
        a1 = motor_right.position  # messures right motor position in degrees
        b1 = motor_left.position  # messures left motor position in degrees
        drive15squares()
        for i in range(1):
            drive1square()
            if x == 4:
                a2 = motor_right.position  # messures right motor position in degrees
                b2 = motor_left.position
                leftturn()
                motor_left.wait_while('running')
                motor_right.wait_while('running')
                motor_left.run_timed(time_sp=1000, speed_sp=180)
                motor_right.run_timed(time_sp=1000, speed_sp=180)
                sleep(1.5)
                dropoffblocks()
                sleep(0.1)
                motor_left.run_timed(time_sp=1000, speed_sp=-180)
                motor_right.run_timed(time_sp=1000, speed_sp=-180)
                rightturn()
                sleep(3)
                a3 = a2 - a1 + 191
                b3 = b2 - b1 + 191
                motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))  # moves back to first position
                motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
                return

            elif x == 5:
                a2 = motor_right.position  # messures right motor position in degrees
                b2 = motor_left.position
                sleep(1.5)
                dropoffblocks()
                sleep(0.1)
                a3 = a2 - a1 + 191
                b3 = b2 - b1 + 191
                motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))  # moves back to first position
                motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
                return

            else:
                a2 = motor_right.position  # messures right motor position in degrees
                b2 = motor_left.position
                rightturn()
                motor_left.wait_while('running')
                motor_right.wait_while('running')
                motor_left.run_timed(time_sp=1000, speed_sp=180)
                motor_right.run_timed(time_sp=1000, speed_sp=180)
                sleep(1.5)
                dropoffblocks()
                sleep(0.1)
                motor_left.run_timed(time_sp=1000, speed_sp=-180)
                motor_right.run_timed(time_sp=1000, speed_sp=-180)
                leftturn()
                sleep(3)
                a3 = a2 - a1 + 191
                b3 = b2 - b1 + 191
                motor_left.run_timed(time_sp=4000, speed_sp=-int(0.25*b3))  # moves back to first position
                motor_right.run_timed(time_sp=4000, speed_sp=-int(0.25*a3))
                return
    else:
        drive15squares()
        if x == 7:
            leftturn()
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=180)
            motor_right.run_timed(time_sp=1000, speed_sp=180)
            sleep(1.5)
            dropoffblocks()
            sleep(0.01)
            motor_left.run_timed(time_sp=1000, speed_sp=-180)
            motor_right.run_timed(time_sp=1000, speed_sp=-180)
            rightturn()
            sleep(3)
            motor_left.run_timed(time_sp=4000, speed_sp=-189)
            motor_right.run_timed(time_sp=4000, speed_sp=-189)
            return

        elif x == 8:
            sleep(3)
            dropoffblocks()
            sleep(0.5)
            motor_left.run_timed(time_sp=4000, speed_sp=-199)
            motor_right.run_timed(time_sp=4000, speed_sp=-199)
            return

        else:
            rightturn()
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=180)
            motor_right.run_timed(time_sp=1000, speed_sp=180)
            sleep(1.5)
            dropoffblocks()
            sleep(0.01)
            motor_left.run_timed(time_sp=1000, speed_sp=-180)
            motor_right.run_timed(time_sp=1000, speed_sp=-180)
            leftturn()
            sleep(3)
            motor_left.run_timed(time_sp=4000, speed_sp=-195)
            motor_right.run_timed(time_sp=4000, speed_sp=-195)
            return


 # Main Code th9at will be executed

if __name__ == '__main__':
    print("Start")
    x = int(input("Enter number from 1-9"))
    pickingupblocks()  # Motor gets its block
    sleep(2)
    navigatesquare()
