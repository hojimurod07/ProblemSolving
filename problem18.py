import datetime

def find_friday_13(year):

    friday_13s = []


    for month in range(1, 13):

        date = datetime.date(year, month, 13)
        if date.weekday() == 4:
            friday_13s.append(date)

    return friday_13s


year = 2024
friday_13s = find_friday_13(year)

print(len(find_friday_13(year)))
