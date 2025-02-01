
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('case/', views.case_list, name='case_list'),
    path('case/add/', views.add_case, name='add_case'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('case/<int:case_id>/delete/', views.delete_case, name='delete_case'), 
    path('evidence/', views.evidence_list, name='evidence_list'),
    path('evidence/<int:evidence_id>/delete/', views.delete_evidence, name='delete_evidence'),
    path('case/<int:case_id>/add_evidence/', views.add_evidence, name='add_evidence'),
    path('evidence/edit/<int:evidence_id>/', views.edit_evidence, name='edit_evidence'),
    path('evidence/<int:evidence_id>/', views.evidence_detail, name='evidence_detail'),
    path('evidence/<int:evidence_id>/delete/', views.delete_evidence, name='delete_evidence'), 
    path('reports/', views.reports, name='reports'),
]
