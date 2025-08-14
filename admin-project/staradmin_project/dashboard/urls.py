from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    # path('leads/', views.leads_view, name='leads'),
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/add/', views.lead_create, name='lead_create'),
    path('leads/edit/<int:pk>/', views.lead_update, name='lead_update'),
    path('leads/delete/<int:pk>/', views.lead_delete, name='lead_delete'),
]
