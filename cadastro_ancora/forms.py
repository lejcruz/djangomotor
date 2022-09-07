from django import forms


class CadastroAncoraForm(forms.Form):
    name = forms.CharField()
    valor_cpf_cnpj = forms.CharField(max_length=18)
