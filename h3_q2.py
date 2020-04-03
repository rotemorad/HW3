

class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """
    def __init__(self, hour=00, minute=00, second=00):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_int(self):
        integers = []
        for item in [self.hour, self.minute, self.second]:
            if item is int:
                integers.append(item)
            if len(integers) == 3:
                [self.hour, self.minute, self.second] = integers


