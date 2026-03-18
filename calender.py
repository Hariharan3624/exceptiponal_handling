import calendar
b = int(input("what year of calender do you want: "))
c = calendar.TextCalendar(calendar.MONDAY)
a = c.formatyear(b)
print(a)