
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
    motor_left.run_timed(time_sp=4000, speed_sp=-42)
    motor_right.run_timed(time_sp=4000, speed_sp=55)
    return

def leftturn2():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=-58)
    motor_right.run_timed(time_sp=4000, speed_sp=65)
    return

def rightturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=67)
    motor_right.run_timed(time_sp=4000, speed_sp=-63)
    return

def rightturn2():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=49)
    motor_right.run_timed(time_sp=4000, speed_sp=-53)
    return

def halfturn():
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=4000, speed_sp=-105)
    motor_right.run_timed(time_sp=4000, speed_sp=105)
    return

def drive15squares():                               #long square
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=266)
    motor_right.run_timed(time_sp=2000, speed_sp=266)
    return


def drive1square():                                    #normal square
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.run_timed(time_sp=2000, speed_sp=100)
    motor_right.run_timed(time_sp=2000, speed_sp=100)
    return


def pickingupblocks():  # in eine funktion noch und mit einem stopp feature
    rightturn()
    sleep(3)
    x1 = motor_right.position                #messures right motor position in degrees
    y1 = motor_left.position                 #messures let motor position in degrees
    while cl.value() != 3:                      #run until the colour green is detected
        motor_left.run_forever(speed_sp=100)
        motor_right.run_forever(speed_sp=100)
    sleep(0.7)                        #continues to run for 1 mor second
    motor_left.stop()               #motor stops
    motor_right.stop()
    sleep(0.1)
    motor_medium.run_forever(speed_sp=-190)     #Hold block
    sleep(1)
    x2 = motor_right.position  #New position
    y2 = motor_left.position
    x3 = x2-x1-40                 #difference between first and second position
    y3 = y2-y1-40
    x4 = 0.25 * x3
    y4 = 0.25 * y3
    motor_left.run_timed(time_sp=4000, speed_sp=-int(y4))      #moves back to first position
    motor_right.run_timed(time_sp=4000, speed_sp=-int(x4))
    print(x1,x2,x3,y1,y2,y3)
    leftturn()                          #turns back to beginning position
    return


def dropoffblocks():
    motor_medium.stop()
    motor_medium.run_timed(time_sp=2000, speed_sp=150)
    return

def navigatesquare(x):
    if x == 1 or x == 2 or x == 3:          #First Row
        drive15squares()
        for i in range(2):
            drive1square()
        if x == 1:
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=100)
            motor_right.run_timed(time_sp=1000, speed_sp=100)
            leftturn()
            sleep(5)
            dropoffblocks()
            sleep(0.1)
            rightturn2()
            sleep(5)
            motor_left.run_timed(time_sp=6000, speed_sp=-175)  # moves back to first position
            motor_right.run_timed(time_sp=6000, speed_sp=-172)
            return

        elif x == 2:
            sleep(1.5)
            dropoffblocks()
            sleep(3)
            motor_left.run_timed(time_sp=6000, speed_sp=-158)  # moves back to first position
            motor_right.run_timed(time_sp=6000, speed_sp=-156)
            return

        else:
            motor_left.wait_while('running')
            motor_right.wait_while('running')
            motor_left.run_timed(time_sp=1000, speed_sp=100)
            motor_right.run_timed(time_sp=1000, speed_sp=100)
            rightturn()
            sleep(5)
            dropoffblocks()
            sleep(0.5)
            leftturn2()
            sleep(5)
            motor_left.run_timed(time_sp=6000, speed_sp=-175)  # moves back to first position
            motor_right.run_timed(time_sp=6000, speed_sp=-172)
            return

    elif x == 4 or x == 5 or x == 6:#second row
        drive15squares()
        for i in range(1):
            drive1square()
            if x == 4:
                leftturn()
                sleep(5)
                dropoffblocks()
                sleep(0.5)
                rightturn2()
                sleep(5)
                motor_left.run_timed(time_sp=5000, speed_sp=-126)  # moves back to first position
                motor_right.run_timed(time_sp=5000, speed_sp=-125)
                return

            elif x == 5:
                sleep(1.5)
                dropoffblocks()
                sleep(0.1)
                motor_left.run_timed(time_sp=5000, speed_sp=-126)  # moves back to first position
                motor_right.run_timed(time_sp=5000, speed_sp=-125)
                return

            else:
                rightturn2()
                sleep(5)
                dropoffblocks()
                sleep(0.5)
                leftturn()
                sleep(5)
                motor_left.run_timed(time_sp=5000, speed_sp=-126)  # moves back to first position
                motor_right.run_timed(time_sp=5000, speed_sp=-125)
                return
    else:                       #third row
        drive15squares()
        if x == 7:
            leftturn()
            sleep(5)
            dropoffblocks()
            sleep(0.5)
            rightturn2()
            sleep(5)
            motor_left.run_timed(time_sp=4000, speed_sp=-123)
            motor_right.run_timed(time_sp=4000, speed_sp=-120)
            return

        elif x == 8:
            sleep(5)
            dropoffblocks()
            sleep(0.5)
            motor_left.run_timed(time_sp=4000, speed_sp=-123)
            motor_right.run_timed(time_sp=4000, speed_sp=-120)
            return

        else:
            rightturn()
            sleep(5)
            dropoffblocks()
            sleep(0.5)
            leftturn2()
            sleep(5)
            motor_left.run_timed(time_sp=4000, speed_sp=-123)
            motor_right.run_timed(time_sp=4000, speed_sp=-120)
            return
