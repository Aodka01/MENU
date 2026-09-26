from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    # Public creation/edit/delete removed — manage dishes from the Django admin only
]
