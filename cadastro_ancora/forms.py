from django import forms
from . import models


class CadastroAncoraForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['cpf_cnpj'].widget.attrs['class'] = 'form-control validador-doc'

    class Meta:
        model = models.Ancora
        fields = "__all__"


AncoraFormSet = forms.modelformset_factory(
    model=models.Ancora,
    form=CadastroAncoraForm,
    fields=("__all__"),
    extra=1
)