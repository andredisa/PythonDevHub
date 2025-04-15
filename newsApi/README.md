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

🔐 Configurazione API Key
Per far funzionare il progetto, devi registrarti su https://newsapi.org e ottenere una chiave API gratuita.

Sostituisci la chiave all'interno del file news.py:

python
Copia
Modifica
self.key_api = "la_tua_chiave_api"
⚠️ Non pubblicare la tua chiave su repository pubblici.

📂 Struttura del Progetto
bash
Copia
Modifica
news/
│
├── main.py          # File di avvio
├── news.py          # Classe principale con tutte le funzionalità
└── README.md        # Documentazione del progetto
▶️ Esempio di utilizzo
Esegui lo script principale:

bash
Copia
Modifica
python main.py
Esempio di output:

nginx
Copia
Modifica
Bitcoin Breaks $70,000 Again! data di pubblicazione: 2024-05-14T18:30:00Z

https://thenextweb.com/news/bitcoin-breaks-again
🧪 Funzioni Disponibili
Funzione	Descrizione
getHeadlines(country)	Titoli principali per nazione (es. "it", "us", "fr")
getHeadlinesLenguage(lang)	Titoli principali per lingua (es. "it", "en")
getByArgument(topic)	Cerca articoli per argomento (es. "AI", "crypto")
getByDate(topic, from, to)	Filtra per argomento e data (formato: "YYYY-MM-DD")
getMostPopularLenguage(lang)	Articoli più popolari in una lingua
getByArgumentDomain(arg, dom)	Articoli su un argomento da un dominio (es. "crypto", "thenextweb.com")
getByArgumentComplete(arg, lang)	Mostra il contenuto del primo articolo in base ad argomento e lingua
💡 Idee per Estensioni
Salvataggio degli articoli in un file .txt o .csv

GUI con Tkinter o PyQt

Integrazione con un bot Telegram per notifiche automatiche

Caching locale delle notizie per utilizzo offline

📚 Obiettivi Didattici
✅ Apprendere l'utilizzo delle REST API
✅ Esercitarsi con il parsing JSON
✅ Rafforzare la struttura a classi in Python
✅ Imparare la gestione di parametri HTTP dinamici

⚠️ Note
La versione gratuita di NewsAPI ha un numero limitato di richieste al giorno

I contenuti completi degli articoli potrebbero non essere sempre disponibili

👨‍💻 Autore
Realizzato per scopi didattici — sentiti libero di modificarlo e migliorarlo!