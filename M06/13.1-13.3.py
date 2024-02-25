import datetime

today_string = datetime.date.today()
filename = today_string.strftime('%Y-%m-%d') + '.txt'
print(filename)
