from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login,authenticate, update_session_auth_hash
from .forms import LoginForm, RegisterForm, ContactForm

from django.contrib.auth.forms import PasswordChangeForm
from .models import Candidate, Position, ControlVote

def sign_in(request):
     if request.method == 'GET':
         form = LoginForm()
         return render(request, 'poll/login.html', {'form': form})
     elif request.method == 'POST':
         form = LoginForm(request.POST)

         if form.is_valid():
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user = authenticate(request, username=username, password=password)

             if user:
                 login(request, user)
                 messages.success(request, f'Hi {username.title()},You have successfully logged in !!!')
                 return redirect('home')
             messages.error(request, f'Invalid username or password')
             return render(request, 'poll/login.html', {'form': form})
def log_out(request):
             messages.success(request, f'You have been logged out.')
             return redirect('login')
def sign_up(request):
     if request.method == 'GET':
         form = RegisterForm()
         return render(request, 'poll/register.html', {'form': form})

     if request.method == 'POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False)
             user.username = user.username.lower()
             user.save()
             messages.success(request, 'You have signed Up successfully.')
             login(request, user)
             return redirect('login')
         else:
             return render(request, 'poll/register.html', {'form': form})

def result(request):
    obj = Candidate.objects.all().order_by('position','-total_vote')
    return render(request, "poll/results.html", {'obj': obj})

def dashboard(request):
    return render(request, "poll/dashboard.html")
def position(request):
    # The obj variable is used to store the list of positions
    obj = Position.objects.all()
    # The render function is used to render the position page
    # obj is passed to the position page to display the list of positions
    return render(request, "poll/position.html", {'obj':obj})

def candidate(request,pos):
        # The obj variable is used to store the position object
        obj = get_object_or_404(Position,pk=pos)
        # if statement is used to check if the request method is POST
        if request.method == "POST":
            temp = ControlVote.objects.get_or_create(user=request.user, position=obj)[0]
            # if statement is used to check if the user has already voted for the position
            if temp.status == False:
                temp1 = Candidate.objects.get(pk=request.POST.get(obj.title))
                temp1.total_vote += 1
                temp1.save()
                temp.status = True
                temp.save()
                return HttpResponseRedirect('/position/')
            else:
                messages.success(request, 'you have already been voted this position.')
                return render(request, 'poll/candidate.html', {'obj': obj})
        else:
            # if the request method is not POST then the render function is used to render the candidate page
            return render(request, 'poll/candidate.html', {'obj': obj})

def candidateDetailView(request, id):
            # The obj variable is used to store the Candidate object
            obj = get_object_or_404(Candidate, pk=id)
            # The render function is used to render the candidate detail page
            # obj is passed to the candidate detail page to display the details of the candidate
            return render(request, "poll/candidate_detail.html", {'obj': obj})


def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "poll/password.html", {'form':form})

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'poll/contact.html', {'form': form})
def success(request):
   return HttpResponse('Success!')


def password(request):
    return render(request,'poll/password.html')

def home(request):
    return render(request, "poll/home.html")

def about_us(request):
    return render(request,'poll/about_us.html')

# def contact_us(request):
#     return render(request,'poll/contact_us.html')

def privacy(request):
    return render(request,'poll/privacypolicy.html')


