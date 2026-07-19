import json
import os
from datetime import datetime


HISTORY_FILE = "data/chat_history.json"


def _ensure_history_file():

    os.makedirs(
        "data",
        exist_ok=True
    )

    if not os.path.exists(
        HISTORY_FILE
    ):

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file
            )


def load_chat_history():

    _ensure_history_file()

    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def save_chat_session(
    title,
    document_name,
    messages
):

    history = load_chat_history()

    session = {

        "id": datetime.now().strftime(
            "%Y%m%d%H%M%S"
        ),

        "title": title,

        "document_name": document_name,

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "messages": messages

    }

    history.insert(
        0,
        session
    )

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


def delete_chat_session(
    session_id
):

    history = load_chat_history()

    history = [

        session

        for session in history

        if session["id"] != session_id

    ]

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )