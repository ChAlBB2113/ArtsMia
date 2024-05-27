import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):

        self._model.creaGrafo()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumeroNodiGrafo()} nodi e {self._model.getNumeroArchiGrafo()} archi"))
        self._view.update_page() #metodo di classe view gia fatto dai prof che fa l'update della pagina della view

    def handleCompConnessa(self,e):

        inputUtenteIdOggetto=self._view._txtIdOggetto.value

        #se converto in intero un imput utente devo sempre farlo con un try
        #PS variabuli devinite nel try sono visibili anche appena fuori dal try/except
        try:
            inputConvertitoInIntero=int(inputUtenteIdOggetto)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Il valore inserito non è un intero"))
            #dopo except esco da tutto quindi prima si deve aggiornare la pagina!!
            self._view.update_page()

        #QUANDO UTENTE DA IN INPUT VALORE DI UN ATTRIBUTO CHE DA DATABASE E' UN
        #INTERO E' BENE SEMPRE SUBITO CONVERTIRLO IN INTERO
        #AFFINCHE OPERAZIONI SUCESSIVE FUNZIONINO; BENE GIA QUI NEL METODO DEL CONTROLLER,
        #PER DARE IN IMPUT A METODI DEL MODEL GIA UN INTERO ,
        #COSI NON DEVO STARE A FARE TENTATVIO DI CONVERSIONE NEI METODI DEL MODEL POI

        if (self._model.controllaEsistenzaNodoDatoId(inputConvertitoInIntero)) is True:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto con id {inputConvertitoInIntero} è presente nel grafo"))

            #punto d) del tema di esame
            numeroNodiConnessi = self._model.getNumeroNodiConnessi(inputConvertitoInIntero)
            self._view.txt_result.controls.append(ft.Text(    f"componente connessa che include il nodo {inputConvertitoInIntero} ha un numero di nodi pari a {numeroNodiConnessi}"))

        else:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto con id {inputConvertitoInIntero} NON è presente nel grafo"))

        #se non sono entrato nell'except è stato fatto il corpo del Try e
        #(visibile anceh da fuori blocco tra/except) e si è proseguito;
        #prima ceh funzioni termini e si esca da tutto come ovgni volta che corpo di una
        #funzione ha effetti sulla pagina ed è terminato, va aggiunto l'aggiornamento della pagina
        #(cosa fatta anceh al termine del blocco except che a sua volta aveva istruzioni
        #con effetto su elementi della pagina
        self._view.update_page()
        #come l'ho messo nell'else poitevo metterlo nell'if pure dato ceh non c'erano
        #altre cose fuori dall'if/else poi