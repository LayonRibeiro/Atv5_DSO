from cachorro import Cachorro
from gato import Gato
from canarinho import Canarinho


apollo = Cachorro(3, 3)
jullys = Gato(2,2)
zangaio = Canarinho(6,15)

print(apollo.mover())
print(apollo.latir())
print(jullys.miar())
print(zangaio.mover())
print(zangaio.cantar())