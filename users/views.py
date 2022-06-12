from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register( request ):
    """Register a user"""
    if request.method != 'POST': #Blank registration form for GET method
        form = UserCreationForm()
    else: #Form with data to submit in POST mode
        form = UserCreationForm( data = request.POST )
        if form.is_valid():
            new_user = form.save()
            login( request, new_user )
            return redirect( 'learning_logs_app:index' )

    context = { 'form' : form }
    return render( request, 'registration/register.html', context )

