class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def check_int(self):
        """Checks if the hour,minute and second are integers"""
        return [item if type(item) == int else 0 for item in [self.hour, self.minute, self.second]]

    def check_positive(self):
        """Checks if the hour,minute and second are positive numbers"""
        return [num if num >= 0 else 0 for num in self.check_int()]

    def check_time(self):
        """Checks if the hour,minute and second are valid in a 24 hour clock"""
        time = self.check_positive()
        if time[0] not in range(24):
            time[0] = 0
        if time[1] not in range(60):
            time[1] = 0
        if time[2] not in range(60):
            time[2] = 0
        return time

    def add_zero(self):
        """Checks if the hour,minute and second are single digits- if so add 0 in front of them to get a double digit
        number """
        new_format = []
        for num in self.check_time():
            if num in range(10):
                str_num = str(num)
                num = str_num.zfill(2)
            new_format.append(num)
        return new_format

    def __str__(self):
        str_to_print = f"""The time is:
            {self.add_zero()[0]}:{self.add_zero()[1]}:{self.add_zero()[2]}"""
        return str_to_print

    # Define a Time().is_after(other_time) method. that returns True if the first Time() is later than the other_time
    # instance, and False otherwise. 00:00:00 is the earliest, 23:59:59 is the latest.
    def is_after(self, other):
        """Checks if time is after other time and returns bool"""
        # TODO not working properly
        time = self.check_time()
        other_time = other.check_time()
        if time != other_time:
            timing = [(time[0] - other_time[0]), (time[1] - other_time[1]), (time[2] - other_time[2])]
            if timing[0] in range(24) and timing[1] in range(60) and timing[2] in range(60):
                return True
        return False

    def __add__(self, other):
        time = self.check_time()
        other_time = other.check_time()
        timing = [(time[0] + other_time[0]), (time[1] + other_time[1]), (time[2] + other_time[2])]
        while timing[2] not in range(60):
            timing[2] -= 60
            timing[1] += 1
        while timing[1] not in range(60):
            timing[1] -= 60
            timing[0] += 1
        while timing[0] not in range(24):
            timing[0] -= 24
        return timing


def main():
    time = Time(hour=1, minute=59, second=59)
    time2 = Time(hour=1, minute=0, second=0)
    print(time.__str__())
    print(time2.is_after(time))
    print(time.__add__(time2))


if __name__ == '__main__':
    main()
