


class Book:
    def __init__(self,name,page_count,price):
        self.page_count = page_count
        self.price = price
        self.name = name
        if self.page_count>100:
            self.price = self.price//2

    def oshir(self):
        self.page_count = self.page_count+10

    def display(self):
        print(f"{self.name} {self.page_count} {self.price}")

a = Book("aa",120,500)
a.display()