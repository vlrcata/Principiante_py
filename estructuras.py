
#Se declaran diccionarios = objetos 

clienteUno = {
    "id":5,
    "nombre":"edificio1",
    "consumo":200
}

clienteDos = {
    "id":58,
    "nombre":"edificio2",
    "consumo":500
}

#Se declara una lista 

clientesAsociados =[
    clienteUno, clienteDos
]

#Y ahora que hago con esa lista 
# Mi objetivo sera obtener la informacion de la lista
#Recorrer una lista o arreglo 
#print(clientesAsociados)

""" for i in range(2):
    print(clientesAsociados[i]["nombre"])   """

#Programemos un foreach que es un for 

#especializado en recorrer arreglos(listas)

for cliente in clientesAsociados : 
    print(cliente["id" ], "=> ", cliente  ["consumo"], "kwh")

    print(f"{cliente["id"]} => {cliente['consumo'] }kwh")


