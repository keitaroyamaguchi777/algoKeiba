from django.forms import ModelForm
from sampling.models import Uma_kihon


class UmaKihonForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Uma_kihon
        fields = ('id', 'race_key', 'blad_int', 'age', 'sex',)
