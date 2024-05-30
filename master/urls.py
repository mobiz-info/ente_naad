from django.urls import path
from .views import *

urlpatterns = [
 path('', home, name='home'),
 path('panchayath_list/', panchayath_list, name='panchayath_list'),
 path('add_panchayath/', Panchayath_Adding, name='add_panchayath'),
 path('edit_panchayath/<str:pk>/', Panchayath_editing, name='edit_panchayath'),
 path('delete_panchayath', panchayath_delete, name='delete_panchayath'),

 ################################corporation####################################
path('add_corporation/', corporation_Adding, name='add_corporation'),
path('corporation_list/', corporation_list, name='corporation_list'),
path('edit_corporation/<str:pk>/', corporation_editing, name='edit_corporation'),
path('delete_corporation', corporation_delete, name='delete_corporation'),

################################muncipality####################################
path('add_muncipality/', muncipality_Adding, name='add_muncipality'),
path('muncipality_list/', muncipality_list, name='muncipality_list'),
path('edit_muncipality/<str:pk>/', muncipality_editing, name='edit_muncipality'),
path('delete_muncipality', muncipality_delete, name='delete_muncipality'),

]