from django.shortcuts import render,redirect
from django.contrib.auth import login  as dj_login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import input_quote
from .forms import inputquoteForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import myUserCreationForm,FeedbackForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def Quote(request):
    if request.method == 'POST':
        form = inputquoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')

    else:
        form = inputquoteForm()

    return render(request, 'myApp/addquote.html', {'form': form}) 
            



def index(request):
      quotes=input_quote.objects.all()

      return render(request,'myApp/index.html',{'quotes':quotes})

def registrations(request):
    context
    form=UserCreationForm()
    return render(request,'myApp/registrations.html',{'form':form})  

def login(request):
    form=myUserCreationForm()
    return render(request,'myApp/login.html',{'form':form})

def success(request):
    context={}
    context['user']=request.user
    return render(request,'myApp/success.html',context)





def logmein_p(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request,username=username,password=password)
        

        if user is not None:
            dj_login(request,user)
            if 'next' in request.POST:
             return redirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('success'))

        else:
            context['error']=" Error wrong username or password"

            return render(request, 'myApp/login.html',context)
    else:
        return render(request, 'myApp/login.html',context)    

@login_required(login_url="login")
def addquote(request):
    form=inputquoteForm()
    return render(request,'myApp/addquote.html',{'form':form})




               
def logmeout_p(request):
    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = myUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')

    else:
        form = myUserCreationForm()

    return render(request, 'myApp/registrations.html', {'form': form})



def feedback(request):

    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('thanks')
    else:
        f = FeedbackForm()
    return render(request, 'myApp/feedback.html', {'form': f})


def thanks(request):
    return render(request, 'myApp/thanks.html')   








    