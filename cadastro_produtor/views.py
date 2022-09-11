from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView, 
                                  CreateView, ListView, 
                                  DetailView, UpdateView, 
                                  DeleteView)
from . import forms, models
from django.http import HttpResponse

# Create your views here.

class ProdutorAddView(TemplateView):
    template_name = 'cadastro_produtor/pages/produtor_form.html'

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset_produtor = forms.ProdutorFormSet(queryset=models.Produtor.objects.none())
        formset_produtor_cultura = forms.ProdutorCulturaFormSet(queryset=models.ProdutorCultura.objects.none())

        return self.render_to_response(
                                        {'produtor_formset': formset_produtor,
                                         'produtor_cultura_formset': formset_produtor_cultura
                                         }
                                      )

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset_produtor = forms.ProdutorFormSet(data=self.request.POST)
        formset_produtor_cultura = forms.ProdutorCulturaFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if all([formset_produtor.is_valid(), formset_produtor_cultura.is_valid()]):

            parent = formset_produtor.save(commit=False)
            # parent.save()

            child = formset_produtor_cultura.save(commit=False)
            child.produtor = parent

            # child.save()

            print("form1: " , formset_produtor.cleaned_data)
            print("form2: " , formset_produtor_cultura.cleaned_data)

            return redirect(reverse_lazy('cadastro_produtor:thank_you_prod'))

        else:
            parent = formset_produtor.save(commit=False)
            child = formset_produtor_cultura.save(commit=False)
            print("Não Deu Certo")
            print(parent.cleaned_data)
            print(child.cleaned_data)

        return self.render_to_response(
                                        {'produtor_formset': formset_produtor,
                                         'produtor_cultura_formset': formset_produtor_cultura
                                         }
                                      )

# class ProdutorCreateView(CreateView):
#     model = models.Produtor
#     template_name = 'cadastro_produtor/pages/produtor_form.html'
#     form_class = forms.CadastroProdutorForm

#     success_url = reverse_lazy('cadastro_ancora:thank_you')


class ProdutorListView(ListView):
    model = models.Produtor
    template_name = 'cadastro_produtor/pages/produtor_list.html'

    queryset = models.Produtor.objects.order_by('name')
    context_object_name = "produtor_list_object"


class ThankYouView(TemplateView):
    template_name = 'cadastro_produtor/pages/thank_you.html'

