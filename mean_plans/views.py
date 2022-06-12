from django.shortcuts import render

# Create your views here.
def index_mp( request ):
    """Simple direction of the request to an html"""
    return render( request, 'mean_plans/index.html' )

