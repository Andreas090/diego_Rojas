var1 = int(input("Ingrese un numero entero corto: "))
var2 = int(input("Ingrese un numero entero largo:  "))
var3 = float(input("Ingrese un numero en decimales: ")) 
var4 = complex(input("Ingrese un numero complejo (ej: 9+bj): "))
var5 = input("Ingrese una cadena de texto: ") 
var6 = input("Ingrese un valor booleano (True/False): ")


# Convertir un valor booleano 

if var6.lower() == 'True': 
    var6 = True 
else:
    var6 = False 
    

# imprimir en pantalla los resultados

print("\n\n a continuacion se muestran los resultados y su tipo")
print(var1, type(var1)) 
print(var2, type(var2)) 
print(var3, type(var3))
print(var4, type(var4))
print(var5, type(var5))
print(var6, type(var6))  