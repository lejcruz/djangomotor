
from django.urls import path
from . import views

app_name = 'cadastro_ancora'

urlpatterns = [
    path('', views.AncoraAddView.as_view(), name='cadastro'),
    path('lista_ancoras/', views.AncoraListView.as_view(), name='lista_ancoras'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'), 
]