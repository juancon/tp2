print miarray[2]
for elem in miarray:
   print elem, " es un valor contenido en el array miarray"
for index in range(len(miarray)):
   print miarray[index], " es el valor contenido en el array sub ", index
index=0
for elem in miarray:
   print index, ":", elem
   index += 1
miarray.append('carlos')
miarray.index('carlos')
'miguel' in miarray
'carlitos' in miarray
undict = {'nombre':'Juan','edad':22,'dni':51022365,'direccion':'Ave María número 35, bajo dcha'}
print undict['direccion']
print undict['dni']
undict.values()
undict.keys()
for key in undict.keys():
  print key, "===>", undict[key]

