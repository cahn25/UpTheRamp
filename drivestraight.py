from autoroutine import AutoRoutine
from wpimath.controller import PIDController

class DriveStraight(AutoRoutine):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain
        # self.goal = goal_in_meters
        self.pid_controller = PIDController(120, 0 , 0)
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        # self.pid_controller_2 = PIDController(20, 0 , 0) #Adam helped me create a second controller
        # self.pid_controller_2.setSetpoint(self.goal)
        # self.pid_controller_2.setTolerance(.05) #meters off from straight
        #self.kp = -20

    def run(self, forward):
        angle_difference = self.drivetrain.getLeftDistanceMeter()-self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller.calculate(angle_difference)

        # distance_difference = self.drivetrain.goal()-self.drivetrain.averageDistanceMeter()
        # forward = self.pid_controller_2.calculate(distance_difference)

        if self.pid_controller.atSetpoint():
            rotate = 0
            # forward = 0
        # if self.pid_controller.atSetpoint() > self.goal:
        #     self.drivetrain.arcadeDrive(0,0)
        # else:
            #rotate = difference * self.kp
            #roate = 0
            #forward = .4
            # print(f"Fwd: {forward}, Rot: {rotate}, distance: {self.drivetrain.averageDistanceMeter}, angle difference:{angle_difference}, distance difference{distance_difference}")
        self.drivetrain.drive(rotate, forward)
