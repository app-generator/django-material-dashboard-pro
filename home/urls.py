from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Pruebas
    path('test_request/', views.test_request, name='test_request'),

    # Servicio de firma
    path('sfirma_nuevo/', views.sfirma_nuevo, name='sfirma_nuevo'),
    path('sfirma_consulta/', views.sfirma_consulta, name='sfirma_consulta'),
    path('sfirma_descarga_pdf/<doc_id>/<status>/', views.sfirma_descarga_pdf, name='sfirma_descarga_pdf'),
]
