class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.list_mode = [self.hour, self.minute, self.second]
        self.int = self.check_int  # bool
        self.positive = self.check_positive()  # bool
        self.format_time = self.add_zero()  # list
        self.hour_format = self.check_hour()  # bool
        self.minute_format = self.check_minute()  # bool
        self.second_format = self.check_second()  # bool

    TODO: 'not supposed to be bool, should probably include errors and exceptions'

    def check_int(self):
        integers = [item for item in self.list_mode if type(item) == int]
        if len(integers) == 3:
            return True
        else:
            return False

    def check_positive(self):
        if self.check_int():
            positive_numbers = [num for num in self.list_mode if num >= 0]
            if len(positive_numbers) == 3:
                return True
            else:
                return False
        else:
            return False

    def check_hour(self):
        if self.check_positive():
            if self.hour in range(25):
                return True
        else:
            return False

    def check_minute(self):
        if self.check_positive():
            if self.minute in range(60):
                return True
        else:
            return False

    def check_second(self):
        if self.check_positive():
            if self.second in range(60):
                return True
        else:
            return False

    def add_zero(self):  # check if hour/minute/second lower than 10- add 0 in front of them
        if self.check_positive():
            new_format = []
            for num in self.list_mode:
                if num in range(10):
                    str_num = str(num)
                    num = str_num.zfill(2)
                new_format.append(num)
            return new_format

    def __str__(self):
        str_to_print = f"""The time is:
            {self.format_time[0]}:{self.format_time[1]}:{self.format_time[2]}"""
        return str_to_print


def main():
    timing = Time(hour=24, minute=61, second=3)
    print(timing.int())
    print(timing.check_positive())
    print(timing.check_hour())
    print(timing.check_minute())
    print(timing.check_second())
    print(timing.format_time)
    print(timing.__str__())


if __name__ == '__main__':
    main()
