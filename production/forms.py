# production/forms.py
from django import forms
from .models import ProductionArea, Nomenclature

class ProductionAreaForm(forms.ModelForm):
    class Meta:
        model = ProductionArea
        fields = ['name', 'price']

class ImportNomenclatureForm(forms.Form):
    csv_file = forms.FileField()
