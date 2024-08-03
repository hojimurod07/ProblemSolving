class Time:
    def __init__(self, time):
        self.secund = int(time.split(":")[2])
        self.minut = int(time.split(":")[1])
        self.hour = int(time.split(":")[0])

    def ish_vaqtimi(self):
        return 8 <= self.hour < 17


class Mobile(Time):
    def __init__(self, surname, operator, real_time):
        super().__init__(real_time)
        self.surname = surname
        self.operator = operator

    def ish_vaqtimi_status(self):
        return "ish vaqti" if self.ish_vaqtimi() else "ish vaqti emas"


# Example usage:
mobile = Mobile("John", "OperatorX", "09:30:00")
print(mobile.ish_vaqtimi_status())  # Output: ish vaqti

mobile2 = Mobile("Doe", "OperatorY", "18:45:00")
print(mobile2.ish_vaqtimi_status())  # Output: ish vaqti emas
