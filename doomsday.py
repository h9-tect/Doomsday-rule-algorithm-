Day_of_the_week = ["الأحد", "الأثنين", "الثلاثاء", "الاربعاء", "الخميس", "الجمعه", "السبت"]
Doomsday = {1:3, 2:28, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}

Date = int(input("تاريخ اليوم" ))
Month = int(input("تاريخ الشهر"))
Year = int(input("السنه"))



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

print ("اليوم هو", Day_of_the_week[Doom])
