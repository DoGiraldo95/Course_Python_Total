'''
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones. 
'''

nombre_vendedor = input('Ingrese nombre del vendedor: ').title()
ventas = float(input('Ventas totales del mes: '))
comision = round((ventas*0.13))

print(f'''El vendedor := {nombre_vendedor.upper()}
Comision mes:= ${comision}''')
            