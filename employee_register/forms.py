from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('Username','Email','emp_code','Password','Confirm','Address')
        labels = {
            'Username':'Username',
            'emp_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Address'].empty_label = "Select"
        self.fields['emp_code'].required = False
