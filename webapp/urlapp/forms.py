
from .models import ShorterUrl
from django import forms


# =======================================================================================================
# This is the Model form class binding with ShorterUrl model class
# =======================================================================================================
class UrlPostForm(forms.ModelForm):
    class Meta:
        model = ShorterUrl
        fields = ('original_url',)

