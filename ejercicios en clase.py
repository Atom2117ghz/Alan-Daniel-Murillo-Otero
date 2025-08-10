lista=[3,5,7,9,11]
indice=lista[0]
indice2=lista[1]
indice3=lista[2]
indice4=lista[3]
indice5=lista[4]
print(indice+indice2+indice3+indice4+indice5)
print("ejercicio 2 haz un programa que detecte que es par o inpar")
print("regalame un numero porfavor uwu")
x= int(input())
resultado=x/2
print(resultado)
if resultado==type(float):
    print("es par")
else:
        print("no es")
print("ahora dame un numero para multiplicartelo hasta el 10")
y=int(input())
print(y)
print(y*1,y*2,y*3,y*4,y*5,y*6,y*7,y*8,y*9,y*10)
print("ahora vamos a promedia una lista")
lista2=[2,4,6,8,10,12]
print(lista2)
print(sum(lista2)/len(lista2))
print("ejercicio 5")
##v5=a
##v1=e
##v2=i
##v3=o
##v4=u
##print("escribe programacion letra por letra")
##l=input("ingrese la primera letra")
##if l== (v5,v1,v3,v4):
##    print("es vocal")
##    l=1
##else:
##    print("es consonante")
##switch case
opcion=1
match opcion:
    case 1:
        print("elegiste uno")
    case 2:
        print("elegistedos")
    case _:
        print("tu mama")
print("no me acuerdo cual sigue xd")
import random
x=random.randint(1,20)

while True:
  y=int(input("adivina el numero uwu"))
  if y < x:
    print("casi pero te falta")
  elif y > x:
    print("te exediste")
  else:
    print("le atinaste")
    break
print("la respuesta es:",x)