import math

def perimeter(s1: float, s2: float, s3: float)->float:
    return (s1+s2+s3)/2
def triangleArea(s1: float, s2: float, s3: float)->float:
    subperimeter = perimeter(s1,s2,s3)
    return round(math.sqrt(subperimeter*(subperimeter-s1)*(subperimeter-s2)*(subperimeter-s3)),1)

print(triangleArea(2,3,4))