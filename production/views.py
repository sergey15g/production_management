# production/views.py
from django.shortcuts import render, redirect
from .forms import ProductionAreaForm, ImportNomenclatureForm
from .models import ProductionArea, Nomenclature, NomenclaturePrice

def add_production_area(request):
    if request.method == 'POST':
        form = ProductionAreaForm(request.POST)
        if form.is_valid():
            production_area = form.save()
            return redirect('add_production_area')
    else:
        form = ProductionAreaForm()
    return render(request, 'add_production_area.html', {'form': form})

def import_nomenclature(request):
    if request.method == 'POST':
        form = ImportNomenclatureForm(request.POST, request.FILES)
        if form.is_valid():
            # Логика обработки CSV файла и создание номенклатур
            # ...
            return redirect('import_nomenclature')
    else:
        form = ImportNomenclatureForm()
    return render(request, 'import_nomenclature.html', {'form': form})
