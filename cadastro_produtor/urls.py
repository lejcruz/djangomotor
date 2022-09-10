from django.urls import path
from . import views

app_name = 'cadastro_produtor'

urlpatterns = [
    path('', views.ProdutorAddView.as_view(), name='cadastro_produtor'),
    path('lista_produtor/', views.ProdutorListView.as_view(), name='lista_produtor'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you_prod'), 
]