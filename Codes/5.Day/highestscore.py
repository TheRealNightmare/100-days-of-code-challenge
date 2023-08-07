scores = input("Enter scores of all students: ").split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

#max() gives highest num in list
#min() gives lowest num in list
highest_score = 0

for score in scores:
    if score>highest_score:
        highest_score = score

print(f"The highest score is: {highest_score}")