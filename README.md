<div align="center">
  <img src="https://cdn.pensieriincodice.it/images/pensieriincodice-locandina.png" alt="Logo Progetto" width="150"/>
  <h1>Pensieri In Codice — News to Mastodon</h1>
  <p>Pubblica automaticamente le news di PIC sull'account Mastodon del podcast, prelevandole da Readwise.</p>
  <p>
    <img src="https://img.shields.io/github/stars/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="GitHub Stars"/>
    <img src="https://img.shields.io/github/forks/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="GitHub Forks"/>
    <img src="https://img.shields.io/github/last-commit/valeriogalano/pensieriincodice-news-to-mastodon?style=for-the-badge" alt="Last Commit"/>
    <a href="https://pensieriincodice.it/sostieni" target="_blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/sostieni-Pensieri_in_codice-fb6400?style=for-the-badge" alt="Sostieni Pensieri in codice"/>
    </a>
  </p>
</div>

---

## Come funziona

Lo script interroga l'API di Readwise per recuperare le ultime news salvate, le formatta tramite un template configurabile e le pubblica sull'account Mastodon del podcast tramite le API ufficiali.

---

## Requisiti

- Python 3.11+
- Un account Mastodon con access token
- Un account Readwise con access token

---

## Variabili di ambiente

Imposta le seguenti variabili nel tuo IDE o nel sistema operativo:

```
MASTODON_TOKEN="<token di Mastodon>"
MASTODON_MESSAGE_TEMPLATE="<template del messaggio>"
READWISE_ACCESS_TOKEN="<token di accesso Readwise>"
```

| Variabile | Descrizione |
|---|---|
| `MASTODON_TOKEN` | Token di accesso di Mastodon |
| `MASTODON_MESSAGE_TEMPLATE` | Template del messaggio (vedi sotto) |
| `READWISE_ACCESS_TOKEN` | Token di accesso di Readwise |

### Template del messaggio

La variabile `MASTODON_MESSAGE_TEMPLATE` supporta i seguenti placeholder:

| Placeholder | Descrizione |
|---|---|
| `{title}` | Titolo dell'articolo |
| `{notes}` | Note dell'articolo |
| `{link}` | Link all'articolo |

Esempio:

```
"{title}\n{notes}\n\n{link}"
```

---

## Installazione e avvio

```bash
pip install -r requirements.txt
python main.py
```

---

## Contributi

Se noti qualche problema o hai suggerimenti, sentiti libero di aprire una **Issue** e successivamente una **Pull Request**. Ogni contributo è ben accetto!

---

## Importante

Vorremmo mantenere questo repository aperto e gratuito per tutti, ma lo scraping del contenuto di questo repository **NON È CONSENTITO**. Se ritieni che questo lavoro ti sia utile e vuoi utilizzare qualche risorsa, ti preghiamo di citare come fonte il podcast e/o questo repository.