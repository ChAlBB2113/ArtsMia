from dataclasses import dataclass


@dataclass
class Object:
    object_id: int
    classification: str
    continent:str
    country:str
    curator_approved:int
    dated: str
    department:str
    medium:str
    nationality:str
    object_name:str
    restricted:int
    rights_type:str
    role:str
    room:str
    style:str
    title:str

    def __hash__(self):
        return hash(self.object_id)
    #dall'hash faccio ritornare l'hash dell'attributo che è chiave del generico oggetto della
    #tabella per la quale sto definendo la classe

    def __str__(self):
        return f"{self.object_id}-{self.object_name}"
        #che sarebbe il toString di Java
        #faccio ritornare la descrizione della stringa che comprenda la chiave dell'oggetto e un attributo per
        #il "riconoscimento logico" che è per esempio il nome