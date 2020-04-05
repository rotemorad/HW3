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
        time_integers = [item if type(item) == int else 0 for item in
                         [self.hour, self.minute, self.second]]
        #  Checks if the hour,minute and second are positive numbers
        time_positive_nums = [num if num >= 0 else 0 for num in time_integers]
        #  Checks if the hour,minute and second are valid in a 24 hour clock
        if time_positive_nums[0] not in range(24):
            time_positive_nums[0] = 0
        if time_positive_nums[1] not in range(60):
            time_positive_nums[1] = 0
        if time_positive_nums[2] not in range(60):
            time_positive_nums[2] = 0
        [self.hour, self.minute, self.second] = time_positive_nums
        return self.hour, self.minute, self.second

    def add_zero(self):
        """Checks if the hour,minute and second are single digits- if so add 0 in front of them to get a double digit
        number """
        new_format = []
        for num in self.validate_time():
            if num in range(10):
                str_num = str(num)
                number = str_num.zfill(2)
                new_format.append(number)
            else:
                new_format.append(num)
        [self.hour, self.minute, self.second] = new_format
        return self.hour, self.minute, self.second

    def __str__(self):
        str_to_print = f"""The time is:
            {self.add_zero()[0]}:{self.add_zero()[1]}:{self.add_zero()[2]}"""
        return str_to_print

    def is_after(self, other):
        """Checks if time is after other time and returns bool"""
        time = self.validate_time()
        other_time = other.validate_time()
        if time != other_time:
            timing = [(time[0] - other_time[0]), (time[1] - other_time[1]), (time[2] - other_time[2])]
            if timing[0] in range(1, 24):
                return True
            elif timing[1] in range(1, 60):
                return True
            elif timing[2] in range(60):
                return True
        return False

    def __add__(self, other):
        time = self.validate_time()
        other_time = other.validate_time()
        timing = [(time[0] + other_time[0]), (time[1] + other_time[1]), (time[2] + other_time[2])]
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
