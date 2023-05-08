from wpilib import Spark
from wpilib.drive import DifferentialDrive
import wpilib
import romi
import math


class Drivetrain:
    def __init__(self):
        self.kCountsPerRevolution = 1440.0
        self.kWheelDiameterMeter = 0.07
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.leftEncoder = wpilib.Encoder(4, 5)
        self.rightEncoder = wpilib.Encoder(6, 7)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.leftEncoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.rightEncoder.setDistancePerPulse(0.07 * math.pi / (12 * 120))
        self.gyro = romi.RomiGyro()

        #Intertial Measuring Unit - Gyro
        #calibrate Gyro before running program

    def move(self, forward, rotate):
        self.drivetrain.arcadeDrive(rotate, forward)

    def drive(self, rot: float, fwd: float):
        self.drivetrain.arcadeDrive(rot, fwd)
    def getGyroAngleY(self):

        #Give me the twist of the robot
        #:return: the current twist angle in degrees

        return self.gyro.getAngleY()
    def resetGyro(self):
        pass
        #Resets the angles to all be 0

    def getLeftDistanceMeter(self):
        return self.leftEncoder.getDistance()

    def getRightDistanceMeter(self):
        return self.rightEncoder.getDistance()


