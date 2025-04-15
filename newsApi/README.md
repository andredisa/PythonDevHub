# 📰 News Aggregator con NewsAPI

Un'applicazione Python semplice ma potente che ti permette di ottenere le ultime notizie da tutto il mondo usando [NewsAPI.org](https://newsapi.org/). Puoi filtrare le notizie per paese, lingua, argomento, data, dominio, e popolarità.

---

## 🚀 Funzionalità

- 🌍 Ottieni le **principali notizie** da un paese specifico
- 🌐 Ottieni notizie in una **lingua specifica**
- 🔍 Ricerca articoli per **argomento**
- 📅 Filtra articoli per **intervallo di date**
- 🌟 Mostra gli articoli più **popolari**
- 🗞️ Ottieni articoli di un **dominio specifico**
- 📖 Mostra il **contenuto completo** del primo articolo trovato

---

## 🧰 Tecnologie Utilizzate

- Linguaggio: **Python 3.x**
- Librerie: [`requests`](https://pypi.org/project/requests/)
- API: [NewsAPI.org](https://newsapi.org/)

---

## 🛠️ Requisiti

Installa le dipendenze necessarie:

```bash
pip install requests
```
---

## 🔐 Configurazione API Key
Per far funzionare il progetto, devi registrarti su https://newsapi.org e ottenere una chiave API gratuita.

Sostituisci la chiave all'interno del file news.py:

````self.key_api = "la_tua_chiave_api" ````

`⚠️ Non pubblicare la tua chiave su repository pubblici.`

---

## 📚 Obiettivi Didattici
- ✅ Apprendere l'utilizzo delle REST API
- ✅ Esercitarsi con il parsing JSON
- ✅ Rafforzare la struttura a classi in Python
- ✅ Imparare la gestione di parametri HTTP dinamici

---

## ⚠️ Note
La versione gratuita di NewsAPI ha un numero limitato di richieste al giorno

I contenuti completi degli articoli potrebbero non essere sempre disponibili

