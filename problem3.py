

class Worker:
    def __init__(self,surname,position,salary):
        self.surname = surname
        self.position = position
        self.salary  = salary
        if self.surname.startswith("Abdulla"):
            self.position = "Injiner " + self.position

    def add_salary(self):
        self.salary = (self.salary/100)*15+self.salary

    def tanishtir(self):
        print(f"{self.surname}  {self.position}  {self.salary}")



w = Worker("Polat","admin",100)
w2 = Worker("Abdullayev","admin",100)

w2.tanishtir()