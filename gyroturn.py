    #
    # from drivetrain import Drivetrain
    # from autoroutine import AutoRoutine
    # from wpimath.controller import PIDController
    #
    # class GyroTurn (AutoRoutine):
    #
    #     def __init__(self, drivetrain: Drivetrain):
    #         self.drivetrain = drivetrain
    #         self.goal = goal_in_meters #angle you want to get to, we are trying to realign ourselves
    #         self.pid_controller = PIDController(1/120, 1/600, 1/500)
    #         self.pid_controller.setSetpoint(self.goal)
    #         self.pid_controller.setTolerance(3)
    #         self.pid_controller.setIntegratorRange(-.3, .3)
    #         #self.kp = -1/120
    #         #self.ki = -1/1000
    #         # self.tolerance = 1
    #         # self.total_error = 0
    #     def run(self):
    #         current_reading = self.drivetrain.getGyroAngleZ()
    #         power = self.pid_controller.calculate(current_reading)
    #         #error = current_reading - self.goal
    #         #self.total_error += error
    #         #self.total_error = min(200, max(-200, self.total_error))
    #
    #         if self.pid_controller.atSetpoint():
    #             #abs(error) < self.tolerance:
    #             #got there stop moving
    #             self.drivetrain.arcadeDrive(0,0)
    #         else:
    #             power = error * self.kp + self.total_error * self.ki
    #             power = max(-.5, min(.5, power)) #if power too big - pick .5, pick max out of -.5 and whatever the min picked
    #             print(f"current reading: {current_reading=} {power=}")
    #             self.drivetrain.arcadeDrive(power, 0)
    #
    #             #P - get you there
    #             #I - steady state error
    #             #D - land softly
