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

################################ward####################################
path('add_ward/', ward_Adding, name='add_ward'),
path('select_government/', select_government, name='select_government'),
path('ward_list/', ward_list, name='ward_list'),
path('edit_ward/<str:ward_id>/', ward_edit, name='edit_ward'),
path('delete_ward', ward_delete, name='delete_ward'),

################################DEPARTMENT#################################
path('add_dep/', department_add, name='add_dep'),
path('dep_list/', dep_list, name='dep_list'),
path('edit_dep/<str:pk>/', dep_edit, name='edit_dep'),
path('delete_dep', dep_delete, name='delete_dep'),

path('get_dep_data', get_dep_data, name='get_dep_data'),
path('allocate_dep/', allocate_dep_page, name='allocate_dep'),
path('allocate_department/', allocate_dep, name='allocate_department'),
    # ajax
    # path('get_branch_location_data', get_branch_location_data, name='get_branch_location_data'),

]