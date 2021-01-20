from math import sqrt

def triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    return area

print(triangle_area(3,4,5))