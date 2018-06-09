#  crea lista miarray
miarray = ['silvia','federico','miguel','julia','evaristo']
#  escribe  un elemento de miarray
print miarray[2]
#  recorre lista escribiendo algo y sacando el contenido de cada elemento
for elem in miarray:
   print elem, " es un valor contenido en el array miarray"
#  otra manera de recorrer la lista haciendo algo por cada elemento
for index in range(len(miarray)):
   print miarray[index], " es el valor contenido en el array sub ", index
index=0
#  aún otra manera de recorrer la lista haciendo algo por cada elemento
for elem in miarray:
   print index, ":", elem
   index += 1
#  agregar un valor a la lista miarray
miarray.append('carlos')
miarray.index('carlos')
#  obtener si un valor existe en la lista miarray
'miguel' in miarray
'carlitos' in miarray
#  crear un diccionario (esto es un hash en otros lenguajes)
undict = {'nombre':'Juan','edad':22,'dni':51022365,'direccion':'Ave María número 35, bajo dcha'}
#  obtener un valor del diccionario undict dada una clave
print undict['direccion']
print undict['dni']
#  obtener todos los valores de un diccionario
undict.values()
#  obtener todas las claves o keys de un diccionario
undict.keys()
#  recorrer un diccionario mostrando cada key con su value
for key in undict.keys():
  print key, "===>", undict[key]

 
  
  
  
  
  
  
  
  
  
  
  