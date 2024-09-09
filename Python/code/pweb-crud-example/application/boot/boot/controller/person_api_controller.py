from boot.dto.person_dto import PersonCreateDTO, PersonDetailsDTO, PersonUpdateDTO
from boot.service.person_api_service import PersonApiService
from pweb import Blueprint
from pweb_form_rest import pweb_endpoint, pweb_paginate_endpoint

person_api_url_prefix = "/api/v1/person"
person_api_controller = Blueprint(
    "person_api_controller",
    __name__,
    url_prefix=person_api_url_prefix
)
person_api_service = PersonApiService()


@person_api_controller.route("/create", methods=['POST'])
@pweb_endpoint(request_obj=PersonCreateDTO, pweb_message_response=True)
def create():
    return person_api_service.create()


@person_api_controller.route("/details/<int:id>", methods=['GET'])
@pweb_endpoint(response_obj=PersonDetailsDTO)
def details(id: int):
    return person_api_service.details(id)


@person_api_controller.route("/update", methods=['POST'])
@pweb_endpoint(request_obj=PersonUpdateDTO, pweb_message_response=True)
def update():
    return person_api_service.update()


@person_api_controller.route("/delete/<int:id>", methods=['DELETE'])
@pweb_endpoint()
def delete(id: int):
    return person_api_service.delete(id)


@person_api_controller.route("/list", methods=['GET'])
@pweb_paginate_endpoint(response_obj=PersonDetailsDTO)
def list():
    return person_api_service.list()
