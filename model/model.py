import networkx as nx
from database import DAO
class Model:
    def __init__(self):

        #definisco la lista di oggetti che il metodo del dao mi permette di ottere dal database
        # come attributo di istanza di classe model (che non è @dataclass, quindi ha un __init__()
        #dove inserire gli attributi e/o le collezioni di istanza.
        self.listaOggettiObject= DAO.DAO.ottieniOggettiObject()

        # I grafi sono un tipo di collezione da assegnare come attributo di istanza di classe model
        # Istanziando oggetto grafo gli assegno subito gli oggetti salvati nella lista qui sopra come nodi con metodo
        #add_notes(listaNodi) degli oggetti di tipo Grafo;
        self._grafo=nx.Graph()
        self._grafo.add_nodes_from(self.listaOggettiObject)
        #un grafo normale come da indicazione della traccia (che dice sempre che grafo implementare
        #(graph, digraph, multigraph)
        #>>>>>>>
        #potevo anche creare grafo e poi aggiungere nodi separatamente
        #self.grafo=nx.Graph()
        # self.grafo.add_nodes_from(self.listaOggettiObject)

        #costruisco diziozario di oggetti Object (assegnati a rispettivo object_id come attributo)
        #come variabile di istanza e lo riempio (avendo gia sopra lista nodi
        self.dizionarioNodi= {}
        for object in self.listaOggettiObject:
            self.dizionarioNodi[object.object_id]= object

        #aggiungo come attributo di istanza la lista di archi che prendo con metodo DAO che riceve a parametro la
        #il dizionario dei nodi per poter poi costruire la lista di oggetti Arco costruendo oggetti Arco
        #chiamando gli oggetti Object da dizionario a parametro  conoscendone l'id da tabella exihbition_objects del database
        #e assegnandoli come attributoi del costruttore Arco iterando sul ogni diz del cursore
        #listaArchi= DAO.DAO.ottieniArchi(self.dizionarioNodi)

    #metodi utili che applicatio a oggetto model in controller mi daranno info su grafo da mettere
    #nella ViewList quando necessario :

    #definisco metodo che applicato all'oggetto model prenderà il grafo dell'oggetto e ne darà numero di nodi
    #(si userà un solo oggetto model nel controller!)
    def getNumeroNodiGrafo(self):
        return self._grafo.number_of_nodes()
        #potevo anche usare
        #return len(self.grafo.nodes())

    # definisco metodo che applicato all'oggetto model prenderà il grafo dell'oggetto e ne darà numero di nodi
    # (si userà un solo oggetto model nel controller!)
    def getNumeroArchiGrafo(self):
        return self._grafo.number_of_edges()
        #potevo anche usare
        #return len(self.grafo.edges())



    # metodi per aggiungere gli archi al grafo;
    def creaGrafo(self):
        self.aggiungiArchi()

    def aggiungiArchi(self):
        # pulisco (lista di) archi che gia esistono da eventuali usi precedenti dell'applicazione
        self._grafo.remove_edges_from(list(self._grafo.edges()))

        # poi prendo gli archi usando metodo del DAO
        listaArchi = DAO.DAO.ottieniArchi(self.dizionarioNodi)
        # e quindi vado ad aggiungere al grafo arco per arco della lista archi
        # col metodo add_edge() che vuole a parametri nodo1 nodo2 e eventuale peso come valore da assegnare a weight
        # dell'arco da aggiungere al grafo; elementi che io ho in attributo di
        # ciascun oggetto Arco
        for arco in listaArchi:
            self._grafo.add_edge(arco.object_nodo1, arco.object_nodo2, weight=arco.peso)


    #Metodo per controllare se , dato un object_id ci sia come nodo un Object corrispondente nel grafo
    #che è attributo di istanza di classe model
    def controllaEsistenzaNodoDatoId(self, id):

        return id in self.dizionarioNodi
               #Condizione vera se id è una chiave nel dizionario dei nodi
    #attenzione che ciò funziona se il parametro id è un intero perchè le chiavi
    #del diaionario sono i valori degli attributi object_id che come da database
    #sono degli interi!!
    #QUINDI quando nel controller inserirò l'input utente che è sempre una stringa,
    #dovrò convertirlo in intero;
    #potevo anche lasciarlo la come stringa e qui far ela conversione in intero

    def getNumeroNodiConnessi(self, idNodoPartenza):
        #occhio che metodo dfs vuole l'oggetto nodo, non il suo id;
        #mentre a parametro ricevo l'id (nel model ci infilerò l'id, l'input utente
        #che sarà già  intero visto che gia in controller appena ricevuto l'imput
        #l'ho convertito da stringa a intero in modo che fosse del tipo dell'attributo
        #che quel valore rappresenta
        dizionarioNodiConnessi=nx.dfs_predecessors(self._grafo, self.dizionarioNodi[idNodoPartenza])
        #voglio numero di nodi della componente connessa del grafo che si è quindi
        #esplorata; e quindi lunghezza della lista dei valori del dizionario in cui
        #son salvati nodi della componente connessa esplorata da metodo dfs()
        return len(dizionarioNodiConnessi.values()) +1

        #oppure potevo usare
        #dizionarioNodiConnessi=nx.node_connected_component(self._grafo, self.dizionarioNodi[idNodoPartenza])
        #return len(dizionarioNodiConnessi.values())

        # oppure potevo usare
        # DiGraphNodiConnessi=nx.dfr.tree(self._grafo, self.dizionarioNodi[idNodoPartenza])
        # return len(DiGraphNodiConnessi.nodes)

        # oppure potevo usare (suc
        # dizionarioNodiConnessi=nx.dfr.successors(self._grafo, self.dizionarioNodi[idNodoPartenza])
        # nuovoDiz={}
        # for i in dizionarioNodiConnessi.values():
        #     nuovoDiz.extend(i)
        # return len(nuovoDiz.values()) +1




