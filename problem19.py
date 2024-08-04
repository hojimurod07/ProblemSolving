



class Worker:
    def __init__(self,name,price,year):
        self.price = price
        self.name = name
        self.year = year

class FarmWorker(Worker):
    def __init__(self,name,price,year,date_birth):
        super().__init__(name,price,year)
        self.yosh = int(date_birth.split(".")[-1])

    def hisobla(self):
        if self.yosh>60:
            print(f"siz {self.yosh-60} yil kop ishlabsiz")
        else:
            print(f"sizga  {60- self.yosh} yil bor")