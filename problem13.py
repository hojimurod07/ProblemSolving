

ls = [23,503,100,230,7]

news = list(map(lambda x: int(str(x)[::-1]),ls[::-1]))

print(news)