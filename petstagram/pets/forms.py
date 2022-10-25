from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Pet
        fields = ("name", "date_of_birth", "personal_pet_photo")

        labels = {
            "name": "Pet name",
            "date_of_birth": "Date of Birth",
            "personal_pet_photo": "Link to image",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Pet name",
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "personal_pet_photo": forms.TextInput(
                attrs={
                    "placeholder": "Link to image"
                }
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].required = False
    #     self.fields['personal_pet_photo'].required = False


class AddPetForm(PetBaseForm):
    pass


class EditPetForm(PetBaseForm):
    pass


class DeletePetForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

