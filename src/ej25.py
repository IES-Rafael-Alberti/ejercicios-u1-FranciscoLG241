fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
año = fecha.split("/")[2]

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f"Dia: {dia} Mes: {mes} Año: {año}")
