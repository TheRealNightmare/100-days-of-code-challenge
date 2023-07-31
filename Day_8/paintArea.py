import math

def calc(height, width,cover):
    area= height*width
    cans =math.ceil(area/cover)
    print(f"number of cans needed: {cans}")




h = int(input("Enter Height: "))
w = int(input("Enter Width: "))
c = int(input("Enter coverage: "))

calc(h,w,c)