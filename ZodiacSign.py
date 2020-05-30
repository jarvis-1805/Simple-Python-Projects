from datetime import date

Year = input("What's your year of birth? (ex: 1992): ")
Month = input("What's your month of birth? (ex: 10): ")
Date = input("What's your date of birth? (ex: 19): ")

print("Your date of Birth is ", (Date + "/" + Month + "/" + Year))

today_date = date.today()

age = today_date.year - int(Year)
print('You are', age, 'years old')

if ((int(Month) == 12 and int(Date) >= 22) or (int(Month) == 1 and int(Date) <= 19)):
    sign = ('Capricorn')
if ((int(Month) == 1 and int(Date) >= 20) or (int(Month) == 2 and int(Date) <= 18)):
    sign = ('Aquarius')
if ((int(Month) == 2 and int(Date) >= 19) or (int(Month) == 3 and int(Date) <= 20)):
    sign = ('Pisces')
if ((int(Month) == 3 and int(Date) >= 21) or (int(Month) == 4 and int(Date) <= 19)):
    sign = ('Aries')
if ((int(Month) == 4 and int(Date) >= 20) or (int(Month) == 5 and int(Date) <= 20)):
    sign = ('Taurus')
if ((int(Month) == 5 and int(Date) >= 21) or (int(Month) == 6 and int(Date) <= 20)):
    sign = ('Gemini')
if ((int(Month) == 6 and int(Date) >= 21) or (int(Month) == 7 and int(Date) <= 22)):
    sign = ('Cancer')
if ((int(Month) == 7 and int(Date) >= 23) or (int(Month) == 8 and int(Date) <= 22)):
    sign = ('Leo')
if ((int(Month) == 8 and int(Date) >= 23) or (int(Month) == 9 and int(Date) <= 22)):
    sign = ('Vigro')
if ((int(Month) == 9 and int(Date) >= 23) or (int(Month) == 10 and int(Date) <= 22)):
    sign = ('Libra')
if ((int(Month) == 10 and int(Date) >= 23) or (int(Month) == 11 and int(Date) <= 21)):
    sign = ('Scorpio')
if ((int(Month) == 11 and int(Date) >= 22) or (int(Month) == 12 and int(Date) <= 21)):
    sign = ('Sagittarius')

print("Your Zodiac sign is", sign)