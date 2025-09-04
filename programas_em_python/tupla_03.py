from collections import namedtuple
coordenadas = namedtuple('coordenadas', ["latitude", "longitude"])

casa_coordenadas = coordenadas(1,8)

print(casa_coordenadas)
print(casa_coordenadas.latitude)
print(casa_coordenadas.longitude)