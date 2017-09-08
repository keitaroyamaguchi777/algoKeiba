from django.forms import ModelForm
from sampling.models import Uma_kihon


class UmaKihonForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Uma_kihon
        fields = ('blad_int', 'name', 'birthday', 'sex',)
