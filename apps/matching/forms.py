from django import forms
from .models import AlbumImage


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = AlbumImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'onchange': 'readURL(this)',
                    'class': 'mx-auto w-75'
                }
            )
        }
