from pweb import url_for
from boot.form.person_form import PersonCreateForm, PersonUpdateForm, PersonDetailsForm
from boot.model.person import Person
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class PersonService:
    form_data_crud = FormDataCRUD(model=Person)

    def create(self):
        params = {"button": "Create", "action": url_for("person_controller.create")}
        form = PersonCreateForm()
        return self.form_data_crud.create(view_name="person/form", form=form, redirect_url=url_for("person_controller.list"), params=params)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("person_controller.update", id=model_id)}
        form = PersonUpdateForm()
        return self.form_data_crud.update(view_name="person/form", model_id=model_id, update_form=form, redirect_url=url_for("person_controller.list"), params=params)

    def details(self, model_id: int):
        form = PersonDetailsForm()
        return self.form_data_crud.details("person/details", model_id=model_id, redirect_url=url_for("person_controller.list"), display_from=form)

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("person_controller.list"))

    def list(self):
        search_fields = ["name", "email"]
        return self.form_data_crud.paginated_list(view_name="person/list", search_fields=search_fields)
