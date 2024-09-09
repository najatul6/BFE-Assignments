from boot.service.person_service import PersonService
from pweb import Blueprint

person_url_prefix = "/person"
person_controller = Blueprint(
    "person_controller",
    __name__,
    url_prefix=person_url_prefix
)
person_service = PersonService()


@person_controller.route("/create", methods=['POST', 'GET'])
def create():
    return person_service.create()


@person_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    return person_service.details(id)


@person_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return person_service.update(id)


@person_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return person_service.delete(id)


@person_controller.route("/", methods=['GET'])
@person_controller.route("/list", methods=['GET'])
def list():
    return person_service.list()
