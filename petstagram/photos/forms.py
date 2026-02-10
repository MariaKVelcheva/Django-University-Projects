from django import forms

from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ("date_of_publication", )

        labels = {
            "photo": "Photo",
            "tagged_pets": "Tag pets:",
            "location": "Location",
            "description": "Description",
        }

        widgets = {
            "location": forms.TextInput(attrs={"placeholder": "Where were you?"}),
        }


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    pass


