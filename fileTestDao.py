from database.DAO import DAO
#importo file DAO.py da cartella database con notazione puntata
#dentro il file DAO cè la classe DAO che ha il metodo che vogio testare
from model.model import Model

#infatti qui sotto vado a chiamare da cartella, il file, la classe, il metodo
print(len(DAO.ottieniOggettiObject()))
#chiamo funzione ottieniOggettiObject di DAO.py di cartella database
#!!!la chiamo sul niente; perchè i metodi DAO sono metodi @staticmethod
#   non hanno istanze; vanno nel database e prendono e ritornare quel che devono;

#provo a stampare la lunghezza della lista che tale metodo ritorna

#print(database.DAO.DAO.ottieniPesoArchi(database.DAO.DAO.ottieniOggettiObject()[0], database.DAO.DAO.ottieniOggettiObject()[1]))

#per testare metodo DAO.ottieniArchi devo dare a parametro il dizionario
#dei nodi di un oggetto model
oggettoModel=Model()
print(len(DAO.ottieniArchi(oggettoModel.dizionarioNodi)))
