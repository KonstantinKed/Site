from django import forms
from django.forms import Select

from .models import Inventory, Apartments, Pics, Brands
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class DateInput(forms.DateInput):
    input_type = 'date'
    format_key = '%Y-%m-%d'


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'brand', 'apt', 'loc', 'type', 'conn', 'cond', 'input_date', 'comments']
        widgets = {
            'input_date': DateInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        # self.helper.add_input(Submit('submit', 'Submit'))


class UploadPicsForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # iquery = Inventory.objects.values_list('invent_id', flat=True).distinct()
    # iquery_choices = [('', 'None')] + [(id, id) for id in iquery]
    # invent_id = forms.ChoiceField(choices = iquery_choices, required=False, widget=forms.Select())
    class Meta:
        model = Pics
        fields = ['images']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Додати'))


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'brand', 'apt', 'loc', 'type', 'conn', 'cond', 'comments']
        widgets = {
            'input_date': DateInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Оновити'))

# selection through apartment
class ApartmentSelectForm(forms.ModelForm):
    # apt_name = forms.CharField(label="Apartment", disabled=True)
    class Meta:
        model = Inventory
        fields = ['apt']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Вибрати'))

class CreateBrandForm (forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['brand_name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Додати'))