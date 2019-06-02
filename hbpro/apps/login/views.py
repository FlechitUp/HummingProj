from django.shortcuts import render
from django.http import HttpResponse
from .form import loginForm


def login(request):
	import pudb; pudb.set_trace()
	if request.method=='POST':
		form = loginForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data['nick_name']
			print(name)
			return render(request, 'initpage/index.html')
		"""
								cont.name=request.POST['name']
								cont.last_name=request.POST['email']
								cont.github=request.POST['name']
								cont.is_working=request.POST['name']
								cont.save()"""
	else:
		form = loginForm()
		return render(request, 'login/index.html',{'form':form})
 
    #return HttpResponse("Index")
