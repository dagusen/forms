from django import forms
from .models import Detail

class StudentForm(forms.ModelForm):
	class Meta:
		model = Detail
		fields = ['first_name',
		'last_name',
		'middle_name',
		'age',
		'birthday',
		'course']