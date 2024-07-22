from django import forms
from .models import Infos_Artistas

class CadastroArtista(forms.ModelForm):
    class Meta:
        model = Infos_Artistas
        fields = "__all__"