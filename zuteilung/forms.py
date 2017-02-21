# zuteilungen/forms.py
# -*- coding: UTF-8 -*-
import floppyforms as forms

class NewEffdt(forms.Form):
    effdt = forms.DateField()
    effdt.label = 'Gültig ab:'

    def send_data(self):
        pass

class FilialForm(forms.Form):
    activ=forms.CheckboxInput()
    flaeche=forms.FloatField()
    eigenschaft=forms.ComboField()

class WabeForm(forms.Form):
    eigenschaft=forms.ComboField()