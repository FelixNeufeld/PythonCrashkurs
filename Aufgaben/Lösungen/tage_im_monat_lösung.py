import sys

month = input("Gebe einen Monat als Zahl ein: ")
year = input("Gebe ein Jahr ein: ")

if (not month.isdigit()):
    print(month + " ist keine Zahl")
    sys.exit()
if (not year.isdigit()):
    print(year + " ist keine Zahl")
    sys.exit()

month = int(month)
year = int(year)

print("### Ausgabe if-else ###")
if (month > 12 or month < 1):
    print("Es gibt nur Monate von 1-12.")
    sys.exit()

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
elif(month == 2):
    if (((year % 4) == 0) and ((not ((year % 100) == 0)) or ((year % 400) == 0))):
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 29 Tage.")
    else:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 28 Tage.")
else:
    print("Der " + str(month) + ". hat im Jahr " + str(year) + " 30 Tage.")

print("### Ausgabe Switch Case ###")
match month:
    case 1:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 3:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 5:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 7:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 8:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 10:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 12:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 31 Tage.")
    case 2:
        if (((year % 4) == 0) and ((not ((year % 100) == 0)) or ((year % 400) == 0))):
            print("Der " + str(month) + ". hat im Jahr " + str(year) + " 29 Tage.")
        else:
            print("Der " + str(month) + ". hat im Jahr " + str(year) + " 28 Tage.")
    case _:
        print("Der " + str(month) + ". hat im Jahr " + str(year) + " 30 Tage.")