

class Employee:
    def __init__(self,surname,position,salary):
        self.surname = surname
        self.position = position
        self.salary = salary

    def display(self):
        print(f"{self.surname} {self.salary} {self.position}")


class Enterprice_Employee(Employee):
    def __init__(self,surname,position,salary,rayting):

        if rayting in range(60,75):
            salary = salary+ (salary//100)*20
        elif rayting in range(75,90):
            salary = salary + (salary // 100) * 40
        elif rayting in range(90,100):
            salary = salary + (salary // 100) * 60
        super().__init__(surname,position,salary)
        self.raiting = rayting



