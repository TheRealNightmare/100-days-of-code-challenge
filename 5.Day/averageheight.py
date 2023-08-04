heights = input("Enter a list of student height: ").split()

for i in range(0,len(heights)):
    heights[i] = int(heights[i])

total = 0
for height in heights:
    total +=height
 
student = 0
for studens in heights:
    student+=1

average = round(total/student)
print(average)