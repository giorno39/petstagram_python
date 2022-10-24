from django import forms

from petstagram.photos.models import Photo


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


# class DeletePhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         if commit:
#             self.instance.tagged_pets.clear()
#
#             Photo.objects.all() \
#                 .first().tagged_pets.clear()
#             # PhotoLike.objects.filter(photo_id=self.instance.id) \
#             #     .delete()  # one-to-many
#             # PhotoComment.objects.filter(photo_id=self.instance.id) \
#             #     .delete()  # one-to-many
#         self.instance.delete()
#
#         return self.instance
