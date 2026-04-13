import json
import logging
import os
from datetime import datetime, timedelta

from readwise import Readwise
from mastodon_helper import MastodonHelper
from github_state import update_github_variable

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("main").setLevel(logging.DEBUG)


def load_published_ids() -> list:
    raw = os.environ.get('PUBLISHED_IDS', '[]')
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        logging.warning("PUBLISHED_IDS non è JSON valido, uso lista vuota.")
        return []


def save_published_ids(published_documents: list) -> None:
    update_github_variable('PUBLISHED_IDS', json.dumps(published_documents))


def main():
    midnight_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    seven_days_ago = midnight_date - timedelta(days=7)

    rw = Readwise()
    response = rw.get_published_documents(seven_days_ago.isoformat())

    if len(response) == 0:
        logging.debug("Nessun documento con tag 'published' trovato.")
        return

    published_documents = load_published_ids()

    to_publish = []
    for document in response:
        document_id = document['id']
        if document_id not in published_documents:
            to_publish.append(document)

    if len(to_publish) == 0:
        logging.debug("Tutti i documenti trovati sono stati già pubblicati.")
        return

    mastodon = MastodonHelper()
    document = to_publish[0]
    logging.debug("Pubblicazione articolo " + document['title'])
    logging.debug("Link: " + document['source_url'])
    logging.debug("Note: " + document['notes'])
    template_message = os.environ["MASTODON_MESSAGE_TEMPLATE"]
    message = template_message.format(
                  title=document['title'],
                  link=document['source_url'],
                  notes=document['notes']
              )
    try:
        mastodon.post(message)
        published_documents.append(document['id'])
        save_published_ids(published_documents)
    except Exception as e:
        # Log the exception and fail the process so the GitHub Action marks the job as failed
        logging.exception("Errore durante la pubblicazione su Mastodon: %s", e)
        raise

    logging.debug("Bye!")


if __name__ == "__main__":
    main()
