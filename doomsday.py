Day_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
Doomsday = {1:3, 2:28, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}

Date = int(input("Date"))
Month = int(input("Month Number"))
Year = int(input("Year"))



if Year%400 in range(200,300):
    Century_code = 5
elif Year%400 in range(300,400):
    Century_code = 3
elif Year%400 in range(0,100):
    Century_code = 2
else:
    Century_code = 0

Quotient = Year // 12
Rem1 = Year % 12
Rem2 = Rem1 % 4

Doom = (Quotient + Rem1 + Rem2 + Century_code) % 7

if Year%4==0 and Year%100!=0:
    Doomsday[1] = 4
    Doomsday[2] = 29

Doom = (abs(Doomsday[Month] - Date) + Doom) % 7

print ("The given date falls on", Day_of_the_week[Doom])
