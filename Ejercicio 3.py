listaNombre= ["Halcon Milenario", "Ala-X/X-Wing", "Destructor Estelar", "Lanzadera Imperial", "Supremacy", "Nave Real Imperial Tipo J"]
listaLongitud=[100, 76, 55, 110, 93, 66]
listaTripulantes= [22, 12, 6, 9, 15, 10] 
listaPasajeros=[25, 15, 10, 10, 15, 10]

import numpy
listaNombre=numpy.array(listaNombre)
listaLongitud=numpy.array(listaLongitud)
inds = listaLongitud.argsort()
sorted_listaNombre=listaNombre[listaLongitud]
print(sorted_listaNombre)

