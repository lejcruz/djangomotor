from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView, 
                                  CreateView, ListView, 
                                  DetailView, UpdateView, 
                                  DeleteView)
from . import forms, models
from django.http import HttpResponse



# Create your views here.

class ThankYouView(TemplateView):
    template_name = 'cadastro_ancora/pages/thank_you.html'


class AncoraAddView(TemplateView):
    template_name = 'cadastro_ancora/pages/ancora_form.html'

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset_ancora = forms.AncoraFormSet(queryset=models.Ancora.objects.none())

        return self.render_to_response({'ancora_formset': formset_ancora })

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset_ancora = forms.AncoraFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset_ancora.is_valid():

            formset_ancora.save()

            return redirect(reverse_lazy('cadastro_produtor:cadastro_produtor'))

        return self.render_to_response({'formset_ancora': formset_ancora} )


class AncoraListView(ListView):
    model = models.Ancora
    template_name = 'cadastro_ancora/pages/ancora_list.html'

    queryset = models.Ancora.objects.order_by('name')
    context_object_name = "ancora_list_object"
