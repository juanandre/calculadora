import sys
print('1 - Suma')
print('2 - Resta')
print('3 - Multiplicacion')
print('4 - Division')
print('5 - Potencia')
operacion = int(input('Seleccione el numero de la operacion:'))

a = int(input('Ingrese el primer numero: '))

if operacion==1:
	b = int(input('Ingrese el segundo numero: '))
	print('El resultado de la suma es: ', a + b)
elif operacion==2:
	b = int(input('Ingrese el segundo numero: '))
	print('El resultado de la resta es: ', a - b)
elif operacion==3:
	b = int(input('Ingrese el segundo numero: '))
	print('El resultado del producto es: ', a * b)
elif operacion==4:
	b = int(input('Ingrese el denominador: '))
	try:
		resultado = a/b
		print('El resultado de la division es: ', resultado)
	except ZeroDivisionError:
		print('No se puede dividir entre 0')

elif operacion==5:
	b = int(input('Ingrese exponente: '))
	print('El resultado de la otenciacion es: ', a ** b)
else:
	print('Opcion Incorrecta')


#except ZeroDivisionError:
#	print('No es posible dividir entre cero')