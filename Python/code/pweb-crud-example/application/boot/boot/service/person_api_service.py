from boot.dto.person_dto import PersonCreateDTO, PersonUpdateDTO, PersonDetailsDTO
from boot.model.person import Person
from pweb_form_rest import RESTDataCRUD


class PersonApiService:
    rest_data_crud = RESTDataCRUD(model=Person)

    def create(self):
        return self.rest_data_crud.create(PersonCreateDTO())

    def update(self):
        return self.rest_data_crud.update(PersonUpdateDTO())

    def details(self, model_id: int):
        return self.rest_data_crud.details(model_id, PersonDetailsDTO())

    def delete(self, model_id: int):
        return self.rest_data_crud.delete(model_id)

    def list(self):
        search_fields = ["name", "email"]
        return self.rest_data_crud.paginated_list(PersonDetailsDTO(), search_fields=search_fields)
