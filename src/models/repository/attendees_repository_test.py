import pytest
from src.models.settings.connection import db_connetction_handler
from .attendees_repository import AttendessRepository

db_connetction_handler.connect_to_db()


@pytest.mark.skip(reason="Novo Registro No Banco De Dados")
def test_insert_attendee():
    event_id = "meu_id_para_teste"
    attendees_info = {
        "uuid": "meu_uuid_attende",
        "name": "attende_name",
        "email": "email@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendessRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)


@pytest.mark.skip(reason="Desnecessário por ser teste de integração")
def test_get_attendee_badge_by_id():
    attendee_id = "meu_uuid_attende"
    attendees_repository = AttendessRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(attendee)
