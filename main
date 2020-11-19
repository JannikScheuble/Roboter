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
cl.mode='COL-COLOR'

# Funktionen werden definiert
def leftturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=-105)
    motor_right.run_timed(time_sp=2000, speed_sp=105)
    return


def rightturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=105)
    motor_right.run_timed(time_sp=2000, speed_sp=-105)
    return

def halfturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=-105)
    motor_right.run_timed(time_sp=4000, speed_sp=105)
    return


def drive():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=360)
    motor_right.run_timed(time_sp=2000, speed_sp=360)
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
        motor_left.run_forever(speed_sp=60)
        motor_right.run_forever(speed_sp=61)
    sleep(1)                        #continues to run for 1 mor second
    motor_left.stop()               #motor stops
    motor_right.stop()
    sleep(1)
    motor_medium.run_forever(speed_sp=-180)     #Hold block
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
    return

# Main Code th9at will be executed
if __name__ == '__main__':
    print("Hello my Name is Arnold and i want to play TicTacToe with you")
    #Motor gets its block
    pickingupblocks()
    sleep(10)
    dropoffblocks()
    print("Finished")






