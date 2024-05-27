from database.DB_connect import DBConnect
from model.tabObjects import Object
from model.Arco import Arco
class DAO():

    #cancello l'__init__() della classe dao dove faro solo staticmethods
    #def __init__(self):
    #   pass

    @staticmethod
    def ottieniOggettiObject(): #che saranno i nodi del grafo
        # devo creare in cartella modelil file con la relativa dataclass per la tabella Objects da cui voglio estrarre righe in oggetti

        oggettoConnessione= DBConnect.get_connection()
                        #metodo di classe DBconnect gia definito da traccia e che vale sempre inteoria quindi con sto nome

        listaOggettiObject=[]

        cursor= oggettoConnessione.cursor(dictionary=True)

        query= "SELECT * FROM objects"
        #prendo tutte le righe dalla tabella objects

        cursor.execute(query, ())
        #eseguo la query , senza parametri quindi con secondo argomento del metodo ();

        for row in cursor:
            #dove row è un dizionario relativo a un una riga dell atabella objects
            #del database con attributi della tabella e valori di quella riga
            #Con questo dizionario ci devo costruire l'oggetto e aggiungerlo alla lista
            #di oggetti che voglio ottenere come risultato  tramite il costruttore della classe Object ovviamente
            #(sono 12 gli attributi di istanza di classe object, da 0 a 11)


            #ALLORA DEVO FARE
            #listaOggettiObject.append(Object(object_id=row["object_id"],classification=row["classification"],......fin ultimo attributo
            #CHE E' LA STESSA COSA DI FARE:
            #o=Object(**row)
            listaOggettiObject.append(Object(**row))
            #se nomi attributi nella classe Object sono uguali a quelli della tab del dizionario (quindi senza underscore davanti pure se in tab non c è)
            #CHE  E' MOLTO PIU CORTO !!!!
                                    #PS. devo importare da cartella model il file tabObjects;

                                        # devo chiamare la classe Object di quel file del model importato;
        cursor.close()
        oggettoConnessione.close()

        return listaOggettiObject


    @staticmethod
    def ottieniArchi(dizionario_idNodi_nodi): #che saranno gli archi;
        #non serve il self a parametro perchè è un staticmethod come sempre nel DAO

        oggettoConnessione= DBConnect.get_connection()
        oggettoCursore=oggettoConnessione.cursor(dictionary=True)

        listaArchi=[]

        #join della tabella exihbition_objects con se stessa;
        #tra righe con stesso attributo exibhition:id ma con diverso attributo object_id
        # (< perchè non voglio righe con due stessi object_id e stesso exibhition_id ma con i due object_id in posizione invertita
        #tenendo solo (group by) le righe con stessa coppia di valori in attributi object_id;
        #seleziono i valori degli attributi object_id che rinomino a mio modo e count(*) che è riferito alla selezione
        #alla selezione fatta dal gruop by...assegnadno ad ogni riga come nuovo attributo che chiamo peso il numero di volte che altrimenti quei due stessi due valori in attributo object_id
        #sarebbero comparsi nella tabella;
        query="""SELECT tab1.object_id as nodo1, tab2.object_id as nodo2, count(*) as peso
                 FROM exhibition_objects as tab1 , exhibition_objects as tab2
                 WHERE tab1.exhibition_id = tab2.exhibition_id
                       and
                       tab1.object_id < tab2.object_id
                 GROUP BY tab1.object_id, tab2.object_id
                """
                # ORDER BY peso desc se volevo ordinate per peso decrescenti le righe

        oggettoCursore.execute(query, ())

        for row in oggettoCursore:
            listaArchi.append(Arco(dizionario_idNodi_nodi[row["nodo1"]], dizionario_idNodi_nodi[row["nodo2"]], row["peso"]))
                             #costruisco oggetto arco (chiamando dal dizionario a parametro) con nel primo campo del costruttore l Object avente come  object_id quello che ho salvato
                             #nella chiave del dizionario row chiamata come nodo 1, nel second ocampo nodo 2 e nell'ultimo campo il peso ;
                             #occhio ch echiavi vanno tra virgolette


        oggettoCursore.close()
        oggettoConnessione.close()

        return listaArchi

