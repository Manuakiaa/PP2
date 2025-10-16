import datetime

today = datetime.date.today()
end = datetime.date(today.year, 12, 31)
left = (end - today).days

weeks = left // 7

print(f"{weeks} weeks left untill the end of the year")