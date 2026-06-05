MVP – v0: 

L’applicazione deve implementare le seguenti funzioni: 

- Aggiungere una transazione 

- Modificare una transazione 

- Eliminare una transazione 

- Visualizzare tutte le transazioni 

Ogni transazione contiene: 

- Id transazione generato automaticamente 

- Tipologia: spesa/entrata 

- Importo: float > 0 

- Data: default = oggi 

- Categoria: string, obbligatoria, da una lista di categoria predefinite: 

    -   Spese: Alimentari, Uscita, Trasporti, Salute e benessere, Viaggio/esperienza, Cibo, Acquisti, Abbonamento, Regali, Altro 

    -   Entrate: Stipendio, Paghetta, Regalo, Altro 

- Descrizione (opzionale): campo di testo 

L’utente può visualizzare: 

- Transazioni in formato tabella 

    - tutte	 

    - ordinate per data (più recente prima) 

- Selezionare un mese e vedere un report testuale con totale spese, totale entrate 

- Selezionare un mese e vedere un grafico a barre con spese e entrate totali 