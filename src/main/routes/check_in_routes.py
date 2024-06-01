from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler
from src.errors.error_handler import handler_error

check_in_route_bp = Blueprint("check_in_route", __name__)


@check_in_route_bp.route("/attendees/<attendee_id>/check_in", methods=["POST"])
def create_check_in(attendee_id):
    try:
        check_in_handler = CheckInHandler()
        http_request = HttpRequest(parametro={"attendee_id": attendee_id})
        http_response = check_in_handler.registry(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handler_error(exception)
        return jsonify(http_response.body), http_response.status_code
