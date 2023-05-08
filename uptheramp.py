from drivetrain import Drivetrain
# from gyroturn import GyroTurn
from autoroutine import AutoRoutine
from drivestraight import DriveStraight
from wpimath.controller import PIDController


class UpTheRamp(AutoRoutine):

     def __init__(self, drivetrain):
         self.drivetrain = drivetrain
         self.driveStraight = DriveStraight(self.drivetrain)
         # self.goal = goal_in_meters
         # self.pid_controller = PIDController(20, 0, 0)
         # self.pid_controller.setSetpoint(0)
         # self.pid_controller.setTolerance(.05)
         self.state = 0

     def run(self):

         current_reading = self.drivetrain.getGyroAngleY()
         forward = .9

         if self.state == 0:
             if current_reading > 5:
                 forward = .5
                 self.state = 1

         else:
            if current_reading > 5:
                forward = .5
                self.state = 1
            else:
                forward = 0

         self.driveStraight.run(forward)
         print(f"{self.state=}, {current_reading=}, {forward=}")


