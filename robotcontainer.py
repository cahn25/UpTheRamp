import wpilib


from drivestraight import DriveStraight
# from gyroturn import GyroTurn
from drivetrain import Drivetrain
from uptheramp import UpTheRamp

class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain()
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Go Up The Ramp", UpTheRamp(self.drivetrain))
        # self.chooser.addOption("Turn 90", GyroTurn(self.drivetrain, 90))
        wpilib.SmartDashboard.putData(self.chooser)




    def get_autonomous(self):
        return self.chooser.getSelected()

