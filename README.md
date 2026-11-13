# 🎭 Auguri Manu – Fidelio alla Wiener Staatsoper

Sito regalo per i 30 anni di Manuela, firmato **Luca e Chiara**. Include la filastrocca dell'invito originale, il sipario animato, la sorpresa, un biglietto regalo stampabile, loghi estratti dal PDF fornito e un accompagnamento di Beethoven. **Non mostra alcun prezzo.**

## Pubblicazione nel repository già esistente

Repository: `https://github.com/luca-torre98/Manu-birthday2`

1. Estrai lo ZIP sul computer.
2. Apri il repository su GitHub, ramo `main`.
3. Clicca **Add file → Upload files** e carica **tutti i file estratti**, non lo ZIP.
4. Quando GitHub chiede di sovrascrivere i file omonimi, conferma il commit: i file `index.html`, `style.css`, `script.js`, i due asset già presenti e il `README.md` verranno aggiornati.
5. Verifica in **Settings → Pages**: `Deploy from a branch` → `main` → `/(root)` → **Save**.
6. Apri `https://luca-torre98.github.io/Manu-birthday2/` dopo che Pages ha pubblicato il nuovo commit. Se vedi la versione precedente, fai refresh forzato (`Ctrl+F5`).

**Non è necessario caricare altri file.** La struttura è volutamente *piatta*: ogni file sta nella cartella principale, senza `assets/`, e tutti i riferimenti sono relativi per GitHub Pages.

## Contenuti

- `index.html` — sito completo e informazioni reali sullo spettacolo
- `style.css` — scena, animazioni, grafica mobile, biglietto stampabile
- `script.js` — sipario, pulsante musica, stampa, navigazione
- `teatro-opera.png` — sfondo evocativo del teatro
- `beethoven-fur-elise.mp3` — estratto strumentale locale
- `logo-staatsoper.png` — logo estratto dal biglietto fornito
- `logo-partner.png` — loghi partner riportati sul biglietto fornito
- `qr-info-staatsoper.png` — QR **informativo** verso il sito ufficiale
- `favicon.svg` — icona del sito
- `.nojekyll` — configura la pubblicazione come sito statico

## Dati verificati dal biglietto ufficiale

**Fidelio** di Ludwig van Beethoven; **sabato 9 gennaio 2027, ore 19:00**; **Wiener Staatsoper, Opernring 2, 1010 Vienna**; **balcone laterale sinistro, fila 2, posti 17 e 18**. Il giorno **14 novembre 2026** corrisponde invece alla data di compleanno sull'invito originale.

## IMPORTANTE: codici d'ingresso

Questo è un **biglietto regalo ricordo**, non un documento valido per l'ingresso. Il QR presente nella grafica rimanda al sito ufficiale della Wiener Staatsoper e **non** permette l'accesso. I due QR originali contenuti nel PDF acquistato sono credenziali d'ingresso monouso: **non inserirli in un repository pubblico** e condividi il PDF autentico privatamente con la persona interessata. Inoltre le condizioni stampate sui biglietti indicano che modifiche ottiche, come coprire il prezzo, possono invalidare il titolo d'ingresso. Per questo il sito non contiene né biglietti originali modificati né prezzi.

## Prova locale

Dopo aver estratto il pacchetto, apri `index.html` in Chrome / Edge / Firefox. Testa il pulsante **ALZA IL SIPARIO**, l'audio di Beethoven, **SCOPRI I TUOI POSTI** e **Stampa o salva il biglietto regalo**. L'audio parte solo dopo un clic per rispettare le restrizioni del browser.
