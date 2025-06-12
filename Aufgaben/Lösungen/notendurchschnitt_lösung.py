def eingaben_sammeln() -> dict:
    grades = []
    while(True):
        pressedKey = input("Geben sie eine Note ein oder q um sich statisitken anzeigen zu lassen!")
        if(pressedKey.isalnum() and pressedKey == "q"):
            return grades
        if(pressedKey.isnumeric() and (int(pressedKey) > 1) and (int(pressedKey) < 7)):
            grades.append(int(pressedKey))

def berechne_statistiken(noten):
    min = noten[0]
    max = noten[0]
    sum = 0

    for grade in noten:
        if(min > grade):
            min = grade
        if(max < grade):
            max = grade
        sum += grade

    avg = sum/len(noten)

    dic = {
        "min": min,
        "max": max,
        "avg": avg
    }

    return dic

def printGrades(noten):
    for i in range(len(noten)):
        print("#" + str(i+1) + " " + str(noten[i]))

def printStatistics(statistic: dict):
    print("Schlechteste: " + str(statistic["min"]))
    print("Beste: " + str(statistic["max"]))
    print("Durschnitt: " + str(statistic["avg"]))
    print("Anzahl: " + str(len(statistic.keys())))

def printGradesAndStatistics(noten):
    printGrades(noten)
    statistics: dict = berechne_statistiken(noten)
    printStatistics(statistics)


grades = eingaben_sammeln()
print(grades)