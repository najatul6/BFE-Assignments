from boot.model.person import Person
from pweb_form_rest import fields, FileField, EnumField, PWebForm


class PersonDetailsForm(PWebForm):

    class Meta:
        model = Person
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True, type="textarea")


class PersonCreateForm(PersonDetailsForm):
    class Meta:
        model = Person
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class PersonUpdateForm(PersonDetailsForm):
    class Meta:
        model = Person
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)

