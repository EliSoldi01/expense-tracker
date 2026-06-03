Transactions

ID: integer, auto-increment, unique. Identificativo della transazione
Type: income/expense, required. Tipologia di transazione (entrata/uscita)
Date: date, required. Data della transazione.
Amount: float, >0, required. Importo della transazione.
Category: id, from catagories table, required. Categoria della transazione.
Description: text, optional. Descrizione della transazione (es. nome negozio, motivazione, etc.)

Categories

ID: integer, auto-increment, unique. Identificativo della categoria
Name: text, required, unique. Nome della categoria
Type: text, required. Tipologia di categoria (entrata/uscitaHo)
