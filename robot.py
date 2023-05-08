import os
import wpilib
from wpilib import TimedRobot
from robotcontainer import RobotContainer


class MyRobot(TimedRobot): #none means nothing is passed out - no return
    def robotInit(self):
       self.container = RobotContainer()

    def autonomousInit(self):
        self.auto = self.container.get_autonomous()

    def autonomousPeriodic(self):
        self.auto.run()
    def autonmousExit(self):
        self.container.drivetrain.resetEncoders()
        self.container.drivetrain.resetGyro()

    def teleopPeriodic(self):
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        self.container.drivetrain.drive(rotate, forward)
        print(f"Forward: {forward}, Rotate: {rotate}")





if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)
