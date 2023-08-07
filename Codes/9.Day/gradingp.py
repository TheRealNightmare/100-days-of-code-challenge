scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermoine" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

grades = {}

for i in scores:
    s = scores[i]

    if s > 90:
        grades[i] = "Outstanding"
    elif s > 80:
        grades[i] = "Exceeds Expectation"
    elif s > 70:
        grades[i] = "Acceptable"
    else:
        grades[i] = "Fail"

print(grades)