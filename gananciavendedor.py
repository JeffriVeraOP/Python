paxm = 0.5
pvap = 1.5

com = str(input("Ingrese el nombre del comprador: "))
cp = int(input("¿Cuántas gaseosas desea llevar?: "))
pago = cp * pvap
print("Sr(a).", com, " su cuenta es de: ", pago, " soles.")

gana = pago - (cp*paxm)
print("La ganancia total para el vendedor por esta compra sera de: ", gana, " soles.")