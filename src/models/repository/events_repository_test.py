import pytest
from src.models.settings.connection import db_connetction_handler
from .events_repository import EventsRepository

db_connetction_handler.connect_to_db()


@pytest.mark.skip(reason="Novo Registro No Banco De Dados")
def test_insert_event():
    event = {
        "uuid": "meu_id_para_teste",
        "title": "meu_title_para_teste",
        "slug": "meu_slug_para_teste",
        "maximum_attendees": 20
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


@pytest.mark.skip(reason="Desnecessário")
def test_get_event_by_id():
    event_id = "meu_id_para_testeiuh"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    # print(response.title)
