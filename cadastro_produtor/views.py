from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView, 
                                  CreateView, ListView, 
                                  DetailView, UpdateView, 
                                  DeleteView)
from . import forms, models
from django.http import HttpResponse

# Create your views here.

class ProdutorCreateView(CreateView):
    model = models.Produtor
    template_name = 'cadastro_produtor/pages/produtor_form.html'
    form_class = forms.CadastroProdutorForm

    success_url = reverse_lazy('cadastro_ancora:thank_you')


class ProdutorListView(ListView):
    model = models.Produtor
    template_name = 'cadastro_produtor/pages/produtor_list.html'

    queryset = models.Produtor.objects.order_by('name')
    context_object_name = "produtor_list_object"


class ThankYouView(TemplateView):
    template_name = 'cadastro_produtor/pages/thank_you.html'