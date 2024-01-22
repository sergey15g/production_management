# production/urls.py
from django.urls import path, include
from .views import add_production_area, import_nomenclature

urlpatterns = [
    path('', include('pages.urls')),
    path('add_production_area/', add_production_area, name='add_production_area'),
    path('import_nomenclature/', import_nomenclature, name='import_nomenclature'),
    # Добавьте другие маршруты, если необходимо
]
