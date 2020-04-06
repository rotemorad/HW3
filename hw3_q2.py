class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.valid_time = self.validate_time()

    def validate_time(self):
        """Checks if the time is valid, if not valid- changes it to default time """
        #  Checks if the hour,minute and second are integers
        self.hour, self.minute, self.second = [item if type(item) == int else 0 for item in
                                               [self.hour, self.minute, self.second]]
        #  Checks if the hour,minute and second are positive numbers
        self.hour, self.minute, self.second = [num if num >= 0 else 0 for num in [self.hour, self.minute, self.second]]
        #  Checks if the hour,minute and second are valid in a 24 hour clock
        if self.hour not in range(24):
            self.hour = 0
        if self.minute not in range(60):
            self.minute = 0
        if self.second not in range(60):
            self.second = 0
        return self.hour, self.minute, self.second

    def is_after(self, other):
        """Checks if time is after other time and returns bool"""
        if self.hour > other.hour:
            return True
        elif self.minute > other.minute:
            return True
        elif self.second > other.second:
            return True
        return False

    def __add__(self, other):
        timing = [(self.hour + other.hour), (self.minute + other.minute), (self.second + other.second)]
        while timing[2] not in range(60):
            timing[2] = timing[2] % 60
            timing[1] += 1
        while timing[1] not in range(60):
            timing[1] = timing[1] % 60
            timing[0] += 1
        while timing[0] % 24 not in range(24):
            timing[0] = timing[0] % 24
        timing = Time(hour=timing[0], minute=timing[1], second=timing[2])
        return timing

    def __str__(self):
        str_to_print = f"""The time is:
            {self.hour:02d}:{self.minute:02d}:{self.second:02d}"""
        return str_to_print
