from django import forms
from . import models


class CadastroAncoraForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['valor_cpf_cnpj'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Ancora
        fields = "__all__"