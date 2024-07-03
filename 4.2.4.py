import calendar
user_date= input("enter a date: ")
day,month,year = user_date.split('/')
days_in_week = ["mon","tus","wen","thur","fri","sat","sun"]
index_of_day =(calendar.weekday(int(year), int(month), int(day)))
print (days_in_week[index_of_day])
