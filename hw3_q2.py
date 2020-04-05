class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.list = [self.hour, self.minute, self.second]

    def check_int(self):
        """Checks if the hour,minute and second are integers"""
        self.list = [item if type(item) == int else 0 for item in [self.hour, self.minute, self.second]]
        return self.list

    def check_positive(self):
        """Checks if the hour,minute and second are positive numbers"""
        self.list = [num if num >= 0 else 0 for num in self.check_int()]
        return self.list

    def check_time(self):
        """Checks if the hour,minute and second are valid in a 24 hour clock"""
        if self.list[0] not in range(24):
            self.list[0] = 0
        if self.list[1] not in range(60):
            self.list[1] = 0
        if self.list[2] not in range(60):
            self.list[2] = 0
        return self.list

    def add_zero(self):
        """Checks if the hour,minute and second are single digits- if so add 0 in front of them to get a double digit
        number """
        new_format = []
        for num in self.list:
            if num in range(10):
                str_num = str(num)
                num = str_num.zfill(2)
            new_format.append(num)
        return new_format

    def __str__(self):
        str_to_print = f"""The time is:
            {self.add_zero()[0]}:{self.add_zero()[1]}:{self.add_zero()[2]}"""
        return str_to_print

    def is_after(self, other):
        """Checks if time is after other time and returns bool"""
        time = self.list
        other_time = other.check_time()
        if time != other_time:
            timing = [(time[0] - other_time[0]), (time[1] - other_time[1]), (time[2] - other_time[2])]
            if timing[0] in range(24) and timing[1] in range(60) and timing[2] in range(60):
                return True
        return False

    def __add__(self, other):
        time = self.list
        other_time = other.check_time()
        self.list = [(time[0] + other_time[0]), (time[1] + other_time[1]), (time[2] + other_time[2])]
        if self.list[2] % 60 not in range(self.list[2], 60):
            self.list[2] = self.list[2] % 60
            self.list[1] += 1
        if self.list[1] % 60 not in range(self.list[1], 60):
            self.list[1] = self.list[1] % 60
            self.list[0] += 1
        if self.list[0] % 24 not in range(self.list[0], 24):
            self.list[0] = self.list[0] % 24
        return self.list


def main():
    time = Time(hour=23)
    time2 = Time(hour=5, minute=17, second=0)
    print(time.check_int())
    print(time.check_positive())
    print(time.check_time())
    print(time.__str__())
    print(time.is_after(time2))
    print(time.__add__(time2))


if __name__ == '__main__':
    main()
