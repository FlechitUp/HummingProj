from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .form import loginForm
from apps.user.models import Student2, Mentor
from django.contrib import messages

def login(request):
	#import pudb;	pudb.set_trace()
	#context = RequestContext(request)
	if request.method == 'POST':
		form = loginForm(request.POST)
		#user = authenticate(username=form.fields['nick_name'], password=form.fields['password'])
		username = request.POST.get('nick_name')
		password = request.POST.get('password')
		print("oksoks!!!!!!!!!!!!!!!!!!!!!!!", username)	
		try:
			stu = Student2.objects.get(Q(nick_name=username) & Q(password=password))
			print(stu)
			return render(request, 'contentuser/index.html')

		except Student2.DoesNotExist:
			print("Either the entry or blog doesn't exist.")
			print('!!!!!!!--***********no estas en la bd')		
			messages.warning(request, ' nickname or password does not exist')
			return redirect('login')

		"""if(username =="u1"):
			return render(request, 'contentuser/index.html')
		else:
			print('!!!!!!!--***********no estas en la bd')
			return render(request, 'login/index.html')	"""
	else:
		form = loginForm()
		return render(request, 'login/index.html', {'form': form})

    #return HttpResponse("Index")
