from .models import Car,Supplier,CustForm,Profit,sales
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['model_name','release_year','body_style','transmission','mileage','seating_capacity','cargo_capacity','cargo_capacity','car_dimension','tyre_strength','color','price','quantity']

class CustForm(forms.ModelForm):
    class Meta:
        model=CustForm
        fields='__all__'

class NICForm(forms.Form):
    NIC=forms.CharField(label='NIC',max_length=100)

class modelForm(forms.Form):
    model_name=forms.CharField(label='Model Name',max_length=100)
    release_year=forms.CharField(label='Release Year',max_length=100)

   

class suppnameform(forms.Form):
    supp_name=forms.CharField(label='Supplier Name',max_length=100)
    supp_address=forms.CharField(label='Supplier Address',max_length=100)

   

class Supplier(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'
class Profit(forms.ModelForm):
    class Meta:
        model=Profit
        fields='__all__'



class SalesForm(forms.ModelForm):
    class Meta:
        model = sales
        fields = ['car_id', 'supplier_id', 'cust_id', 'price']


class YearSelectionForm(forms.Form):
    year_choices = [(year, year) for year in range(2000, 2025)]
    year = forms.ChoiceField(choices=year_choices)
class CustdataForm(forms.Form):
    Enter_Model_Name=forms.CharField(max_length=100)
class CardataForm(forms.Form):
    Enter_Car_Model=forms.CharField(max_length=100)
    Enter_release_Year=forms.CharField(max_length=100)
class UpdateForm(forms.Form):
    f_name=forms.CharField(max_length=10)
    l_name=forms.CharField(max_length=10)
    NIC=forms.CharField(label='NIC',max_length=100)
    Enter_Car_Model=forms.CharField(max_length=100)
    Enter_release_Year=forms.CharField(max_length=100)
from django import forms

class NCUSTForm(forms.Form):
    New_Customer_NIC = forms.CharField(label='New Customer NIC', max_length=100)
    New_Customer_Name = forms.CharField(label='New Customer Name', max_length=100)


class login(forms.Form):
    Name = forms.CharField(label='Name', max_length=100)
    Password = forms.CharField(label='Password', max_length=100)

