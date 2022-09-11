from django import forms
from . import models


class CadastroProdutorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.keys():
            
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Produtor
        fields = "__all__"


ProdutorFormSet = forms.modelformset_factory(
    model=models.Produtor,
    form=CadastroProdutorForm,
    fields=("__all__"),
    extra=1
)

class CadastroProdutorCulturaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.keys():

            if field != 'produtor':
            
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.ProdutorCultura
        fields = ["cultura", "area"]

ProdutorCulturaFormSet = forms.modelformset_factory(
    model=models.ProdutorCultura,
    form=CadastroProdutorCulturaForm,
    fields=("__all__"),
    extra=1
)