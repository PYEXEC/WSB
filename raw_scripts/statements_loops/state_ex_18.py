import calendar

months_list = "Lista miesięcy: "
for month in calendar.month_name:
    months_list += f"{month} "

print(months_list)
month_name = input("Wprowadź nazwę miesiąca spośród podanych: ")

if month_name == "February":
    print("Liczba dni: 28/29")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("Liczba dni: 31")
elif month_name in ("April", "June", "September", "November"):
    print("Liczba dni: 30")
else:
    print("Nieprawidłowa nazwa miesiąca")
