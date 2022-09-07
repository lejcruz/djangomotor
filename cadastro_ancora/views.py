from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView, 
                                  CreateView, ListView, 
                                  DetailView, UpdateView, 
                                  DeleteView)
from . import forms, models
from django.http import HttpResponse



# Create your views here.

def home(request):

    return HttpResponse("Funcionando")


class ThankYouView(TemplateView):
    template_name = 'cadastro_ancora/pages/thank_you.html'


class AncoraCreateView(CreateView):
    model = models.Ancora
    template_name = 'cadastro_ancora/pages/ancora_form.html'
    fields = "__all__"

    success_url = reverse_lazy('cadastro_ancora:thank_you')


class AncoraListView(ListView):
    model = models.Ancora
    template_name = 'cadastro_ancora/pages/ancora_list.html'

    queryset = models.Ancora.objects.order_by('name')
    context_object_name = "ancora_list_object"
