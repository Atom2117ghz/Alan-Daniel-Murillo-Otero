x1 = abs(float(input("x1")))
x2 = abs(float(input("x2")))
y1 = abs(float(input("y1")))
y2 = abs(float(input("y2")))
from math import sqrt
def distanciam(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
def distanciae(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("quieres euclidianna o manhattan? m/e")
while True:
 moe =input()
 if moe == "m":
  print(distanciam(x1, y1, x2, y2))
  break
 elif moe == "e":
  print(distanciae(x1, y1, x2, y2))
  break
 else:
    print("escoge m o e")
