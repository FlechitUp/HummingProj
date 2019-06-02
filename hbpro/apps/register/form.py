from django.forms import ModelForm
from apps.register.models import Student

class studentForm(ModelForm):
	class Meta:
		model = Student
		fields = ('name','last_name','nick_name',
			'password','password_confir','age','e_mail',
			'number_phone','github')