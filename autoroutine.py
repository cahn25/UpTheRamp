from typing import Protocol #makes ure there are certain methods available

class AutoRoutine(Protocol):
    def run(self):
        ...

    def reset(self):
        ...
