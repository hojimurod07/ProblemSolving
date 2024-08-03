class TimeZone:
    def __init__(self, vatq):
        self.hour = int(vatq.split(":")[0])
        self.minute = int(vatq.split(":")[1])
        self.second = int(vatq.split(":")[2])

    def display(self):
        print(f"{self.hour:02d} : {self.minute:02d} : {self.second:02d}")

    def pilusHundred(self):
        total_minutes = (self.hour * 60) + self.minute + 100
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def qanchaQoldi(self):
        total_minutes_today = 24 * 60
        current_minutes = (self.hour * 60) + self.minute
        remaining_minutes = total_minutes_today - current_minutes
        hours_left = remaining_minutes // 60
        minutes_left = remaining_minutes % 60
        print(f"{hours_left} soat {minutes_left} minut qoldi")

a = TimeZone("7:00:00")
a.pilusHundred()
a.display()
