from dataclasses import dataclass
from model import tabObjects
@dataclass
class Arco:
    object_nodo1: tabObjects.Object
    object_nodo2: tabObjects.Object
    peso: int

    def __str___(self):
        return f"arco: {self.object_nodo1}, {self.object_nodo2},{self.peso} "
