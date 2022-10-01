# Ejercicio 4: Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado (IVA)
# Formula: pago_total= pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def pagoTotal(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    print(f'El pago total con impuesto de {impuesto}% es de ${pago_total}')

pagoTotal(1000,21)
