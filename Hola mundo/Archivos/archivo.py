texto = open('victor.txt')
#print(texto.read()) #De esta forma abrimos y leemos todo el doc

for textito in texto:  #mediante el uso del for podemos ñeer el achivo lina por linea sin necesidad de readline
    print(textito)

texto.close() #cerramos el archivo 