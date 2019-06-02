from django.forms import ModelForm
from apps.login.models import Login

class loginForm(ModelForm):
	class Meta:
		model = Login
		fields = ('nick_name','password')