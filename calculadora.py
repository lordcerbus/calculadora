# Calculadora simples 
# emplemetando mais metodos a calculadora...
import math

contador = 0
infinito = 1

def calculadoracientifica():
	operador = input('Escola a operação: ')
	ang = int(input('Digite o angulo: '))
	rad = math.radians(ang)
	operadorescientificos = {
'sen': math.sin(rad),
'cos': math.cos(rad),
'tan': math.tan(rad)
}
	print(operadorescientificos[operador])

def calculadorasimples():
	pn = float(input('Digite o primeito numero: '))
	operador = input('Escola a operação: ')
	sn = float(input('Digite o segundo numero: '))
	operadoressimples= {
'+': lambda pn, sn: pn + sn,
'-': lambda pn, sn: pn - sn,
'*': lambda pn, sn: pn * sn,
'/': lambda pn, sn: pn  /  sn,
'^': lambda pn, sn: pn ** sn,
'√': lambda pn, sn: pn ** (1/sn),
'%': lambda pn, sn: pn / 100 * sn
}
	print(operadoressimples[operador](pn, sn))
   	
while contador < infinito:
	calculator = input('Selecione o modelo de calculo:\n 1 - Simples(+,-,x,/,^,√,%) \n 2 - Cientifico(cos,sen,tan) ')

	if calculator == '2':
		calculadoracientifica()
	else:
		calculadorasimples()
