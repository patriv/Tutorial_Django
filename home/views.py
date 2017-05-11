from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import *
from home.forms import *



class Home(TemplateView):
    template_name = 'home.html'

class Register(CreateView):
    print('en register!')
    template_name = 'register.html'
    form_class = RegisterForm

    def post(self, request,*args, **kwargs):
        post_values = request.POST.copy()
        userForm = RegisterForm(post_values)

        if userForm.is_valid():
            new_user = userForm.save(commit=False)
            print(new_user.first_name)
            new_user.first_name = post_values['first_name']
            new_user.last_name = post_values['last_name']
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('register'))
        else:
            messages.error(request, "Error")
            return render (request, 'register.html', {'form':userForm})
