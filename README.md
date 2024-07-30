
# Video to MP3 Converter

## Descrizione
Questo progetto è un'applicazione che consente di convertire file video in file audio MP3. È stato sviluppato utilizzando Python e le librerie `moviepy`, `psutil`, `customtkinter` e `tkinter`.

## Struttura del Progetto

```
video_to_mp3_converter/
│
├── converter/
│   ├── __init__.py
│   ├── conversion.py
│   ├── gui.py
│   └── utils.py
│
├── main.py
└── requirements.txt
```

### Descrizione dei File

- **main.py**: Il punto di ingresso del programma. Avvia l'interfaccia grafica.
- **converter/**: Directory contenente i moduli per la logica di conversione e l'interfaccia grafica.
  - **__init__.py**: File vuoto che indica che `converter` è un pacchetto Python.
  - **conversion.py**: Modulo che gestisce la logica di conversione dei file video in audio MP3.
  - **gui.py**: Modulo che gestisce l'interfaccia grafica dell'applicazione.
  - **utils.py**: (Opzionale) Modulo per funzioni ausiliarie, se necessarie.
- **requirements.txt**: File che elenca tutte le dipendenze del progetto.

## Requisiti
Assicurati di avere Python 3.6 o superiore installato. Le dipendenze richieste sono elencate nel file `requirements.txt`.

## Installazione

1. Clona questo repository:
    ```bash
    git clone <repository_url>
    cd video_to_mp3_converter
    ```

2. Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```

## Utilizzo

1. Avvia l'applicazione:
    ```bash
    python main.py
    ```

2. Segui questi passaggi nell'interfaccia grafica:
    - **Choose Folder**: Seleziona la cartella contenente i file video che desideri convertire.
    - **Extract Audio**: Avvia il processo di conversione.

## Funzionalità

- Selezione di una cartella contenente file video.
- Conversione dei file video selezionati in file audio MP3.
- Visualizzazione dello stato di avanzamento della conversione.
- Possibilità di interrompere il processo di conversione chiudendo l'applicazione.

## Moduli

### `conversion.py`
Gestisce la logica di conversione dei file video in MP3. Contiene le funzioni:
- `convert_to_mp3()`: Converte un singolo file video in MP3.
- `terminate_all_processes()`: Termina tutti i processi attivi e chiude l'applicazione.

### `gui.py`
Gestisce l'interfaccia grafica dell'applicazione. Contiene le funzioni:
- `start_gui()`: Avvia l'interfaccia grafica.
- `select_folder()`: Gestisce la selezione della cartella contenente i file video.
- `convert_all_videos()`: Gestisce la conversione di tutti i file video nella cartella selezionata.
- `on_closing()`: Gestisce la chiusura dell'applicazione.

## Creato da
Salvatore Gambino
