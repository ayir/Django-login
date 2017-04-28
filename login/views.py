from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {'form': form })
    ctx = {
        'form' : form,
        'variables' : variables
    }
 
    return render(request, 'registration/register.html',ctx)
 
def register_success(request):
    return render(request,'registration/success.html')
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render(request,'home.html',{ 'user': request.user }
    )

# there is major change in rendering views in the django 1.10 
# try to use render function instead of render_to_response
# otherwise it will not run the {% csrf_token %} in views 
# and there is a 403 error
