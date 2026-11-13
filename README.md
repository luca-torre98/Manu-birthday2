# 🎭 Auguri Manu — una notte all'Opera di Vienna

Un sito web regalo per i **30 anni di Manuela**: sipario animato, rivelazione a sorpresa, biglietto regalo stampabile, ambientazione da teatro d'opera e musica di **Beethoven – Für Elise**.

Il progetto è **già completo**, senza dipendenze, registrazioni, chiavi API o compilazioni. Il file MP3, lo sfondo e gli altri asset sono inclusi nel repository e funzionano su GitHub Pages.

## 🚀 Pubblicare su GitHub Pages

1. **Estrai** il file ZIP sul tuo computer. Non caricare il solo ZIP: devi caricare **i file e le cartelle al suo interno**.
2. Su [GitHub](https://github.com/new), crea un nuovo repository **pubblico**, per esempio `auguri-manu`. Usa il ramo `main`.
3. Carica **il contenuto** della cartella estratta nella **radice** del repository, mantenendo la struttura delle cartelle (in particolare `assets/` e `.github/workflows/`). Su GitHub puoi usare **Add file → Upload files → Commit changes**, trascinando i file e le cartelle. In alternativa usa GitHub Desktop o Git.
4. Apri **Settings → Pages → Build and deployment → Source** e seleziona **GitHub Actions**. Il workflow `deploy.yml` è già incluso: non devi crearne uno nuovo.
5. Vai in **Actions**, scegli il workflow **Pubblica il regalo di Manuela su GitHub Pages** e, se non è partito da solo, premi **Run workflow**. Aspetta che la pubblicazione termini con il segno di spunta verde.
6. Apri il sito all'indirizzo previsto:

   `https://TUO-USERNAME.github.io/auguri-manu/`

   Sostituisci `TUO-USERNAME` con il tuo username GitHub e `auguri-manu` con il nome effettivo del repository. Il link reale viene mostrato anche in **Settings → Pages**.

**Nota:** se GitHub Pages richiede l'abilitazione di Actions o l'approvazione del workflow, concedila dalle impostazioni del repository e riesegui il workflow. Il sito non sarà online finché non avrai creato il repository e completato la pubblicazione.

### Alternativa più semplice: deploy da `main`

Anche senza GitHub Actions puoi andare in **Settings → Pages → Build and deployment**, selezionare **Deploy from a branch**, scegliere **main** e la cartella **/(root)**, quindi fare **Save**. Entrambe le modalità funzionano perché `index.html` si trova nella radice.

## 🧪 Provare prima sul computer

Basta **aprire `index.html` con Chrome, Edge, Firefox o Safari**. La grafica, la musica e la sorpresa funzionano anche offline. Se preferisci servirlo in locale, dalla cartella del progetto esegui `python -m http.server 8000` e visita <http://localhost:8000/>.

### Verificare che funzioni

- La pagina deve mostrare l'invito per Manuela senza rivelare subito il regalo.
- Cliccando **ALZA IL SIPARIO** si apre il sipario, appare Vienna e parte la musica (i browser non consentono di avviarla senza interazione).
- Il comando **Musica ON/OFF** deve mettere in pausa o riprendere l'audio.
- Cliccando **SCOPRI IL TUO BIGLIETTO** la pagina scorre fino al regalo.
- **Stampa o salva il biglietto** apre la finestra di stampa/salvataggio PDF.
- Su telefono, testi e pulsanti devono rimanere leggibili.

Puoi controllare i file essenziali anche con `python tests/check_site.py`. GitHub Actions esegue automaticamente lo stesso controllo prima di pubblicare il sito.

## 📁 Struttura del progetto

```text
index.html                   Pagina HTML principale
style.css                    Stili, effetti, versione mobile e stampa
script.js                    Interazioni, animazioni, gestione musica
assets/
  teatro-opera.png           Scenografia originale ispirata a un teatro d'opera
  beethoven-fur-elise.mp3    Estratto musicale di pianoforte incluso
  favicon.svg                Icona del sito
.github/workflows/deploy.yml Workflow per GitHub Pages
tests/check_site.py          Controllo dei file prima del deploy
.nojekyll                    Evita la trasformazione con Jekyll
README.md                    Queste istruzioni
```

## ✏️ Personalizzare il contenuto

Modifica `index.html` per cambiare messaggi, nome e data. La data **14 novembre 2026** indica il compleanno, **non** la data della visita a Vienna. La serata specifica e i posti dell'opera non sono indicati: non vengono inventati dettagli della prenotazione.

In `style.css` puoi variare colori e caratteri; in `assets/` puoi sostituire immagini o musica lasciando invariati i nomi dei file.

### Nota sulle risorse

L'immagine è un'illustrazione evocativa di un teatro d'opera: **non** è una fotografia né una ricostruzione fedele della Wiener Staatsoper. La traccia audio è una resa strumentale prodotta appositamente per questo progetto, basata su un estratto della composizione in pubblico dominio *Für Elise* di Ludwig van Beethoven. Non sono richiesti servizi esterni.
