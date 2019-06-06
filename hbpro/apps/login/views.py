from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .form import loginForm

def login(request):
	#import pudb;	pudb.set_trace()
	#context = RequestContext(request)
	if request.method == 'POST':
		form = loginForm(request.POST)
		user = authenticate(username=form.fields['nick_name'], password=form.fields['password'])
		print("oksoks!!!!!!!!!!!!!!!!!!!!!!!", form.fields['nick_name'])
		if user is not None:
			if user.is_active:
				login(request, user)
				# Redirect to index page.
				#return HttpResponseRedirect("rango/")
				return render(request, 'initpage/index.html')
			else:
				# Return a 'disabled account' error message
				#return HttpResponse("You're account is disabled.")
				return render(request, 'login/index.html')
		else:
			print('!!!!!!!--***********no estas en la bd')
			return render(request, 'login/index.html')
		"""if form.is_valid():
			form.save()
			name = form.cleaned_data['nick_name']
			print(name)
			return render(request, 'initpage/index.html')"""
		"""
								cont.name=request.POST['name']
								cont.last_name=request.POST['email']
								cont.github=request.POST['name']
								cont.is_working=request.POST['name']
								cont.save()"""
	else:
		form = loginForm()
		return render(request, 'login/index.html', {'form': form})

    #return HttpResponse("Index")
