from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('slug', "user", )

        labels = {
            "name": "Pet name",
            'personal_photo': "Personal photo",
            "date_of_birth": "Birth date",
        }

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name...'}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True

